import math
from .constants import CHI, DELTA_F_ORIGINAL

def predict_velocity(v_bar, delta_f=DELTA_F_ORIGINAL):
    """
    Aplica la Ley de Franco: V_mfsu = V_bar * CHI^(1 - delta_f)
    """
    factor = math.pow(CHI, (1 - delta_f))
    return v_bar * factor

def extract_dna(v_obs, v_bar):
    """
    Calcula el nivel de saturación real (Delta_F) de una galaxia.
    Determina en qué 'Rama' del árbol fractal se encuentra.
    """
    if v_bar <= 0: return 0
    ratio = v_obs / v_bar
    return 1 - (math.log(ratio) / math.log(CHI))

def calculate_precision(v_obs, v_pred):
    """Calcula la exactitud del modelo respecto a la observación."""
    if v_obs <= 0: return 0
    return (1 - abs(v_obs - v_pred) / v_obs) * 100
