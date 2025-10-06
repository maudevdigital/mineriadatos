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
│   ├── generar_documentos.py        # Generador de todos los documentos
│   └── generar_informe.py           # Generador específico del informe
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
│   ├── Informe_Grupal_Solemne_I.docx   # 📄 INFORME OFICIAL (máx. 3 págs)
│   ├── Respuestas_Solemne_I.docx       # Respuestas detalladas 20 preguntas
│   └── Prompt_Presentacion_PPT.docx    # Prompt para generar PPT con IA
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

El proyecto incluye **documentación completa** para la Solemne I según el enunciado del profesor Diego Robles C.:

### 1. 📄 Informe_Grupal_Solemne_I.docx (ENTREGABLE OFICIAL)
**Informe grupal de máximo 3 páginas** que cumple con todos los requisitos:
- ✅ Introducción y metodología
- ✅ Resultados y comparación de modelos
- ✅ Análisis de variables y visualización
- ✅ Comparación crítica y escalabilidad
- ✅ Consideraciones éticas y recomendaciones
- ✅ Conclusiones con respuestas a las 20 preguntas integradas
- **Formato**: Profesional, conciso, listo para entregar

### 2. 📚 Respuestas_Solemne_I.docx (MATERIAL DE APOYO)
Documento extenso con respuestas **detalladas** a las 20 preguntas de evaluación:
- **I. Análisis y Preprocesamiento** (Q1-3)
- **II. Modelos y Rendimiento** (Q4-7)
- **III. Validación Cruzada** (Q8-10)
- **IV. Visualización y Explicación** (Q11-13)
- **V. Comparación Crítica** (Q14-16)
- **VI. Ética y Aplicación Real** (Q17-20)
- **Uso**: Estudio, preparación de presentación oral, consulta

### 3. 🎤 Prompt_Presentacion_PPT.docx (PRESENTACIÓN ORAL)
Prompt optimizado para generar presentación de **15 minutos**:
- Estructura de 15 diapositivas completas
- Todos los datos, tablas y métricas incluidas
- Instrucciones de diseño visual profesional
- Compatible con: **Gamma.app** ⭐, Tome.app, Beautiful.AI
- **Uso**: Copiar prompt → Pegar en plataforma IA → PPT automático

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

# Generar TODOS los documentos de evaluación
python src/generar_documentos.py
```

Esto creará **3 documentos** en `results/`:
1. **Informe_Grupal_Solemne_I.docx**: Informe oficial de máx. 3 páginas ✅ ENTREGAR
2. **Respuestas_Solemne_I.docx**: Respuestas detalladas a las 20 preguntas (apoyo)
3. **Prompt_Presentacion_PPT.docx**: Prompt para generar PPT con IA (Gamma.app)

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

## 📋 Checklist de Entregables Solemne I

### ✅ Entregables Completados:

- [x] **Informe Grupal** (máx. 3 páginas) → `Informe_Grupal_Solemne_I.docx`
- [x] **Presentación Oral** (15 minutos) → `Prompt_Presentacion_PPT.docx` (generar PPT)
- [x] Análisis exploratorio y preprocesamiento
- [x] Implementación correcta de 2 modelos (LR + RF)
- [x] Evaluación con validación cruzada (5-fold)
- [x] Comparación y justificación de resultados
- [x] Visualizaciones (6 gráficos generados)
- [x] Respuestas a las 20 preguntas del enunciado

### 📝 Criterios de Evaluación Cubiertos:

**Evaluación Grupal (70 pts):**
- ✅ Análisis exploratorio y preprocesamiento (10 pts)
- ✅ Implementación correcta de modelos (15 pts)
- ✅ Evaluación con validación cruzada (15 pts)
- ✅ Comparación y justificación de resultados (10 pts)
- ✅ Visualizaciones y calidad del informe (10 pts)
- ⏳ Claridad en la exposición oral (10 pts) - *Preparar con material generado*

**Evaluación Individual (30 pts):**
- ⏳ Participación activa en presentación (10 pts)
- ⏳ Argumentación técnica (10 pts)
- ⏳ Dominio del flujo metodológico aplicado (10 pts)

---

**Grupo 4 - Minería de Datos**
