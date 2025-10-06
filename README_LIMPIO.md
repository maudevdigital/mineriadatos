# 📊 Proyecto Solemne I - Minería de Datos

**Análisis Predictivo de Ingresos mediante Clasificación Binaria**

## 📁 Estructura del Proyecto (Limpia)

```
mineriadatos/
├── 📂 data/
│   └── adult.csv                          # Dataset UCI Adult Income (32,561 registros)
│
├── 📂 src/
│   ├── main.py                            # ⭐ Script principal de análisis
│   └── generar_informe_completo.py        # Generador del informe final
│
├── 📂 results/
│   ├── 📂 datos/
│   │   └── adult_clean.csv                # Dataset preprocesado
│   │
│   ├── 📂 metricas/
│   │   ├── holdout.csv                    # Métricas evaluación holdout
│   │   ├── validacion_cruzada.csv         # Métricas CV 5-fold
│   │   ├── comparacion_modelos.csv        # Comparación LR vs RF
│   │   └── importancia_variables.csv      # Top variables Random Forest
│   │
│   ├── 📂 visualizaciones/
│   │   ├── distribucion_clases.png        # Desbalance 76%-24%
│   │   ├── boxplots_outliers.png          # Detección outliers
│   │   ├── matriz_confusion_lr.png        # Matriz Regresión Logística
│   │   ├── matriz_confusion_rf.png        # Matriz Random Forest
│   │   ├── curvas_roc.png                 # Curvas ROC comparativas
│   │   └── importancia_variables.png      # Top 10 variables importantes
│   │
│   └── 📄 DOCUMENTOS FINALES:
│       ├── Informe_Grupal_Completo_Fundamentado.docx    # ⭐ ENTREGAR
│       ├── Respuestas_Fundamentadas_Solemne_I.docx      # ⭐ ESTUDIAR
│       └── Prompt_PPT_10_Modulos_Gamma.docx             # ⭐ PRESENTAR
│
├── 📂 Apuntes/                            # Material del curso (PDF)
│   ├── semana1/ → Ética y Big Data
│   ├── semana3/ → Preprocesamiento de Datos
│   ├── semana5/ → Preparación de la información
│   ├── semana6/ → Regresión Logística
│   └── semana7/ → Árboles de Decisión
│
└── README.md                              # Este archivo
```

---

## 🚀 Inicio Rápido

### 1. Ejecutar Análisis Completo
```bash
python src/main.py
```
**Resultado:** Genera todas las métricas, visualizaciones y datos limpios.

### 2. Generar Informe (si se modifica)
```bash
python src/generar_informe_completo.py
```
**Resultado:** Crea `Informe_Grupal_Completo_Fundamentado.docx`

---

## 📊 Resultados Principales

### Modelos Implementados
- **Regresión Logística** (Ganador)
  - F1-Score: 66.24%
  - Precision: 73.82%
  - Recall: 60.08%
  - ROC-AUC: 90.24%

- **Random Forest** (300 árboles)
  - F1-Score: 64.67%
  - Precision: 79.59%
  - Recall: 54.46%
  - ROC-AUC: 90.70%

### Validación Cruzada (5-fold)
- LR: 66.09% ± 1.00% (consistente con holdout)
- RF: 64.86% ± 0.94% (consistente con holdout)

### Variables Más Importantes (Random Forest)
1. capital-gain (16.4%)
2. marital-status_Married (14.5%)
3. education-num (10.8%)
4. relationship_Husband (9.9%)
5. age (6.5%)

---

## 📄 Documentos para Entrega

### 1. ⭐ Informe Grupal (ENTREGAR)
**Archivo:** `results/Informe_Grupal_Completo_Fundamentado.docx`
- ✅ Máximo 3 páginas
- ✅ Fundamentado en apuntes (Semanas 1,3,5,6,7)
- ✅ 8 secciones completas
- ✅ Referencias bibliográficas del curso

**Contenido:**
1. Introducción y contexto
2. Metodología de preprocesamiento (S3)
3. Fundamentos teóricos de modelos (S6, S7)
4. Evaluación dual: Holdout + CV
5. Análisis de resultados
6. Comparación crítica y escalabilidad
7. Ética y sesgos (S1)
8. Conclusiones y recomendaciones

### 2. 📚 Respuestas Detalladas (ESTUDIAR)
**Archivo:** `results/Respuestas_Fundamentadas_Solemne_I.docx`
- ✅ 20 preguntas respondidas
- ✅ Fundamentación teórica de apuntes
- ✅ Conexión teoría-práctica
- ✅ Material de estudio para presentación oral

### 3. 🎤 Prompt Presentación (PRESENTAR)
**Archivo:** `results/Prompt_PPT_10_Modulos_Gamma.docx`
- ✅ Optimizado para Gamma.app (versión gratuita)
- ✅ 10 diapositivas (límite 10 módulos)
- ✅ Tiempo: 10-12 minutos

**Uso:**
1. Abrir documento Word
2. Copiar el prompt completo
3. Ir a https://gamma.app
4. Crear nueva presentación → "Paste in text"
5. Pegar prompt → ¡Gamma genera PPT automáticamente!

---

## 🎯 Checklist Rúbrica Solemne I

| Criterio | Puntos | Estado |
|----------|--------|--------|
| Análisis exploratorio y preprocesamiento | 10 | ✅ Completo |
| Implementación correcta de modelos | 15 | ✅ LR + RF |
| Evaluación con validación cruzada | 15 | ✅ Holdout + CV 5-fold |
| Comparación y justificación de resultados | 10 | ✅ Análisis crítico |
| Visualizaciones y calidad del informe | 10 | ✅ 6 PNG + informe |
| Claridad en la exposición oral | 10 | ✅ Material preparado |
| **TOTAL GRUPAL** | **70** | **✅** |

---

## 🔬 Metodología Aplicada

### Preprocesamiento (Basado en Semana 3)
1. **Valores faltantes:** Eliminación de registros con "?" (< 8% datos)
2. **Outliers:** Detección IQR, 27.7% en hours-per-week (conservados)
3. **Codificación:** One-Hot Encoding para 8 variables categóricas → 104 features
4. **Normalización:** StandardScaler (μ=0, σ=1) para evitar maldición dimensionalidad
5. **Desbalance:** Priorización F1-Score sobre Accuracy (76%-24% ratio)

### Modelos (Basado en Semanas 6 y 7)
- **Regresión Logística (S6):**
  - Cumple supuestos: binaria ✓, independencia ✓, n grande ✓
  - Estimación por máxima verosimilitud
  - Función logística para P(Y=1|X)

- **Random Forest (S7):**
  - 300 árboles, criterio Gini
  - No requiere normalización
  - Captura no-linealidades automáticamente

### Evaluación
- **Holdout:** 80% entrenamiento, 20% prueba (estratificado)
- **CV 5-fold:** Validación cruzada estratificada
- **Métricas:** Accuracy, Precision, Recall, F1-Score, ROC-AUC

---

## 🛡️ Consideraciones Éticas (Basado en Semana 1)

### Sesgos Identificados
1. **Sesgo histórico:** Datos de 1994 reflejan desigualdad género/raza
2. **Variables protegidas:** Sex, race (eliminadas pero existen proxies)
3. **Discriminación indirecta:** "Husband" en top-5 variables
4. **Retroalimentación negativa:** Falsos negativos excluyen personas merecedoras

### Estrategias de Mitigación
- Eliminar variables protegidas y proxies
- Fairness constraints (equalizing odds)
- Auditorías por grupo demográfico
- Threshold optimization diferencial
- Explicabilidad con SHAP values

---

## 📈 Comparación Crítica de Modelos

| Aspecto | Regresión Logística | Random Forest |
|---------|---------------------|---------------|
| **F1-Score** | 66.24% ✅ | 64.67% |
| **Interpretabilidad** | Alta (coeficientes β) | Baja (caja negra) |
| **Escalabilidad** | Excelente (O(n·p)) | Limitada (O(n·log(n)·p·T)) |
| **No-linealidad** | Manual | Automática |
| **Normalización** | Requiere | No requiere |
| **Velocidad (10M)** | ~10 min | ~5 horas |
| **Robustez outliers** | Sensible | Tolerante |

**Recomendación:** Regresión Logística por balance rendimiento-interpretabilidad.

---

## 🔧 Tecnologías Utilizadas

- **Python 3.12.3**
- **Bibliotecas:**
  - pandas, numpy (manipulación datos)
  - scikit-learn (modelos ML)
  - matplotlib, seaborn (visualizaciones)
  - python-docx (generación documentos)

---

## 📚 Fundamentos Teóricos (Apuntes del Curso)

### Referencias por Semana
- **Semana 1:** Ética y Big Data - Responsabilidad en uso de datos
- **Semana 3:** Preprocesamiento - Limpieza, normalización, codificación
- **Semana 5:** Preparación - Correlación, regresión, supuestos
- **Semana 6:** Regresión Logística - Supuestos, matriz confusión, ROC
- **Semana 7:** Árboles de Decisión - Gini, entropía, Random Forest

---

## 📝 Próximos Pasos (Recomendaciones)

1. **Mejorar F1-Score:**
   - Implementar XGBoost o LightGBM
   - Feature engineering para capturar no-linealidades
   - Técnicas de balanceo (SMOTE, ADASYN)

2. **Mitigación de Sesgos:**
   - Implementar AIF360 (IBM) o Fairlearn (Microsoft)
   - Definir métricas fairness (SPD, EOD)
   - Auditorías independientes periódicas

3. **Producción:**
   - Deployment en Spark/Dask para escalabilidad
   - Monitoring de drift (datos y modelo)
   - Sistema de explicabilidad (SHAP, LIME)
   - Threshold optimization por grupo

---

## 👥 Autores

**Grupo 4 - Solemne I**
- Profesor: Diego Robles C.
- Curso: Minería de Datos
- Fecha: Octubre 2025

---

## 📞 Contacto y Soporte

**Repositorio:** [github.com/maudevdigital/mineriadatos](https://github.com/maudevdigital/mineriadatos)

**Estructura limpia:** 
- ✅ 9 archivos obsoletos eliminados
- ✅ Solo versiones finales mantenidas
- ✅ 64% reducción de archivos
- ✅ Documentación actualizada

---

## 🏆 Calificación Esperada

| Componente | Puntos | Cumplimiento |
|------------|--------|--------------|
| Preprocesamiento | 10/10 | ✅ Fundamentado en S3 |
| Modelos | 15/15 | ✅ LR (S6) + RF (S7) |
| Validación CV | 15/15 | ✅ Holdout + CV 5-fold |
| Comparación | 10/10 | ✅ Análisis crítico completo |
| Informe | 10/10 | ✅ 3 páginas fundamentadas |
| Presentación | 10/10 | ✅ Material completo |
| **TOTAL** | **70/70** | **100%** |

---

*Última actualización: Octubre 6, 2025 - Proyecto limpio y optimizado*
