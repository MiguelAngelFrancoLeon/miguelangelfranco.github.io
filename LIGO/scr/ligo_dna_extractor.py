import math

# Constantes MFSU
CHI = 12.65
SATURACION_DIAMANTE = 0.921

def analizar_evento_ligo(m1, m2, energia_irradiada):
    """
    Calcula la desviación fractal en una fusión de agujeros negros.
    """
    masa_total = m1 + m2
    # La eficiencia de la red de espín para absorber el choque
    eficiencia_fractal = energia_irradiada / masa_total
    
    # En un evento de colapso, el delta_F se altera
    # Si delta_f = 0.921, el evento es 'original' o en equilibrio
    # La desviación indica la 'juventud' o 'tensión' de la rama local
    delta_f_evento = SATURACION_DIAMANTE + (eficiencia_fractal * math.log(CHI))
    
    return {
        'delta_f_pico': round(delta_f_evento, 4),
        'tension_red': round(delta_f_evento - SATURACION_DIAMANTE, 4),
        'tipo': 'Estabilización' if delta_f_evento > 0.921 else 'Rama Joven'
    }

# Ejemplo con el primer evento histórico GW150914
# m1=36, m2=29, energía irradiada=3 masas solares
print(analizar_evento_ligo(36, 29, 3))
