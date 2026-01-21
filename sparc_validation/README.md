# MFSU: Modelo Fractal Estocástico Unificado
### Validación Masiva con el Catálogo SPARC (175 Galaxias)

Este repositorio presenta la validación empírica del modelo **MFSU**, desarrollado por **Miguel Ángel Franco**. La investigación demuestra que las anomalías en las curvas de rotación galáctica, tradicionalmente atribuidas a la materia oscura, pueden explicarse mediante la **Ley de Reducción Dimensional** basada en la **Identidad de Euler-Franco**.

---

## 🌌 El "Doble Camino" del 0.921
La potencia de este modelo reside en la convergencia de dos vías independientes hacia una misma constante de coherencia fractal: **$\delta_F = 0.921$**.

1. **Vía Teórica (Geometría del Vacío):** Derivada de la impedancia topológica del espacio-tiempo ($\chi = 5.85$) mediante la Identidad de Euler-Franco.
   
2. **Vía Observacional (Cinemática Galáctica):** Validada empíricamente ajustando las velocidades de rotación de 175 galaxias del catálogo SPARC sin usar halos de materia oscura.

---

## 📊 Metodología y Ecuación Maestro
Para cada galaxia, se calcula la velocidad predicha ($V_{MFSU}$) a partir de la masa visible (gas + estrellas) utilizando la constante de reducción dimensional:

$$V_{MFSU} = \frac{V_{bar}}{\sqrt{0.921}}$$

Donde $V_{bar}$ representa la contribución bariónica total calculada de forma Newtoniana.

---

## 📂 Estructura de Datos en este Repo
Los resultados del procesamiento masivo se dividen en:

* **`MFSU_SPARC_FULL_DATABASE.csv`**: Datos punto por punto de las 175 galaxias, incluyendo radio, velocidad observada y predicción fractal.
* **`Resumen_Precision_Galactica.csv`**: Análisis estadístico que clasifica las galaxias según su nivel de ajuste.
    * **Eventos Originales:** Alta coherencia con el valor base 0.921.
    * **Ramas (Branching):** Desviaciones que indican sistemas más jóvenes o evoluciones del evento original.

---

## 🛠️ Cómo Replicar el Estudio
El código de procesamiento está optimizado para ejecutarse en entornos de Python (Google Colab/Jupyter). 

1. Descarga el catálogo SPARC (Lelli et al. 2016).
2. Ejecuta el script de validación incluido para procesar los archivos `.dat`.
3. Compara los residuos resultantes con el modelo estándar $\Lambda$CDM.

---

## ✉️ Contacto e Investigación
**Autor:** Miguel Ángel Franco  
*Arquitecto de Datos e Investigador en Astrofísica Teórica.*

> "La gravedad no es una partícula invisible, es la firma geométrica del espacio fractal."
