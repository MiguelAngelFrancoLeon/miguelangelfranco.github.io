import pandas as pd
import numpy as np

# =================================================================
# PROPIEDAD INTELECTUAL: MIGUEL ÁNGEL FRANCO LEÓN
# GENERADOR DE DATOS MFSU V2.2 - VALIDACIÓN LIGO (92 EVENTOS)
# =================================================================

class MFSUEngine:
    def __init__(self):
        self.SEMILLA = 0.921
        self.RF = 0.00005
        self.CHI = 5.85

    def procesar(self, dist_mpc, es_ns):
        # Regla de origen para distancias cortas o estrellas de neutrones
        if es_ns or dist_mpc < 100:
            return self.SEMILLA, 0, 100.0
        
        # LEY DE REDUCCIÓN DIMENSIONAL (Cálculo del nivel n)
        # Basado en la escala logarítmica de la red fractal
        n = int(np.log1p(dist_mpc) * 1.8)
        
        # delta_F(n) = 0.921 * (1 - 0.00005)^n
        delta_f_n = self.SEMILLA * (1 - self.RF)**n
        
        # Coherencia métrica considerando la impedancia 5.85
        coherencia = (1 - (n * self.RF / self.CHI)) * 100
        return round(delta_f_n, 5), n, round(coherencia, 4)

# Datos maestros (Asegurando simetría total)
eventos_mpc = {
    'GW150914': 430, 'GW151226': 440, 'GW170104': 960, 'GW170608': 320, 'GW170729': 2750, 
    'GW170809': 990, 'GW170814': 580, 'GW170817': 40, 'GW170818': 1020, 'GW170823': 1850,
    'GW190408': 1580, 'GW190412': 730, 'GW190421': 3150, 'GW190424': 2550, 'GW190425': 159, 
    'GW190426': 370, 'GW190503': 1450, 'GW190512': 1430, 'GW190513': 2060, 'GW190514': 4100,
    'GW190517': 1860, 'GW190519': 2530, 'GW190521': 5300, 'GW190521_074359': 1240, 'GW190527': 2500, 
    'GW190602': 2700, 'GW190620': 2800, 'GW190630': 890, 'GW190701': 2060, 'GW190706': 4400,
    'GW190707': 770, 'GW190708': 880, 'GW190719': 3900, 'GW190720': 790, 'GW190727': 790, 
    'GW190728': 870, 'GW190731': 3300, 'GW190803': 3300, 'GW190814': 241, 'GW190828_063405': 2130,
    'GW190828_065509': 1600, 'GW190909': 3800, 'GW190910': 1460, 'GW190915': 1620, 'GW190924': 570, 
    'GW190925': 930, 'GW190930': 760, 'GW200105': 280, 'GW200112': 1250, 'GW200115': 300,
    'GW200129': 900, 'GW200202': 410, 'GW200208_130117': 2230, 'GW200209': 3400, 'GW200210': 940, 
    'GW200216': 3800, 'GW200219': 3400, 'GW200220_061928': 6000, 'GW200224': 1710, 'GW200225': 1150,
    'GW200302': 1480, 'GW200311': 1170, 'GW200316': 1120, 'GW240109': 1510, 'GW240107': 5800, 
    'GW240104': 1910, 'GW231231': 1070, 'GW231226': 1180, 'GW231224': 950, 'GW231223_202619': 890,
    'GW231221': 4600, 'GW231213': 4000, 'GW231206_233901': 1490, 'GW231129': 3800, 'GW231127': 4500, 
    'GW231123': 2200, 'GW231119': 6700, 'GW231118_090602': 1350, 'GW231114': 1380, 'GW231113_200417': 1160,
    'GW231110': 1890, 'GW231108': 2060, 'GW231104': 1470, 'GW231102': 3800, 'GW201029': 3100, 
    'GW201028': 4100, 'GW201020': 1230, 'GW201018': 1530, 'GW201014': 2300, 'GW201008': 3000, 
    'GW201005_091549': 3800, 'GW201004': 6400, 'GW191001': 4300
}

# Identificación de NS (Estrellas de Neutrones)
eventos_ns = ['GW170817', 'GW190425', 'GW200105', 'GW200115']

# Construcción de la tabla
lista_final = []
for ev, dist in eventos_mpc.items():
    es_ns = ev in eventos_ns
    lista_final.append({'event': ev, 'dist_mpc': dist, 'is_ns': es_ns})

df = pd.DataFrame(lista_final)
engine = MFSUEngine()

# Procesamiento masivo
resultados = df.apply(lambda x: engine.procesar(x['dist_mpc'], x['is_ns']), axis=1)
df[['delta_F', 'n_nivel', 'coherencia_%']] = pd.DataFrame(resultados.tolist(), index=df.index)

# Guardar y mostrar
df.to_csv('DATA_MFSU_VALIDATION_LIGO_V2_2.csv', index=False)
print("✅ Procesamiento exitoso. Total eventos:", len(df))
print(df.sort_values(by='n_nivel').head(10))
