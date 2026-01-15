# =============================================================================
# MFSU: IXPE POLARIMETRY VALIDATION (QUATERNION ENGINE)
# Arquitecto: Miguel Ángel Franco León
# Objetivo: Validar la rotación de fase en Rayos X de alta energía
# =============================================================================

import numpy as np
import pandas as pd

class IXPE_MFSU_Engine:
    def __init__(self):
        self.delta_F0 = 0.921   # Semilla de Coherencia
        self.chi = 5.85          # Impedancia (Regula el grado de polarización)
        self.tau = 2.221         # Tortuosidad (Afecta el ángulo de fase)

    def compute_ixpe_quaternion(self, obs_pd, obs_pa):
        """
        obs_pd: Polarization Degree (0 to 1)
        obs_pa: Polarization Angle (degrees)
        """
        # El grado de polarización real es una función de la coherencia delta_F
        # Si delta_F baja, la dispersión aumenta (menor PD)
        expected_pd = self.delta_F0 / (1 + (self.chi / 100)) 
        
        # Rotación Cuaterniónica basada en el ángulo observado
        theta = np.radians(obs_pa)
        qw = np.cos(theta / 2) * self.delta_F0
        qz = np.sin(theta / 2) * (1 - self.delta_F0)
        
        return qw, qz, expected_pd

# --- PROCESAMIENTO DE FUENTES REALES IXPE ---
def generate_ixpe_data():
    engine = IXPE_MFSU_Engine()
    
    # Fuentes icónicas de IXPE (Data real aproximada de misiones 2024-2025)
    sources = [
        {'name': 'Cassiopeia A', 'obs_pd': 0.05, 'obs_pa': 78.0},
        {'name': 'Crab Nebula', 'obs_pd': 0.20, 'obs_pa': 136.0},
        {'name': 'Cyg X-1', 'obs_pd': 0.04, 'obs_pa': 21.0},
        {'name': 'MSH 15-52', 'obs_pd': 0.15, 'obs_pa': 120.0}
    ]
    
    results = []
    for s in sources:
        qw, qz, exp_pd = engine.compute_ixpe_quaternion(s['obs_pd'], s['obs_pa'])
        
        results.append({
            'Source': s['name'],
            'Obs_PD': s['obs_pd'],
            'Obs_PA_deg': s['obs_pa'],
            'MFSU_Quat_W': round(qw, 6),
            'MFSU_Quat_Z': round(qz, 6),
            'Topological_Coherence': round(qw / engine.delta_F0, 4)
        })
        
    df = pd.DataFrame(results)
    df.to_csv('IXPE_MFSU_DATA.csv', index=False)
    print("✅ IXPE_MFSU_DATA.csv generado con éxito.")

if __name__ == "__main__":
    generate_ixpe_data()
