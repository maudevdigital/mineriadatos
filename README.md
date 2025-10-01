# # Análisis de Clasificación Binaria - Adult Income Dataset

## Descripción del Proyecto

Este proyecto implementa un análisis completo de clasificación binaria utilizando el **Adult Income Dataset** del UCI Machine Learning Repository. El objetivo es predecir si una persona gana más de $50K anuales basándose en características demográficas y laborales.

## Estructura del Proyecto

```
mineriadatos/
├── data/
│   └── adult.csv                    # Dataset original
├── src/
│   └── main.py                      # Código principal optimizado
├── results/
│   ├── datos/
│   │   └── adult_clean.csv          # Datos preprocesados
│   ├── metricas/
│   │   ├── holdout.csv              # Métricas holdout validation
│   │   ├── validacion_cruzada.csv   # Métricas cross-validation
│   │   ├── comparacion_modelos.csv  # Comparación completa
│   │   └── importancia_variables.csv # Importancia de características
│   └── visualizaciones/
│       ├── distribucion_clases.png   # Distribución variable objetivo
│       ├── boxplots_outliers.png     # Detección de outliers
│       ├── matriz_confusion_lr.png   # Matriz confusión - Regresión Logística
│       ├── matriz_confusion_rf.png   # Matriz confusión - Random Forest
│       ├── curvas_roc.png           # Comparación curvas ROC
│       └── importancia_variables.png # Top 15 variables más importantes
└── README.md
```

## Dataset

- **Fuente**: UCI Machine Learning Repository
- **Tamaño**: 32,561 registros con 15 variables
- **Objetivo**: Clasificación binaria (≤50K vs >50K)
- **Variables**: 6 numéricas, 9 categóricas

### Variables Principales
- **Demográficas**: age, race, sex, native-country
- **Educación**: education, education-num
- **Laborales**: workclass, occupation, hours-per-week
- **Económicas**: capital-gain, capital-loss
- **Familiares**: marital-status, relationship

## Metodología

### 1. Preprocesamiento
- Limpieza de valores faltantes (representados como "?")
- Detección de outliers mediante método IQR
- Codificación de variables categóricas (One-Hot Encoding)
- Escalado de variables numéricas (StandardScaler)

### 2. Modelos Implementados
- **Regresión Logística**: Modelo lineal interpretable
- **Random Forest**: Modelo ensemble no paramétrico

### 3. Evaluación
- **Holdout Validation**: División 80/20
- **Cross-Validation**: 5-fold estratificado
- **Métricas**: Accuracy, Precision, Recall, F1-Score, ROC-AUC

## Resultados Principales

### Rendimiento de Modelos

| Modelo | F1-Score | ROC-AUC | Precisión | Recall |
|--------|----------|---------|-----------|--------|
| **Regresión Logística** | **66.85%** | 90.43% | 73.82% | 60.08% |
| Random Forest | 64.31% | **90.74%** | 79.59% | 54.46% |

### Hallazgos Clave
- **Modelo Ganador**: Regresión Logística (mejor F1-Score)
- **Variables Más Importantes**: capital-gain, marital-status, education-num
- **Desbalance de Clases**: 75.9% vs 24.1%
- **Outliers**: 27.7% en hours-per-week

## Instalación y Uso

### Requisitos
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### Ejecución
```bash
python src/main.py
```

El script ejecutará automáticamente:
1. Carga y análisis exploratorio
2. Limpieza y preprocesamiento
3. Entrenamiento de modelos
4. Evaluación completa
5. Generación de visualizaciones

## Características del Código

- **Código Profesional**: Sin elementos decorativos, documentado
- **Optimizado**: Procesamiento vectorizado y paralelo
- **Modular**: Funciones especializadas y reutilizables
- **Robusto**: Manejo de errores y configuración automática
- **Completo**: Cumple todos los requisitos académicos

## Visualizaciones Generadas

1. **Distribución de Clases**: Análisis del desbalance
2. **Boxplots de Outliers**: Detección de valores atípicos
3. **Matrices de Confusión**: Para ambos modelos
4. **Curvas ROC**: Comparación de rendimiento
5. **Importancia de Variables**: Top 15 características

## Conclusiones

- La **Regresión Logística** mostró el mejor balance entre precisión y recall
- Las variables económicas y familiares son los predictores más importantes
- El dataset presenta desbalance significativo que requiere atención en producción
- Ambos modelos logran un rendimiento superior al 85% en accuracy

## Recomendaciones

1. **Para Producción**: Implementar técnicas de balanceo (SMOTE, undersampling)
2. **Feature Engineering**: Crear interacciones entre variables
3. **Monitoreo**: Evaluar sesgos en variables protegidas
4. **Validación Externa**: Probar con datos más recientes

---

**Autor**: [Tu Nombre]  
**Curso**: Minería de Datos  
**Fecha**: Octubre 2025  
**Institución**: [Tu Universidad]