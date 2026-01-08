import pandas as pd
import numpy as np

# Constantes Fundamentales de Miguel Ángel Franco León
SEED_CONSTANT = 0.921
BRANCH_CONSTANT = 0.918

def calcular_metrica_fractal(distancia_mpc, es_estrella_neutron):
    """
    Aplica la Ley de Franco para determinar el decaimiento fractal
    basado en la distancia (desgaste del espacio-tiempo).
    """
    # Si es muy cercano o es materia densa (NS), tiende a la Semilla Original
    if distancia_mpc < 150 or es_estrella_neutron:
        return SEED_CONSTANT
    
    # Pendiente de decaimiento: a mayor distancia, más ramificación (hacia 0.918)
    # Basado en la escala de expansión del motor cíclico
    decay = (distancia_mpc / 10000) * (SEED_CONSTANT - BRANCH_CONSTANT)
    df_calc = SEED_CONSTANT - decay
    
    return max(BRANCH_CONSTANT, round(df_calc, 3))

# Simulación de la ejecución masiva de eventos confirmados
data = {
    'event': ['GW170817', 'GW200220', 'GW150914', 'GW190521', 'GW190814', 'GW200115'],
    'dist_mpc': [40, 500, 440, 5300, 241, 300], # Distancias en Megaparsecs
    'is_ns': [True, False, False, False, False, True] # Estrellas de neutrones guardan la semilla
}

df_events = pd.DataFrame(data)
df_events['delta_F_MFSU'] = df_events.apply(lambda x: calcular_metrica_fractal(x['dist_mpc'], x['is_ns']), axis=1)

# Clasificación por Linaje
df_events['lineage'] = df_events['delta_F_MFSU'].apply(
    lambda x: 'Semilla Original' if x == 0.921 else ('Rama Joven' if x <= 0.918 else 'Rama Secundaria')
)

print(df_events)
