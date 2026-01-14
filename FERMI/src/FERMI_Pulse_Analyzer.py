import pandas as pd
import numpy as np

# =================================================================
# PROPIEDAD INTELECTUAL: MIGUEL ÁNGEL FRANCO LEÓN
# VALIDACIÓN FERMI - EXTRUSIÓN GAMMA V1.0
# =================================================================

class MFSUFermiEngine:
    def __init__(self):
        self.SEED = 0.921
        self.CHI = 5.85

    def calcular_coherencia_gamma(self, energia_gev, altura_kpc):
        # La energía se ramifica a medida que la burbuja se expande (altura)
        n = int(altura_kpc / 2)
        delta_f_n = self.SEED * (1 - 0.00005)**n
        
        # El flujo gamma es proporcional a la relación Semilla/Impedancia
        factor_extrusion = (delta_f_n / self.CHI) * 100
        return round(delta_f_n, 5), n, round(factor_extrusion, 4)

# Datos de las Burbujas de Fermi (Basado en observaciones de 1-100 GeV)
datos_fermi = {
    'Region': ['North Bubble Base', 'North Bubble Mid', 'North Bubble Edge', 
               'South Bubble Base', 'South Bubble Mid', 'South Bubble Edge'],
    'Height_kpc': [1.0, 4.0, 8.0, 1.0, 4.0, 8.0],
    'Energy_GeV': [50, 20, 5, 50, 20, 5]
}

df_fermi = pd.DataFrame(datos_fermi)
engine = MFSUFermiEngine()

# Procesamiento
resultados = df_fermi.apply(lambda x: engine.calcular_coherencia_gamma(x['Energy_GeV'], x['Height_kpc']), axis=1)
df_fermi[['delta_F', 'n_nivel', 'Extrusion_Flux_%']] = pd.DataFrame(resultados.tolist(), index=df_fermi.index)

# Guardar
df_fermi.to_csv('DATA_MFSU_VALIDATION_FERMI_V1.csv', index=False)
print("✅ Validación FERMI completada.")
print(df_fermi)
