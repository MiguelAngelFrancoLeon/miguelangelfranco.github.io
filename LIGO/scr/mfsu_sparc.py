import pandas as pd
import numpy as np

# =================================================================
# PROPIEDAD INTELECTUAL: MIGUEL ÁNGEL FRANCO LEÓN
# GENERADOR DE DATOS MFSU V3.0 - VALIDACIÓN GALAXY ROTATION (SPARC)
# =================================================================

class MFSUGalaxyEngine:
    def __init__(self):
        self.DELTA_F = 0.921  # Semilla de déficit fractal
        self.CHI = 5.85       # Impedancia métrica (Topological Invariant)
        self.G = 4.302e-6     # constante G en (kpc/Msun) * (km/s)^2

    def predecir_v(self, r_kpc, v_bar):
        """
        Aplica la corrección MFSU:
        V_mfsu = V_bar * sqrt( (r^delta_f) / chi )
        Donde r es el radio galactocéntrico en kpc.
        """
        if r_kpc <= 0: return 0, 100.0
        
        # Factor de amplificación MFSU (Sustituto de la Materia Oscura)
        # En la escala fractal, el flujo se conserva con r^(2-df)
        amplificacion = np.sqrt((r_kpc**self.DELTA_F) / self.CHI)
        
        v_pred = v_bar * amplificacion
        
        # Coherencia con el plateau observado
        return round(v_pred, 2), amplificacion

# Datos de muestra de SPARC (NGC 3198 - La galaxia 'Golden Standard')
# Radio (kpc), V_observada (km/s), V_barionica (km/s) [Gas + Estrellas]
datos_sparc = {
    'NGC3198': [
        {'r': 2.1, 'v_obs': 92, 'v_bar': 85},
        {'r': 5.2, 'v_obs': 148, 'v_bar': 120},
        {'r': 10.5, 'v_obs': 155, 'v_bar': 105},
        {'r': 15.8, 'v_obs': 153, 'v_bar': 92},
        {'r': 21.0, 'v_obs': 150, 'v_bar': 80},
        {'r': 30.5, 'v_obs': 148, 'v_bar': 65}
    ],
    'NGC2403': [
        {'r': 1.5, 'v_obs': 70, 'v_bar': 68},
        {'r': 4.0, 'v_obs': 110, 'v_bar': 95},
        {'r': 10.0, 'v_obs': 130, 'v_bar': 88},
        {'r': 18.0, 'v_obs': 134, 'v_bar': 75}
    ]
}

engine = MFSUGalaxyEngine()
filas = []

for galaxy, points in datos_sparc.items():
    for p in points:
        v_mfsu, factor = engine.predecir_v(p['r'], p['v_bar'])
        error = abs(v_mfsu - p['v_obs']) / p['v_obs'] * 100
        filas.append({
            'Galaxy': galaxy,
            'Radius_kpc': p['r'],
            'V_obs': p['v_obs'],
            'V_bar': p['v_bar'],
            'V_MFSU_Pred': v_mfsu,
            'MFSU_Factor': round(factor, 3),
            'Error_%': round(error, 2)
        })

df_sparc = pd.DataFrame(filas)

# Guardar resultados
df_sparc.to_csv('DATA_MFSU_VALIDATION_SPARC_V3.csv', index=False)
print("✅ Validación SPARC completada.")
print(df_sparc)
