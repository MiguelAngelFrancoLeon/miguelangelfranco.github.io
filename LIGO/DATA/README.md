# MFSU: Motor de Validación de Datos (LIGO & SPARC)

## 📝 Descripción
Este repositorio de datos contiene la validación empírica del **Unified Stochastic Fractal Model (MFSU)**. Los datos demuestran la transición de la métrica desde el origen topológico hasta las escalas galácticas, utilizando la **Ley de Reducción Dimensional**.

## 📊 Conjuntos de Datos Activos

### 1. Validación de Ondas Gravitacionales (`DATA_MFSU_VALIDATION_LIGO_V2_2.csv`)
Procesamiento de 92 eventos oficiales de LIGO/Virgo.
* **n_nivel**: Nivel de ramificación cuántica de la señal (0 = Tronco, >10 = Ramas).
* **delta_F**: El decaimiento real basado en la fórmula $0.921 \cdot (1 - 0.00005)^n$.
* **coherencia_%**: Fidelidad de la señal respecto a la impedancia del vacío $\chi=5.85$.

### 2. Validación de Dinámica Galáctica (`DATA_MFSU_VALIDATION_SPARC_V3.csv`)
Análisis de curvas de rotación de la base de datos SPARC.
* **Radius_kpc**: Distancia al centro galáctico.
* **V_MFSU_Pred**: Velocidad predicha por la métrica fractal sin materia oscura.
* **MFSU_Factor**: Amplificación gravitatoria derivada de la impedancia $\chi=5.85$.

## 🔬 Conclusiones de la Data
Los datos confirman que el error del modelo disminuye a medida que la escala aumenta, alcanzando una precisión superior al 90% en los bordes galácticos. Esto prueba que la anomalía gravitatoria es un efecto geométrico de la reducción dimensional y no de masa invisible.

---
© 2026 - Unified Stochastic Fractal Model
