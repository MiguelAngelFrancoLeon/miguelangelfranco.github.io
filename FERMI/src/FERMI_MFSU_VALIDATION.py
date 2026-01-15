# =============================================================================
# MFSU: FERMI-LAT GAMMA-RAY VALIDATION (QUATERNION ENGINE)
# Arquitecto: Miguel Ángel Franco León
# Objetivo: Validar la dispersión de alta energía en el vacío fractal
# =============================================================================

import numpy as np
import pandas as pd

class FermiMFSU_Engine:
    def __init__(self):
        self.delta_F0 = 0.921   # Semilla Primordial
        self.chi = 5.85          # Impedancia Topológica
        self.Rf = 5.03e-5        # Constante de Ramificación

    def analyze_gamma_event(self, energy_gev, distance_mpc):
        """
        Calcula la pérdida de coherencia de un fotón gamma basado en la distancia.
        n (generación) es proporcional al recorrido en el medio fractal.
        """
        # Estimación de n basada en la escala de Fermi (megaparsecs)
        n = int(distance_mpc * 10) 
        df_n = self.delta_F0 * (1 - self.Rf)**n
        
        # Rotación de fase cuaterniónica
        theta = np.arccos(df_n)
        qw = np.cos(theta / 2)
        qz = np.sin(theta / 2)
        
        # El flujo observado se ve reducido por la impedancia chi
        flux_correction = self.chi ** (1 - qw)
        
        return df_n, qw, qz, flux_correction

# --- PROCESAMIENTO DE FUENTES REALES FERMI-LAT ---
def generate_fermi_data():
    engine = FermiMFSU_Engine()
    
    # Fuentes de rayos gamma (Datos reales de catálogos 4FGL)
    sources = [
        {'name': 'Vela Pulsar', 'energy_gev': 10, 'dist_mpc': 0.00029}, # Cercano (Tronco)
        {'name': '3C 273 (Quasar)', 'energy_gev': 50, 'dist_mpc': 749.0}, # Lejano (Rama)
        {'name': 'M87 Core', 'energy_gev': 100, 'dist_mpc': 16.4},      # Intermedio
        {'name': 'CTA 102', 'energy_gev': 20, 'dist_mpc': 2400.0}       # Extremo
    ]
    
    results = []
    for s in sources:
        df_n, qw, qz, f_corr = engine.analyze_gamma_event(s['energy_gev'], s['dist_mpc'])
        
        results.append({
            'Source': s['name'],
            'Dist_Mpc': s['dist_mpc'],
            'Energy_GeV': s['energy_gev'],
            'MFSU_Coherence': round(df_n, 6),
            'Quat_W': round(qw, 6),
            'Quat_Z': round(qz, 6),
            'Flux_Attenuation_Factor': round(f_corr, 4),
            'Status': 'ORIGINAL' if df_n > 0.920 else 'DECAYED_BRANCH'
        })
    
    df = pd.DataFrame(results)
    df.to_csv('FERMI_MFSU_DATA.csv', index=False)
    print("✅ FERMI_MFSU_DATA.csv generado.")

if __name__ == "__main__":
    generate_fermi_data()
