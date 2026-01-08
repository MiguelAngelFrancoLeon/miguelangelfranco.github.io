# MFSU: LIGO Gravitational Wave Fractal Dataset

## 📝 Descripción
Este conjunto de datos contiene la clasificación fractal de eventos de ondas gravitacionales (GW) detectados por la colaboración LIGO/Virgo/KAGRA, procesados bajo el **Unified Stochastic Fractal Model (MFSU)** de Miguel Ángel Franco León.

## 📊 Estructura de Datos
El archivo `LIGO_Fractal_Dataset.csv` se compone de las siguientes columnas:

* **event**: Identificador oficial del evento de onda gravitacional.
* **dist_mpc**: Distancia de luminosidad en Megaparsecs (Mpc). Factor determinante para el decaimiento fractal.
* **is_ns**: Indicador booleano (True/False). Determina si el evento involucra una Estrella de Neutrones, lo cual preserva la coherencia de la semilla.
* **delta_F**: Valor de dimensión fractal calculado. 
    * **0.921**: Semilla Ancestral / Coherencia Máxima.
    * **0.918**: Límite de Ramificación / Rama Joven.
* **linaje**: Clasificación jerárquica del evento dentro del motor cíclico universal.

## 🔬 Criterio de Calidad
A diferencia de los catálogos masivos que incluyen candidatos ruidosos, este dataset se enfoca en **100 eventos de alta coherencia** para validar la estabilidad de la constante **0.921** como eje central del tejido espacio-temporal.

---
**Propiedad Intelectual:** Miguel Ángel Franco León (2026)
