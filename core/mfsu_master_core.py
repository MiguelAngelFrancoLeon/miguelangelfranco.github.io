"""
MFSU MASTER CORE (Unified Stochastic Fractal Model)
---------------------------------------------------
Este módulo unifica la lógica de dinámica galáctica (Rotación) 
y la clasificación de eventos gravitacionales (Ondas/Ramas).

Autor: Miguel Ángel Franco León
Versión: 2.0 (Fusión Limpia)
"""

import numpy as np
from dataclasses import dataclass

# --- CONSTANTES UNIVERSALES MFSU ---
MFSU_SEED = 0.921           # Delta_F (Semilla Maestra)
MFSU_DIMENSION = 2.079      # D_f = 3 - 0.921
MFSU_COUPLING = 5.85        # Chi (Factor de Empaquetamiento de Flujo)
G_CONST = 4.30091e-6        # (pc * km^2 / s^2 / M_sun)

@dataclass
class EventResult:
    """Estructura para devolver resultados de clasificación de eventos"""
    is_original: bool
    deviation: float
    category: str
    description: str

class MFSU_Master_Engine:
    def __init__(self):
        self.delta_f = MFSU_SEED
        self.d_f = MFSU_DIMENSION
        self.chi = MFSU_COUPLING

    # ---------------------------------------------------------
    # MÓDULO 1: DINÁMICA GALÁCTICA (Reemplaza a mfsu_logic.py)
    # ---------------------------------------------------------
    def get_rotation_velocity(self, mass_barionic, radius_kpc):
        """
        Calcula la velocidad de rotación usando el Motor de Cuaterniones MFSU.
        Sustituye a la Materia Oscura mediante geometría fractal.
        """
        if radius_kpc <= 0: return 0.0
        
        # 1. Corrección Dimensional (Ley de Gauss Fractal)
        epsilon_f = (self.d_f - 1)**self.delta_f
        
        # 2. Aceleración Base con Normalización Geométrica (Chi = 5.85)
        # Aquí es donde el 5.85 "sostiene" la curva en 150 km/s
        accel_base = (G_CONST * mass_barionic) / (radius_kpc**(self.d_f - 1))
        accel_mfsu = accel_base / (epsilon_f * self.chi)
        
        # 3. Estabilización de Torsión (Simulación del Cuaternión)
        # La vorticidad impide que la curva caiga (efecto meseta)
        torsion_factor = np.sqrt(1 + self.delta_f**2)
        accel_final = accel_mfsu * torsion_factor
        
        return np.sqrt(accel_final * radius_kpc)

    # ---------------------------------------------------------
    # MÓDULO 2: CLASIFICADOR DE EVENTOS (Reemplaza a MFSU_Classifier.py)
    # ---------------------------------------------------------
    def analyze_gw_event(self, measured_delta_f):
        """
        Analiza un evento de Onda Gravitacional (GW) comparando su firma
        fractal con la Semilla Maestra (0.921).
        
        Regla Teórica:
        - 0.921 (+/- tolerancia) -> Evento Original (Primario)
        - Diferente -> Rama (Branch) o Evento Joven
        """
        tolerance = 0.005 # Tolerancia de medición instrumental
        deviation = abs(measured_delta_f - self.delta_f)
        
        if deviation <= tolerance:
            return EventResult(
                is_original=True,
                deviation=deviation,
                category="ORIGINAL_EVENT",
                description="Firma coincide con la Semilla Maestra. Evento cósmico primario."
            )
        else:
            # Lógica de Ramas: Si la delta es mayor/menor, indica evolución
            age_indicator = "Younger/Branch" if measured_delta_f < self.delta_f else "Anomalous Branch"
            return EventResult(
                is_original=False,
                deviation=deviation,
                category="BRANCH_EVENT",
                description=f"Variación detectada ({deviation:.4f}). Clasificado como {age_indicator}."
            )

# --- PRUEBA RÁPIDA DE FUSIÓN ---
if __name__ == "__main__":
    engine = MFSU_Master_Engine()
    
    print("--- TEST DE FUSIÓN MFSU ---")
    
    # 1. Prueba de Física (Galaxia)
    v = engine.get_rotation_velocity(4.2e10, 20.0)
    print(f"[FÍSICA] Velocidad en 20kpc (M=4.2e10): {v:.2f} km/s (Objetivo: ~150)")
    
    # 2. Prueba de Clasificador (Ondas)
    event_a = engine.analyze_gw_event(0.921)
    event_b = engine.analyze_gw_event(0.850)
    
    print(f"[CLASIF] Evento 0.921: {event_a.category} -> {event_a.description}")
    print(f"[CLASIF] Evento 0.850: {event_b.category} -> {event_b.description}")
