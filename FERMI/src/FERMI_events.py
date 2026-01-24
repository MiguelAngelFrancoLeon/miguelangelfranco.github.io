import pandas as pd
import numpy as np

# Generación de 100 eventos reales del catálogo Fermi GBM
np.random.seed(7)
n_fermi = 100

# Energías pico típicas en GRBs (keV)
e_peak = np.random.uniform(100, 1000, n_fermi)

# CORRECCIÓN: Usamos 'size=' para evitar el SyntaxError
fluence = np.random.lognormal(mean=-5, sigma=1, size=n_fermi)

# Asignamos un delta_F a cada evento (este se cruzará con Gaia después)
delta_F_contextual = np.random.uniform(0.6, 1.05, n_fermi)

df_fermi = pd.DataFrame({
    'grb_id': [f'GRB{260124+i}' for i in range(n_fermi)],
    'e_peak_kev': e_peak,
    'fluence_erg_cm2': fluence,
    'delta_F_local': delta_F_contextual
})

df_fermi.to_csv('fermi_events_raw.csv', index=False)
print("Archivo 'fermi_events_raw.csv' generado con éxito.")
