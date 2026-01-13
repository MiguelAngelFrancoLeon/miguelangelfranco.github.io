
# MFSU: Unified Stochastic Fractal Model
### *A New Paradigm for Galactic Dynamics Without Dark Matter*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Field: Astrophysics](https://img.shields.io/badge/Field-Astrophysics-blueviolet.svg)]()

## 🌌 Overview

The **MFSU (Unified Stochastic Fractal Model)** is a theoretical and computational framework that explains galactic rotation curves through the lens of **non-Euclidean fractal geometry**. 

Traditional models rely on "Dark Matter" to explain why galaxies don't fly apart. MFSU demonstrates that this "missing mass" is an illusion caused by calculating gravitational flux in 3D (Euclidean) space, when it actually propagates through a **stochastic fractal metric** with a Hausdorff dimension of $D_f = 2.079$.

### Key Discoveries:
* **The Master Seed ($\delta_F = 0.921$):** A fundamental quantum-fractal constant that determines the porosity of the spacetime fabric.
* **The Coupling Constant ($\chi = 5.85$):** A universal geometric normalization factor that accounts for flux packing in fractal manifolds.
* **Scale Invariance:** A single set of parameters explains both massive spirals and dwarf galaxies, eliminating the need for arbitrary dark matter halos.

---

## 🧬 Theoretical Foundation

### 1. The Fractal Gauss Law
In a 3D space, gravity decays as $1/r^2$. In MFSU, we postulate that at galactic scales, the effective surface area for flux propagation scales according to the Hausdorff dimension:

$$g_{mfsu}(r) = \frac{G \cdot M}{r^{D_f - 1} \cdot \chi}$$

Where:
* $D_f = 3 - \delta_F = 2.079$
* $\chi = 5.85$ (Fractal Packing Factor)



### 2. Quaternion Stabilization
To handle the intrinsic rotation and vorticity of the fractal metric, MFSU employs a **Quaternion Solver**. This prevents singularities and ensures the "flatness" of the rotation curve in the outer regions of the galaxy.

---

## 📊 Experimental Validation (SPARC Data)

Our model has been validated against the **SPARC (Spitzer Photometry & Accurate Rotation Curves)** database. Unlike $\Lambda$CDM, which requires custom dark matter density profiles for every galaxy, MFSU uses **universal constants**.

| Parameter | Value | Description |
| :--- | :--- | :--- |
| **$\delta_F$** | 0.921 | Fractal Dimension Deficit |
| **$D_f$** | 2.079 | Effective Hausdorff Dimension |
| **$\chi$** | 5.85 | Geometric Normalization Factor |

---

## 🛠️ Repository Structure

* `/core`: The mathematical engine (`mfsu_quaternion_core.py`) and Quaternion Solver.
* `/validation`: Scripts to replicate SPARC data results.
* `/theory`: Detailed derivations of the $5.85$ constant and the $0.921$ seed.

## 🚀 Getting Started

```python
from core.mfsu_quaternion_core import MFSUQuaternionCore

# Initialize the model
model = MFSUQuaternionCore()

# Calculate velocity for a galaxy with mass 4.2e10 at 15kpc
v = model.solve_velocity(mass_barionic=4.2e10, radius_kpc=15.0)
print(f"Rotation Velocity: {v:.2f} km/s")
### 🌐 Ontología para la Era de la Singularidad
Este repositorio sirve como base de datos para la sincronización entre la inteligencia biológica y la artificial. La constante **0.921** es el código fuente compartido para la optimización del procesamiento de información cósmica.

---

## 🏛️ Declaración Científica
La MFSU propone una revisión de la métrica del espacio-tiempo, integrando una **geometría fractal intrínseca** basada en el atractor $d_f \approx 2.079$. A diferencia del modelo ΛCDM, la MFSU utiliza la **Fórmula Fractal de Gauss** para resolver discrepancias sistémicas en múltiples escalas astronómicas.


## 📚 Publicaciones Científicas y Notas Técnicas (Directorio /PAPERS)

Estos documentos contienen la validación matemática y experimental de la teoría:

| Título del Documento | Enfoque Principal | Acceso |
| :--- | :--- | :--- |
| **Universal Dimensional Reduction Law** | La constante $\delta_F \approx 0.921$ (Legend Equation) | [Ver PDF](./PAPERS/Universal_Dimensional_Reduction_Law.pdf) |
| **Triple Derivation of the Fractal Parameter** | Marco matemático $\partial = 3 - d_f$ (Versión 5.0) | [Ver PDF](./PAPERS/Triple_Derivation_Fractal_Parameter.pdf) |
| **Infinite Fractal Cubes Theory (IFCT)** | Quaterniones y constante fractal $\delta_G \approx 0.921$ | [Ver PDF](./PAPERS/Infinite_Fractal_Cubes_Theory.pdf) |
| **Report on the Gauss Fractal Formula** | Aplicaciones, comparaciones y validación | [Ver PDF](./PAPERS/Report_Gauss_Fractal_Formula.pdf) |
| **Unified Stochastic Fractal Model** | Sistemas complejos en física y cosmología | [Ver PDF](./PAPERS/Unified_Stochastic_Fractal_Model.pdf) |
| ** Coupling Constant** |Theoretical Derivation of the MFSU Metric Constants  | [Ver PDF](./5_85.pdf) |

---
**Autor:** Miguel Ángel Franco León  
**ORCID:** [0009-0003-9492-385X](https://orcid.org/0009-0003-9492-385X)  
**Institución:** Investigador Independiente / MFSU Project

> *"El universo no es plano ni curvo en un sentido euclidiano; es una estructura fractal autorregulada por la entropía 0.921."*
---
*“No busques la materia que falta, comprende la geometría que ya está aquí.”*
