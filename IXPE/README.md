# MFSU: IXPE X-Ray Polarization & Dimensional Reduction Mapping

## 📝 Descripción
Este módulo del repositorio aplica el **Unified Stochastic Fractal Model (MFSU)** a los datos de polarización de rayos X obtenidos por la misión **IXPE (Imaging X-ray Polarimetry Explorer)** de la NASA. El objetivo es identificar la huella del déficit fractal **0.921** y la impedancia del vacío en la organización de los campos de alta energía.

## 🔭 Tesis de Polarización Fractal
A diferencia de los modelos cinéticos estándar, la MFSU postula que la polarización en restos de supernovas (SNR) y púlsares es una manifestación directa de la **Birefringencia del Vacío Fractal**. La radiación no se propaga por un espacio liso, sino a través de una red con impedancia métrica **$\chi = 5.85$**.

### Constantes de Aplicación y Ley de Reducción:
* **0.921 (Semilla Topológica):** El valor de máxima coherencia donde el ángulo de polarización está alineada con la geometría original del vacío.
* **Ley de Reducción de Franco:** A medida que los fotones atraviesan el medio fractal, el grado de polarización ($PD$) experimenta una ramificación nivelada:
  $$\delta_F(n) = 0.921 \cdot (1 - 0.00005)^n$$
  Donde **$n$** representa el nivel de ramificación espacial entre la fuente y el observador.



## 📊 Variables de Análisis
El dataset procesado en esta carpeta (`DATA_MFSU_VALIDATION_IXPE_V1.csv`) incluye:
* **Source:** Identificador de la fuente de alta energía (ej. Crab Nebula, Cassiopeia A).
* **Energy (keV):** Nivel energético. A mayor energía, mayor proximidad a la vibración de la semilla 0.921.
* **n_nivel:** Nivel de ramificación fractal detectado en la señal de rayos X.
* **delta_F:** Valor fractal resultante que define el linaje de coherencia magnética.

## 🔬 Conclusión Científica
La alineación observada por IXPE confirma que el vacío posee una estructura porosa. La constante **5.85** actúa como el regulador de flujo que previene la dispersión total de la polarización, manteniendo la firma de la semilla original incluso en ambientes de extrema gravedad.

---
**Propiedad Intelectual:** Miguel Ángel Franco León (2026) 
*Unified Stochastic Fractal Model (MFSU)*
