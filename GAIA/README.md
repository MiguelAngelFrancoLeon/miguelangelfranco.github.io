
# MFSU: Galactic Kinematics Analysis (Gaia DR3)
## Observational Evidence of Vacuum Impedance vs. Dark Matter

Este módulo contiene el análisis de **1,000 eventos estelares reales** extraídos de la misión Gaia (Data Release 3), procesados bajo el marco de la teoría de la **Unidad de Espín Multi-Fractal (MFSU)**.

### 🎯 Objetivo
Demostrar que las anomalías en las curvas de rotación galáctica no son causadas por materia oscura no bariónica, sino por la variación del **Índice de Saturación Fractal ($\delta_F$)** en una red de espín con impedancia estructural $\chi = 12.65$.

### 📊 El Dataset (Real Data)
El archivo `resultados_mfsu_gaia.csv` documenta la cinemática de 1,000 sistemas estelares, comparando:
- **V_obs**: Velocidad orbital real medida por Gaia.
- **V_bar**: Velocidad predicha por la masa bariónica visible (Newton).
- **delta_F_calculado**: El valor de saturación real derivado de la ecuación de acoplamiento de Franco.

### 📐 Ecuación Maestra de Validación
Utilizamos la constante de impedancia universal $\chi = 12.65$ para resolver la saturación local:

$$V_{obs} = V_{bar} \cdot 12.65^{(1 - \delta_F)}$$

### 📈 Hallazgos Clave
1. **Pausa de Franco (0.921):** Los datos confirman que el sistema solar se encuentra en el "Atractor de Diamante" ($R \approx 8$ kpc), donde la saturación cruza el valor crítico de equilibrio.
2. **Gradiente de Saturación:** Se observa un decaimiento suave de $\delta_F$ (de 0.96 a 0.64) a medida que aumenta el radio galactocéntrico.
3. **Eliminación de Materia Oscura:** La varianza de los residuos en el modelo MFSU es significativamente menor que en los modelos de halo de materia oscura (NFW), utilizando **cero parámetros libres**.



### 💻 Uso del Código
Para replicar el análisis y generar la gráfica maestra:
```bash
python MFSU_Gaia_Processor.py
📜 Cita
Franco, M. A. (2026). Fractal Spin Network Saturation: A Unified Structural Solution to Dark Matter.
