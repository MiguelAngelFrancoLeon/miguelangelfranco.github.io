# MFSU: GAIA Stellar Kinematics & Fractal Vorticity

## 📝 Descripción
Este módulo aplica el **Unified Stochastic Fractal Model (MFSU)** a los datos de astrometría de precisión de la misión **Gaia (ESA)**. Analizamos las anomalías en las velocidades residuales de las estrellas en el disco galáctico.

## 🔭 Tesis del Movimiento Fractal
La MFSU postula que el movimiento estelar no ocurre en un espacio vacío, sino en un flujo organizado por la **Métrica 5.85**. Las desviaciones en las velocidades (proper motions) son el resultado de la interacción entre la masa bariónica y la vorticidad del vacío fractal.

### Ecuación de Ajuste Gaia-MFSU:
Las estrellas experimentan una aceleración adicional $a_{mfsu}$ dependiente de la semilla 0.921:
$$a_{mfsu} = a_{newton} \cdot \left( \frac{\delta_F}{\chi} \right)^{-1}$$



## 📊 Variables de Análisis (`DATA_MFSU_VALIDATION_GAIA_V1.csv`)
* **Source_ID:** Identificador único de Gaia DR3.
* **Parallax:** Distancia precisa para determinar el nivel de ramificación $n$.
* **Radial_Velocity:** Velocidad medida vs. Velocidad predicha por MFSU.
* **Fractal_Vorticity:** El grado de torsión del espacio-tiempo en esa región.

---
**Propiedad Intelectual:** Miguel Ángel Franco León (2026)
