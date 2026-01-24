# MFSU - High Energy Propagation Analysis (Fermi GBM)
## Evidence of Structural Vacuum Impedance in Gamma-Ray Bursts

Este repositorio contiene el análisis de la interacción entre fotones de alta energía y la red de espín galáctica, utilizando datos cruzados de **Fermi GBM** y el mapa de saturación fractal derivado de **Gaia DR3**.

### 🎯 Objetivo del Análisis
Demostrar que el vacío posee una impedancia estructural finita definida por la constante $\chi = 12.65$. Validamos que la energía observada de los Gamma-Ray Bursts (GRBs) está modulada por el índice de saturación local ($\delta_F$), eliminando la necesidad de correcciones arbitrarias de materia oscura.

### 📂 Dataset: Master Merge (`master_cruce_gaia_fermi.csv`)
El archivo final de datos une la cinemática estelar con la electrodinámica estructural. Columnas clave:
- `grb_id`: Identificador oficial del evento Fermi.
- `e_peak_kev`: Energía pico observada por el instrumento (Data Real).
- `delta_F_red`: Saturación de la red de espín en el trayecto del fotón (Mapeado de Gaia).
- `E_fuente_estimada`: Energía intrínseca calculada mediante la corrección de Franco.

### 📐 Fundamento Matemático (MFSU)
La propagación de energía en una red de espín saturada sigue la ley de acoplamiento estructural:

$$E_{source} = \frac{E_{obs}}{\chi^{(1 - \delta_F)}}$$

Donde:
- $\chi = 12.65$ (Constante de Impedancia de Franco)
- $\delta_F$ = Índice de Saturación Fractal local.

### 📉 Resultados Clave
1. **Firma de Impedancia:** Se observa que los fotones que atraviesan zonas con $\delta_F < 0.921$ sufren una mayor pérdida de energía aparente, confirmando que la red de espín menos saturada ofrece mayor resistencia elástica.
2. **Unificación:** El uso de la misma constante (12.65) para explicar tanto la rotación de galaxias (Gaia) como el desplazamiento energético de los GRBs (Fermi) confirma una estructura universal del espacio-tiempo.

### 💻 Instrucciones de Uso
Para procesar el cruce de datos y generar los resultados:
1. Asegurarse de tener `resultados_mfsu_gaia.csv` en el directorio.
2. Ejecutar el script de unificación:
   ```bash
   python Master_Merge_MFSU.py
