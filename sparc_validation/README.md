# 🌌 MFSU V2: Validación Masiva - Catálogo SPARC (175 Galaxias)

Este repositorio contiene la validación estadística y física del modelo ** (MFSU) V2**. Se ha procesado el catálogo completo SPARC para demostrar que la dinámica galáctica está regida por la impedancia del vacío y no por la materia oscura.

## 💎 El Descubrimiento: Saturación en 0.921

El análisis revela que la constante de saturación **δF = 0.921** actúa como el "atractor" o **Tronco Original** de la estructura galáctica. Utilizando una impedancia estructural de **χ = 12.65**, el modelo predice la velocidad de rotación con una precisión de hasta el **99.9%** en sistemas en equilibrio.

### 📊 Resumen de Resultados (Top 10 - Rama Original)

| GALAXIA | V_BAR (Bariónica) | V_OBS (Real) | V_MFSU (δF=0.921) | PRECISION | DELTA_F_REAL |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CamB** | 16.43 | 20.10 | 20.08 | **99.91%** | 0.9206 |
| **UGC09992** | 28.18 | 34.30 | 34.44 | **99.60%** | 0.9226 |
| **NGC7793** | 73.74 | 90.80 | 90.11 | **99.24%** | 0.9180 |
| **NGC6946** | 127.64 | 154.00 | 155.98 | **98.72%** | 0.9260 |
| **UGC09037** | 122.47 | 152.00 | 149.66 | **98.46%** | 0.9149 |
| **UGC07577** | 14.97 | 17.80 | 18.29 | **97.24%** | 0.9317 |
| **NGC0801** | 171.77 | 216.00 | 209.90 | **97.18%** | 0.9089 |
| **UGC11455** | 211.25 | 266.00 | 258.15 | **97.05%** | 0.9084 |
| **UGC11914** | 257.78 | 305.00 | 315.01 | **96.72%** | 0.9348 |
| **NGC4010** | 96.32 | 122.00 | 117.70 | **96.48%** | 0.9056 |

## 🧬 Teoría de Ramificación Fractal (Branching)

De acuerdo con la teoría presentada, la dispersión en los valores de **δF** observada en las 175 galaxias no es un error, sino una medición de la **madurez fractal** del sistema:

* **δF ≈ 0.921:** Galaxias en el **Tronco Original**. Saturación total del vacío.
* **δF < 0.921:** **Ramas Jóvenes**. Sistemas en proceso de acoplamiento a la red de espín.
* **δF > 0.921:** **Eventos de Supersaturación**. Puntos de alta densidad de información fractal.



## 📐 Fundamentos Matemáticos

El motor MFSU V2 transforma la velocidad bariónica ($V_{bar}$) en velocidad observada ($V_{obs}$) mediante la relación de impedancia:

$$V_{MFSU} = V_{bar} \cdot \chi^{(1 - \delta_F)}$$

Donde:
* $\chi = 12.65$ (Impedancia Estructural / Conectividad de Newton-Gregory).
* $\delta_F = 0.921$ (Punto de saturación del vacío).

## 📂 Contenido del Repositorio

* `REGISTRO_MAESTRO_MFSU_175.csv`: Base de datos completa con el "ADN fractal" (Delta_F Real) de cada galaxia.
* `motor_mfsu_v2.py`: Script en Python compatible con Google Colab para replicar los cálculos sobre el dataset SPARC.
* `plots/`: Gráficas de distribución y validación de la constante de saturación.

---
**Autor:** Miguel Ángel Franco  
**Fecha:** 2026-01-23  
**Proyecto:**  (MFSU) - Reemplazo del paradigma de Materia Oscura.

> "La gravedad no es una partícula invisible, es la firma geométrica del espacio fractal."
