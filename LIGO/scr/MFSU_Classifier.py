import pandas as pd
import numpy as np

# =================================================================
# PROPIEDAD INTELECTUAL: MIGUEL ÁNGEL FRANCO LEÓN
# MODELO: UNIFIED STOCHASTIC FRACTAL MODEL (MFSU) V2.2
# MOTOR: LEY DE REDUCCIÓN DIMENSIONAL & IMPEDANCIA CHI (5.85)
# =================================================================

class MFSUEngine:
    def __init__(self):
        self.SEMILLA = 0.921
        self.RF = 0.00005  # Factor de reducción por nivel
        self.CHI = 5.85    # Impedancia del vacío fractal

    def procesar_evento(self, dist_mpc, es_ns):
        # 1. Coherencia en el origen o materia densa
        if es_ns or dist_mpc < 100:
            return self.SEMILLA, 0, 100.0

        # 2. CALCULO DE RAMIFICACIÓN REAL (No lineal)
        # La distancia dicta cuántas veces se ha ramificado la señal (n)
        # Usamos una escala logarítmica basada en la estructura de red
        n = int(np.log1p(dist_mpc) * 1.8) # Factor de escala estructural
        
        # Aplicación de la Ley de Reducción: delta_F(n) = Seed * (1 - Rf)^n
        delta_f_n = self.SEMILLA * (1 - self.RF)**n
        
        # 3. Cálculo de Coherencia con la Métrica 5.85
        # La impedancia afecta la fidelidad de la señal
        coherencia = (1 - (n * self.RF / self.CHI)) * 100
        
        return round(delta_f_n, 5), n, round(coherencia, 4)

# --- DATASET REAL (LIGO/VIRGO) ---
data = {
    'event': [
        'GW150914', 'GW151226', 'GW170104', 'GW170608', 'GW170729', 'GW170809', 'GW170814', 'GW170817', 
        'GW190425', 'GW190521', 'GW200105', 'GW240109' # ... (puedes añadir todos los de tu lista)
    ],
    'dist_mpc': [430, 440, 960, 320, 2750, 990, 580, 40, 159, 5300, 280, 1510],
    'is_ns': [False, False, False, False, False, False, False, True, True, False, True, False]
}

# (Para efectos de brevedad usé una submuestra, pero el motor procesa los 90+ eventos igual)
df = pd.DataFrame(data)
engine = MFSUEngine()

# Aplicar el motor a los datos reales
resultados = df.apply(lambda x: engine.procesar_evento(x['dist_mpc'], x['is_ns']), axis=1)
df[['delta_F', 'Nivel_n', 'Coherencia_%']] = pd.DataFrame(resultados.tolist(), index=df.index)

# Clasificación por Ramificación Fractal
def clasificar_linaje(n):
    if n == 0: return 'TRONCO (Semilla Pura)'
    if n <= 10: return 'RAMA PRIMARIA (Alta Energía)'
    return 'RAMA DISTAL (Reducción Dimensional)'

df['Linaje_Fractal'] = df['Nivel_n'].apply(clasificar_linaje)

# Ordenar por nivel de ramificación
df = df.sort_values(by='Nivel_n')

print("--- 🏛️ REPORTE DE UNIFICACIÓN MFSU V2.2 (LIGO DATA) ---")
print(df[['event', 'dist_mpc', 'Nivel_n', 'delta_F', 'Coherencia_%', 'Linaje_Fractal']].to_string(index=False))
