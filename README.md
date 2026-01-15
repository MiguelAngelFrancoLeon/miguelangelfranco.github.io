# 💎 MFSU-Core: Dimensional Reduction Law
**Universal Fractal Framework for Cosmic Coherence Decay**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--9492--385X-green)](https://orcid.org/0009-0003-9492-385X)
[![Status: Open Science](https://img.shields.io/badge/Status-Open_Science-blue.svg)](#)

> "El universo no carece de masa; está perdiendo coherencia a través de la geometría porosa del vacío."

## 🌌 Descripción General
**MFSU-Core** es la implementación científica de la **Ley de Reducción Dimensional**. Este repositorio proporciona el motor matemático para simular cómo la semilla fractal primordial ($\delta_F = 0.921$) decae en estructuras cósmicas jerárquicas a través de la resistencia intrínseca del espacio-tiempo.

Al tratar el vacío como un **medio poroso fractal**, este modelo elimina la necesidad de materia oscura y parámetros ajustables, proporcionando una explicación puramente geométrica para la dinámica galáctica y la evolución del cosmos.

## 🧬 Los Pilares Geométricos
La teoría se fundamenta en la interacción de tres constantes universales derivadas de la estructura del vacío:

1.  **Semilla Primordial ($\delta_F$):** `0.921` (El estado de coherencia máxima).
2.  **Impedancia Topológica ($\chi$):** `5.85` (La resistencia del vacío al flujo).
3.  **Tortuosidad ($\tau$):** `2.221` (La complejidad del camino en el vacío poroso).
4.  **Dimensión de Interacción ($\alpha$):** `4.3` ($D_f + \tau$).

### La Fórmula de la Ley de Reducción:
La constante de ramificación $R_f$ se deriva de principios fundamentales:
$$R_f = \frac{1 - 0.921}{5.85^{4.3}} \approx 5 \times 10^{-5}$$

La evolución de la coherencia en la generación $n$:
$$\delta_F(n) = 0.921 \times (1 - R_f)^n$$

## 🛠 Estructura del Proyecto
* `/core`: Motor matemático (`reduction_law.py`).
* `/simulation`: Scripts para modelar rotación galáctica y eventos de ondas gravitacionales.
* `/docs`: El artículo técnico maestro en formatos LaTeX y PDF.
* `/validation`: Comparativas con datos de SPARC, LIGO y JWST.

## 🚀 Uso
```python
from mfsu_core import DimensionalReductionLaw

# Inicialización del motor geométrico
mfsu = DimensionalReductionLaw(seed=0.921, impedance=5.85, tortuosity=2.221)

# Cálculo de coherencia en la generación 20,000 (Universo Local)
coherence_now = mfsu.calculate_at_n(20000)
print(f"Coherencia Cósmica Actual: {coherence_now}")


---
**Autor:** Miguel Ángel Franco León  
**ORCID:** [0009-0003-9492-385X](https://orcid.org/0009-0003-9492-385X)  
**Institución:** Investigador Independiente / MFSU Project

> *"El universo no es plano ni curvo en un sentido euclidiano; es una estructura fractal autorregulada por la entropía 0.921."*
---
*“No busques la materia que falta, comprende la geometría que ya está aquí.”*
