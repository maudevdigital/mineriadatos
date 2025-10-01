"""
Análisis de Clasificación Binaria - Adult Income Dataset
Implementación optimizada y profesional para Solemne I de Minería de Datos.
"""

import warnings
import matplotlib
warnings.filterwarnings('ignore')
matplotlib.use('Agg')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, make_scorer,
    roc_curve, auc, roc_auc_score
)

# Configuración global
RANDOM_STATE = 42
TEST_SIZE = 0.2
CV_FOLDS = 5

# Configuración de visualización
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.4f}'.format)
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")


def get_project_paths():
    """Obtiene las rutas del proyecto y crea directorios necesarios."""
    current_dir = Path.cwd()
    
    # Buscar directorio raíz del proyecto
    for parent in [current_dir] + list(current_dir.parents):
        if (parent / "data").exists() or (parent / "adult.csv").exists():
            project_root = parent
            break
    else:
        project_root = current_dir
    
    # Localizar archivo de datos
    data_candidates = [
        project_root / "data" / "adult.csv",
        project_root / "adult.csv"
    ]
    
    data_path = None
    for path in data_candidates:
        if path.exists():
            data_path = path
            break
    
    # Crear estructura de directorios
    results_dir = project_root / "results"
    (results_dir / "datos").mkdir(parents=True, exist_ok=True)
    (results_dir / "metricas").mkdir(parents=True, exist_ok=True)
    (results_dir / "visualizaciones").mkdir(parents=True, exist_ok=True)
    
    return data_path, results_dir


def clean_adult_data(df):
    """
    Limpia y preprocesa el dataset Adult.
    
    Returns:
        pandas.DataFrame: Dataset limpio
    """
    df_clean = df.copy()
    
    # Identificar columna objetivo
    target_candidates = ['income', 'class', 'target', 'salary']
    target_col = next((col for col in target_candidates if col in df_clean.columns), 
                      df_clean.columns[-1])
    
    if target_col != 'income':
        df_clean = df_clean.rename(columns={target_col: 'income'})
    
    # Limpieza vectorizada
    categorical_cols = df_clean.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df_clean[col] = df_clean[col].astype(str).str.strip().replace('?', np.nan)
    
    # Filtrar filas problemáticas
    missing_per_row = df_clean.isnull().sum(axis=1)
    df_clean = df_clean[missing_per_row <= 3]
    df_clean = df_clean.dropna(subset=['income'])
    
    return df_clean


def exploratory_analysis(df):
    """Realiza análisis exploratorio eficiente."""
    print("Análisis exploratorio:")
    print(f"  Dimensiones: {df.shape}")
    print(f"  Variables numéricas: {len(df.select_dtypes(include=[np.number]).columns)}")
    print(f"  Variables categóricas: {len(df.select_dtypes(include=['object']).columns)}")
    
    # Valores faltantes representados como '?'
    question_marks = {}
    for col in df.select_dtypes(include=['object']).columns:
        count = (df[col] == '?').sum()
        if count > 0:
            question_marks[col] = count
    
    if question_marks:
        print("  Valores '?' detectados:")
        for col, count in question_marks.items():
            print(f"    {col}: {count} ({count/len(df)*100:.1f}%)")


def detect_and_visualize_outliers(df, results_dir):
    """Detecta outliers y genera boxplots."""
    numeric_features = df.select_dtypes(include=[np.number]).columns
    
    if len(numeric_features) == 0:
        return
    
    # Generar boxplots optimizado
    n_cols = min(3, len(numeric_features))
    n_rows = (len(numeric_features) + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
    axes = np.atleast_1d(axes).flatten()
    
    for i, col in enumerate(numeric_features):
        if i < len(axes):
            df.boxplot(column=col, ax=axes[i])
            axes[i].set_title(f'Boxplot - {col}')
            axes[i].grid(True, alpha=0.3)
    
    # Ocultar ejes no utilizados
    for i in range(len(numeric_features), len(axes)):
        axes[i].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(results_dir / "visualizaciones" / "boxplots_outliers.png",
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    plt.clf()
    
    # Detección IQR vectorizada
    outliers_found = False
    for col in numeric_features:
        Q1, Q3 = df[col].quantile([0.25, 0.75])
        IQR = Q3 - Q1
        outliers_mask = (df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)
        outliers_count = outliers_mask.sum()
        
        if outliers_count > 0:
            if not outliers_found:
                print("  Outliers detectados (IQR):")
                outliers_found = True
            print(f"    {col}: {outliers_count} ({outliers_count/len(df)*100:.1f}%)")


def analyze_target_variable(df, results_dir):
    """Analiza variable objetivo y genera visualizaciones."""
    # Determinar clase positiva
    income_values = df['income'].unique()
    pos_label = next((val for val in income_values if str(val).startswith('>')), income_values[0])
    
    class_dist = df['income'].value_counts()
    print(f"Variable objetivo: {pos_label} vs otros")
    print("Distribución:")
    for cls, count in class_dist.items():
        print(f"  {cls}: {count} ({count/len(df)*100:.1f}%)")
    
    # Visualización compacta
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    class_dist.plot(kind='bar', ax=ax1, color=['#2E86AB', '#A23B72'])
    ax1.set_title('Distribución de Clases')
    ax1.set_xlabel('Clase')
    ax1.set_ylabel('Frecuencia')
    ax1.tick_params(axis='x', rotation=45)
    
    ax2.pie(class_dist, labels=class_dist.index, autopct='%1.1f%%',
            colors=['#2E86AB', '#A23B72'], startangle=90)
    ax2.set_title('Proporción de Clases')
    
    plt.tight_layout()
    plt.savefig(results_dir / "visualizaciones" / "distribucion_clases.png",
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    plt.clf()
    
    return pos_label, class_dist


def build_preprocessor(numeric_features, categorical_features):
    """Construye pipeline de preprocesamiento optimizado."""
    numeric_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    try:
        categorical_transformer = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    except TypeError:
        categorical_transformer = OneHotEncoder(handle_unknown='ignore', sparse=False)
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ],
        remainder='drop',
        verbose_feature_names_out=False
    )
    
    return preprocessor


def calculate_metrics(y_true, y_pred, y_proba, pos_label):
    """Calcula métricas de evaluación de manera eficiente."""
    y_true_binary = (y_true == pos_label).astype(int)
    
    return {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred, pos_label=pos_label, zero_division=0),
        'Recall': recall_score(y_true, y_pred, pos_label=pos_label, zero_division=0),
        'F1-Score': f1_score(y_true, y_pred, pos_label=pos_label, zero_division=0),
        'ROC-AUC': roc_auc_score(y_true_binary, y_proba)
    }


def perform_cross_validation(pipeline, X, y, pos_label, cv):
    """Ejecuta validación cruzada optimizada."""
    scoring_functions = {
        'accuracy': 'accuracy',
        'precision': make_scorer(precision_score, pos_label=pos_label, zero_division=0),
        'recall': make_scorer(recall_score, pos_label=pos_label, zero_division=0),
        'f1': make_scorer(f1_score, pos_label=pos_label, zero_division=0)
    }
    
    cv_results = cross_validate(
        pipeline, X, y, cv=cv, scoring=scoring_functions,
        return_train_score=False, n_jobs=-1
    )
    
    # Procesamiento vectorizado
    results = {}
    for metric in scoring_functions.keys():
        scores = cv_results[f'test_{metric}']
        results.update({
            f'{metric}_mean': scores.mean(),
            f'{metric}_std': scores.std()
        })
    
    return results


def plot_confusion_matrix(y_true, y_pred, pos_label, title, save_path):
    """Genera matriz de confusión optimizada."""
    unique_labels = sorted(y_true.unique())
    neg_label = next(label for label in unique_labels if label != pos_label)
    labels_order = [pos_label, neg_label]
    
    cm = confusion_matrix(y_true, y_pred, labels=labels_order)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=labels_order, yticklabels=labels_order,
                cbar_kws={'label': 'Frecuencia'})
    
    plt.title(title, fontsize=14, fontweight='bold', pad=20)
    plt.ylabel('Valor Real', fontsize=12)
    plt.xlabel('Valor Predicho', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    plt.clf()


def generate_visualizations(y_test, lr_pipeline, rf_pipeline, X_test, pos_label, results_dir):
    """Genera todas las visualizaciones de manera eficiente."""
    # Predicciones una sola vez
    y_pred_lr = lr_pipeline.predict(X_test)
    y_proba_lr = lr_pipeline.predict_proba(X_test)[:, 1]
    y_pred_rf = rf_pipeline.predict(X_test)
    y_proba_rf = rf_pipeline.predict_proba(X_test)[:, 1]
    
    # Matrices de confusión
    plot_confusion_matrix(y_test, y_pred_lr, pos_label,
                         "Matriz de Confusión - Regresión Logística",
                         results_dir / "visualizaciones" / "matriz_confusion_lr.png")
    
    plot_confusion_matrix(y_test, y_pred_rf, pos_label,
                         "Matriz de Confusión - Random Forest",
                         results_dir / "visualizaciones" / "matriz_confusion_rf.png")
    
    # Curvas ROC
    y_test_binary = (y_test == pos_label).astype(int)
    fpr_lr, tpr_lr, _ = roc_curve(y_test_binary, y_proba_lr)
    fpr_rf, tpr_rf, _ = roc_curve(y_test_binary, y_proba_rf)
    auc_lr, auc_rf = auc(fpr_lr, tpr_lr), auc(fpr_rf, tpr_rf)
    
    plt.figure(figsize=(10, 8))
    plt.plot(fpr_lr, tpr_lr, label=f'Regresión Logística (AUC = {auc_lr:.4f})',
             linewidth=2, color='#2E86AB')
    plt.plot(fpr_rf, tpr_rf, label=f'Random Forest (AUC = {auc_rf:.4f})',
             linewidth=2, color='#A23B72')
    plt.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Clasificador Aleatorio')
    
    plt.xlabel('Tasa de Falsos Positivos', fontsize=12)
    plt.ylabel('Tasa de Verdaderos Positivos', fontsize=12)
    plt.title('Curvas ROC - Comparación de Modelos', fontsize=14, fontweight='bold')
    plt.legend(loc='lower right')
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(results_dir / "visualizaciones" / "curvas_roc.png",
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    plt.clf()
    
    # Importancia de variables optimizada
    feature_names = rf_pipeline.named_steps['preprocessor'].get_feature_names_out()
    importances = rf_pipeline.named_steps['classifier'].feature_importances_
    
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values('Importance', ascending=False)
    
    importance_df.to_csv(results_dir / "metricas" / "importancia_variables.csv", index=False)
    
    # Visualización de importancia
    top15 = importance_df.head(15)
    plt.figure(figsize=(14, 10))
    
    y_pos = np.arange(len(top15))
    colors = plt.cm.viridis(np.linspace(0, 1, len(top15)))
    
    plt.barh(y_pos, top15['Importance'], color=colors, alpha=0.8, height=0.7)
    plt.yticks(y_pos, top15['Feature'], fontsize=11)
    plt.gca().invert_yaxis()
    plt.xlabel('Importancia Relativa', fontsize=13, fontweight='bold')
    plt.title('Importancia de Variables - Random Forest\n(Top 15 Variables)', 
              fontsize=16, fontweight='bold', pad=25)
    plt.grid(axis='x', alpha=0.4, linestyle='--', linewidth=0.5)
    plt.gca().set_axisbelow(True)
    
    # Agregar valores
    for i, value in enumerate(top15['Importance']):
        plt.text(value + 0.003, i, f'{value:.3f}', 
                va='center', ha='left', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.subplots_adjust(left=0.35, right=0.95, top=0.9, bottom=0.1)
    plt.savefig(results_dir / "visualizaciones" / "importancia_variables.png",
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    plt.clf()


def main():
    """
    Función principal optimizada para análisis de clasificación binaria.
    Ejecuta pipeline completo de manera eficiente y profesional.
    """
    print("ANÁLISIS DE CLASIFICACIÓN BINARIA - ADULT INCOME DATASET")
    print("=" * 60)
    
    # 1. Configuración inicial
    data_path, results_dir = get_project_paths()
    if data_path is None:
        raise FileNotFoundError("Archivo adult.csv no encontrado")
    
    # 2. Carga y análisis exploratorio
    print("\n[1/8] Carga y análisis exploratorio...")
    df = pd.read_csv(data_path)
    print(f"Dataset cargado: {df.shape[0]} filas x {df.shape[1]} columnas")
    exploratory_analysis(df)
    
    # 3. Limpieza y preprocesamiento
    print("\n[2/8] Limpieza y detección de outliers...")
    df_clean = clean_adult_data(df)
    detect_and_visualize_outliers(df_clean, results_dir)
    df_clean.to_csv(results_dir / "datos" / "adult_clean.csv", index=False)
    print(f"Datos procesados: {df_clean.shape[0]} filas")
    
    # 4. Análisis de variable objetivo
    print("\n[3/8] Análisis de variable objetivo...")
    pos_label, class_dist = analyze_target_variable(df_clean, results_dir)
    
    # 5. Preparación de variables
    print("\n[4/8] Preparación de características...")
    X = df_clean.drop('income', axis=1)
    y = df_clean['income']
    
    numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
    categorical_features = X.select_dtypes(include=['object']).columns.tolist()
    
    print(f"Variables numéricas: {len(numeric_features)}")
    print(f"Variables categóricas: {len(categorical_features)}")
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, stratify=y, random_state=RANDOM_STATE
    )
    print(f"División: {X_train.shape[0]} entrenamiento, {X_test.shape[0]} prueba")
    
    # 6. Construcción y entrenamiento de modelos
    print("\n[5/8] Entrenamiento de modelos...")
    preprocessor = build_preprocessor(numeric_features, categorical_features)
    
    lr_pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(solver='liblinear', max_iter=200, random_state=RANDOM_STATE))
    ])
    
    rf_pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=300, max_depth=10, 
                                            min_samples_split=5, n_jobs=-1, random_state=RANDOM_STATE))
    ])
    
    # Entrenamiento
    lr_pipeline.fit(X_train, y_train)
    rf_pipeline.fit(X_train, y_train)
    
    # Evaluación holdout
    y_pred_lr = lr_pipeline.predict(X_test)
    y_proba_lr = lr_pipeline.predict_proba(X_test)[:, 1]
    y_pred_rf = rf_pipeline.predict(X_test)
    y_proba_rf = rf_pipeline.predict_proba(X_test)[:, 1]
    
    lr_metrics = calculate_metrics(y_test, y_pred_lr, y_proba_lr, pos_label)
    rf_metrics = calculate_metrics(y_test, y_pred_rf, y_proba_rf, pos_label)
    
    print("Resultados Holdout:")
    print(f"  Regresión Logística - F1: {lr_metrics['F1-Score']:.4f}, AUC: {lr_metrics['ROC-AUC']:.4f}")
    print(f"  Random Forest - F1: {rf_metrics['F1-Score']:.4f}, AUC: {rf_metrics['ROC-AUC']:.4f}")
    
    # Guardar métricas holdout
    pd.DataFrame([
        {'Modelo': 'Regresion_Logistica', **lr_metrics},
        {'Modelo': 'Random_Forest', **rf_metrics}
    ]).to_csv(results_dir / "metricas" / "holdout.csv", index=False)
    
    # 7. Validación cruzada
    print("\n[6/8] Validación cruzada...")
    cv = StratifiedKFold(n_splits=CV_FOLDS, shuffle=True, random_state=RANDOM_STATE)
    
    lr_cv = perform_cross_validation(lr_pipeline, X_train, y_train, pos_label, cv)
    rf_cv = perform_cross_validation(rf_pipeline, X_train, y_train, pos_label, cv)
    
    print("Resultados Validación Cruzada:")
    print(f"  Regresión Logística - F1: {lr_cv['f1_mean']:.4f} ± {lr_cv['f1_std']:.4f}")
    print(f"  Random Forest - F1: {rf_cv['f1_mean']:.4f} ± {rf_cv['f1_std']:.4f}")
    
    # Guardar resultados CV
    pd.DataFrame([
        {'Modelo': 'Regresion_Logistica', **lr_cv},
        {'Modelo': 'Random_Forest', **rf_cv}
    ]).to_csv(results_dir / "metricas" / "validacion_cruzada.csv", index=False)
    
    # 8. Visualizaciones y reporte final
    print("\n[7/8] Generación de visualizaciones...")
    generate_visualizations(y_test, lr_pipeline, rf_pipeline, X_test, pos_label, results_dir)
    
    print("\n[8/8] Reporte final...")
    # Comparación final
    comparison_data = [
        {'Modelo': 'Regresión Logística', 'Método': 'Holdout', **lr_metrics},
        {'Modelo': 'Random Forest', 'Método': 'Holdout', **rf_metrics},
        {'Modelo': 'Regresión Logística', 'Método': 'CV', 
         'Accuracy': lr_cv['accuracy_mean'], 'Precision': lr_cv['precision_mean'],
         'Recall': lr_cv['recall_mean'], 'F1-Score': lr_cv['f1_mean'], 'ROC-AUC': 'N/A'},
        {'Modelo': 'Random Forest', 'Método': 'CV',
         'Accuracy': rf_cv['accuracy_mean'], 'Precision': rf_cv['precision_mean'],
         'Recall': rf_cv['recall_mean'], 'F1-Score': rf_cv['f1_mean'], 'ROC-AUC': 'N/A'}
    ]
    
    pd.DataFrame(comparison_data).to_csv(results_dir / "metricas" / "comparacion_modelos.csv", index=False)
    
    # Determinar modelo ganador
    best_f1 = 'Random Forest' if rf_metrics['F1-Score'] > lr_metrics['F1-Score'] else 'Regresión Logística'
    best_auc = 'Random Forest' if rf_metrics['ROC-AUC'] > lr_metrics['ROC-AUC'] else 'Regresión Logística'
    
    print("RESUMEN EJECUTIVO:")
    print(f"  Mejor F1-Score (Holdout): {best_f1}")
    print(f"  Mejor ROC-AUC (Holdout): {best_auc}")
    
    minority_pct = (class_dist.min() / class_dist.sum()) * 100
    print(f"  Desbalance de clases: {minority_pct:.1f}% - {100-minority_pct:.1f}%")
    
    if minority_pct < 40:
        print("  NOTA: Dataset desbalanceado - considerar técnicas de balanceo")
    
    print(f"\nAnálisis completado. Resultados en: {results_dir}")
    print("Archivos generados:")
    print("  - Datos: adult_clean.csv")
    print("  - Métricas: 4 archivos CSV")
    print("  - Visualizaciones: 6 gráficos PNG")


if __name__ == "__main__":
    main()