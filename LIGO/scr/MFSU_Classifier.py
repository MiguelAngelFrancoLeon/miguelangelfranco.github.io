import pandas as pd
import numpy as np

# =================================================================
# PROPIEDAD INTELECTUAL: MIGUEL ÁNGEL FRANCO LEÓN
# MODELO: UNIFIED STOCHASTIC FRACTAL MODEL (MFSU)
# CONSTANTES: SEED (0.921) | BRANCH (0.918)
# =================================================================

def clasificador_mfsu(dist_mpc, es_ns):
    """
    Calcula el decaimiento de la señal según la Distancia de Franco.
    """
    # 1. Regla de Coherencia de Materia Densa (Estrellas de Neutrones)
    if es_ns or dist_mpc < 150:
        return 0.921
    
    # 2. Cálculo de Ramificación por Desgaste Espacial (Pendiente Fractal)
    # A mayor distancia, la señal se aleja de la semilla (0.921) hacia la rama (0.918)
    pendiente = (dist_mpc / 10000) * (0.921 - 0.918)
    resultado = 0.921 - pendiente
    
    # 3. Límite de Estabilidad (No puede bajar de la rama joven 0.918)
    return max(0.918, round(resultado, 3))

# --- DATASET COMPLETO (GWTC-1, 2, 3 y 4.0 Aproximado) ---
data = {
    'event': [
        'GW150914', 'GW151226', 'GW170104', 'GW170608', 'GW170729', 'GW170809', 'GW170814', 'GW170817', 'GW170818', 'GW170823',
        'GW190408', 'GW190412', 'GW190421', 'GW190424', 'GW190425', 'GW190426', 'GW190503', 'GW190512', 'GW190513', 'GW190514',
        'GW190517', 'GW190519', 'GW190521', 'GW190521_074359', 'GW190527', 'GW190602', 'GW190620', 'GW190630', 'GW190701', 'GW190706',
        'GW190707', 'GW190708', 'GW190719', 'GW190720', 'GW190727', 'GW190728', 'GW190731', 'GW190803', 'GW190814', 'GW190828_063405',
        'GW190828_065509', 'GW190909', 'GW190910', 'GW190915', 'GW190924', 'GW190925', 'GW190930', 'GW200105', 'GW200112', 'GW200115',
        'GW200129', 'GW200202', 'GW200208_130117', 'GW200209', 'GW200210', 'GW200216', 'GW200219', 'GW200220_061928', 'GW200224', 'GW200225',
        'GW200302', 'GW200311', 'GW200316', 'GW240109', 'GW240107', 'GW240104', 'GW231231', 'GW231226', 'GW231224', 'GW231223_202619',
        'GW231221', 'GW231213', 'GW231206_233901', 'GW231129', 'GW231127', 'GW231123', 'GW231119', 'GW231118_090602', 'GW231114',
        'GW231113_200417', 'GW231110', 'GW231108', 'GW231104', 'GW231102', 'GW231029', 'GW231028', 'GW231020', 'GW231018', 'GW231014',
        'GW231008', 'GW231005_091549', 'GW231004'
    ],
    'dist_mpc': [
        430, 440, 960, 320, 2750, 990, 580, 40, 1020, 1850,
        1580, 730, 3150, 2550, 159, 370, 1450, 1430, 2060, 4100,
        1860, 2530, 5300, 1240, 2500, 2700, 2800, 890, 2060, 4400,
        770, 880, 3900, 790, 790, 870, 3300, 3300, 241, 2130,
        1600, 3800, 1460, 1620, 570, 930, 760, 280, 1250, 300,
        900, 410, 2230, 3400, 940, 3800, 3400, 6000, 1710, 1150,
        1480, 1170, 1120, 1510, 5800, 1910, 1070, 1180, 950, 890,
        4600, 4000, 1490, 3800, 4500, 2200, 6700, 1350, 1380, 1160,
        1890, 2060, 1470, 3800, 3100, 4100, 1230, 1530, 2300, 3000,
        3800, 6400, 4300
    ],
    'is_ns': [
        False, False, False, False, False, False, False, True, False, False,
        False, False, False, False, True, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, True, False, True,
        False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False,
        False, False, False
    ]
}

df = pd.DataFrame(data)
df['delta_F'] = df.apply(lambda x: clasificador_mfsu(x['dist_mpc'], x['is_ns']), axis=1)

# Clasificación de Linaje (Jerarquía MFSU)
condiciones = [
    (df['delta_F'] == 0.921),
    (df['delta_F'] < 0.921) & (df['delta_F'] > 0.919),
    (df['delta_F'] <= 0.919)
]
etiquetas = ['Semilla Original', 'Rama Primaria (Madura)', 'Rama Joven (Distante)']
df['linaje'] = np.select(condiciones, etiquetas)

# Ordenar por importancia fractal
df = df.sort_values(by=['delta_F', 'dist_mpc'], ascending=[False, True])

print("--- REPORTE DE CLASIFICACIÓN FRACTAL MFSU ---")
print(df[['event', 'dist_mpc', 'delta_F', 'linaje']].to_string(index=False))

print("\n--- RESUMEN DE DISTRIBUCIÓN ---")
print(df['linaje'].value_counts())
