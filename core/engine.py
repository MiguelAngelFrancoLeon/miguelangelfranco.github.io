import math
from .constants import DELTA_F, RU, FRACTAL_SCALE

def franco_reduction_law(n=0):
    """
    Calcula la coherencia en cualquier nivel del fractal.
    n=0: Rama Original (Tronco)
    n>0: Ramas secundarias (Eventos jóvenes)
    """
    return DELTA_F * math.exp(-RU * n)

def apply_mfsu_transform(v_newtonian, n=0):
    """
    Transformación Maestra MFSU.
    Convierte la velocidad bariónica en velocidad observada.
    """
    # 1. Obtenemos la saturación de la rama
    coherence = franco_reduction_law(n)
    
    # 2. Aplicamos el factor de escala fractal (1.22)
    # y compensamos la reducción topológica (7.9%)
    v_corrected = v_newtonian * FRACTAL_SCALE * (1 + (1 - coherence) * 1.91)
    
    return v_corrected
