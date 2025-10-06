# Análisis de Clasificación Binaria - Adult Income Dataset

## Descripción del Proyecto

Este proyecto implementa un análisis completo de clasificación binaria utilizando el **Adult Income Dataset** del UCI Machine Learning Repository. El objetivo es predecir si una persona gana más de $50K anuales basándose en características demográficas y laborales.

## 📂 Estructura del Proyecto

```
mineriadatos/
├── data/
│   └── adult.csv                    # Dataset original UCI
├── src/
│   ├── main.py                      # Script principal de análisis
│   └── generar_documentos.py        # Generador de documentos Word
├── results/
│   ├── datos/
│   │   └── adult_clean.csv         # Dataset limpio y preprocesado
│   ├── metricas/
│   │   ├── holdout.csv             # Resultados evaluación holdout
│   │   ├── validacion_cruzada.csv  # Resultados CV 5-fold
│   │   ├── comparacion_modelos.csv # Comparativa entre modelos
│   │   └── importancia_variables.csv # Feature importance
│   ├── visualizaciones/
│   │   ├── distribucion_clases.png
│   │   ├── boxplot_age.png
│   │   ├── boxplot_hours.png
│   │   ├── matriz_confusion_lr.png
│   │   ├── matriz_confusion_rf.png
│   │   ├── curvas_roc.png
│   │   └── importancia_variables.png
│   ├── Respuestas_Solemne_I.docx   # Respuestas a las 20 preguntas
│   └── Prompt_Presentacion_PPT.docx # Prompt para generar PPT con IA
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

## 📊 Resultados Principales

### Comparativa de Modelos

| Modelo | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|----------|-----------|--------|----------|---------|
| **Regresión Logística** | 85.26% | 73.82% | 60.08% | **66.24%** | 90.24% |
| **Random Forest** | 85.67% | 79.59% | 54.46% | 64.67% | **90.70%** |

**Modelo ganador**: Regresión Logística (mejor F1-Score y balance precision-recall)

### Validación Cruzada (5-fold stratified)

- **Regresión Logística**: F1 = 66.09% ± 1.00%
- **Random Forest**: F1 = 64.86% ± 0.94%

La consistencia con los resultados holdout confirma la robustez de los modelos.

### Variables Más Importantes (Random Forest)

1. **capital-gain** (16.43%) - Ganancias de capital
2. **marital-status_Married-civ-spouse** (14.45%) - Estado civil casado
3. **education-num** (10.77%) - Años de educación
4. **relationship_Husband** (9.93%) - Rol familiar
5. **age** (6.46%) - Edad

## 📝 Documentación de Evaluación

El proyecto incluye documentación completa para la evaluación Solemne I:

### 1. Respuestas_Solemne_I.docx
Documento Word con respuestas detalladas a las 20 preguntas de evaluación, organizadas en 6 secciones:
- **I. Análisis y Preprocesamiento** (Q1-3)
- **II. Modelos y Rendimiento** (Q4-7)
- **III. Validación Cruzada** (Q8-10)
- **IV. Visualización y Explicación** (Q11-13)
- **V. Comparación Crítica** (Q14-16)
- **VI. Ética y Aplicación Real** (Q17-20)

### 2. Prompt_Presentacion_PPT.docx
Prompt optimizado para generar presentación profesional usando plataformas de IA:
- Estructura de 15 diapositivas completas
- Instrucciones de diseño visual
- Compatible con Gamma.app, Tome.app, Beautiful.AI
- Incluye todos los hallazgos clave del análisis

## 🚀 Uso

### Ejecución del Análisis Principal

```bash
# Instalar dependencias
pip install numpy pandas matplotlib seaborn scikit-learn

# Ejecutar análisis completo
python src/main.py
```

El script generará automáticamente:
- Dataset limpio en `results/datos/`
- Métricas de evaluación en `results/metricas/`
- Visualizaciones en `results/visualizaciones/`

### Generación de Documentos Word

```bash
# Instalar librería adicional
pip install python-docx

# Generar documentos de evaluación
python src/generar_documentos.py
```

Esto creará:
- **Respuestas_Solemne_I.docx**: Documento con respuestas completas a las 20 preguntas de evaluación
- **Prompt_Presentacion_PPT.docx**: Prompt optimizado para generar presentación PPT con IA (Gamma, Tome, Beautiful.AI)

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

**Grupo 4 - Minería de Datos**
