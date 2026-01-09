import pandas as pd
import numpy as np
from google.colab import files

# =================================================================
# MFSU: FERMI GAMMA-RAY BURST (GRB) ANALYZER
# "The Heartbeat of the Fractal Engine"
# =================================================================

def clasificador_fermi(fluence, duration_s):
    """
    Clasifica el GRB según la pureza del latido.
    Fluence > 1e-4 o duración extrema indica conexión directa a la Semilla.
    """
    if fluence > 1e-4 or duration_s > 1000:
        return 0.921  # Latido Semilla (Extrusión pura)
    
    # Decaimiento hacia ramas secundarias para eventos menores
    return 0.918

# Datos reales de eventos históricos (Fermi/GBM Catalog)
data_fermi = {
    'grb_id': ['GRB 221009A (BOAT)', 'GRB 250702B', 'GRB 130427A', 'GRB 190114C', 'GRB 080916C', 'GRB 211211A'],
    'fluence_erg_cm2': [0.021, 0.005, 0.0006, 0.0004, 0.0002, 0.0005],
    'duration_s': [600, 25200, 138, 116, 66, 51],
    'type': ['Long', 'Ultra-Long/Repeating', 'Long', 'Long', 'Long', 'Kilonova-like']
}

df_fermi = pd.DataFrame(data_fermi)
df_fermi['delta_F'] = df_fermi.apply(lambda x: clasificador_fermi(x['fluence_erg_cm2'], x['duration_s']), axis=1)
df_fermi['linaje'] = np.where(df_fermi['delta_F'] == 0.921, 'Latido Semilla', 'Latido Rama')

# Guardar y descargar
filename = 'FERMI_Heartbeat_Data.csv'
df_fermi.to_csv(filename, index=False)
files.download(filename)
print("✅ Dataset de Fermi (Latidos del Motor) listo para blindar.")
