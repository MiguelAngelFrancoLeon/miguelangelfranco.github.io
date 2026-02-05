import numpy as np
import math

# --- CONSTANTES DEL MODELO MFSU ---
CHI = 12.65          # Impedancia Topológica (Newton-Gregory / Rugosidad)
DELTA_F_BASE = 0.921 # Tallo Primordial (Semilla)
SIGMA = 0.02         # Fluctuación de Franco (Vibración del contenedor)

def calcular_velocidad_mfsu(v_bar, tipo_galaxia="tallo"):
    """
    Calcula la velocidad predicha usando la Ecuación Maestra Dinámica.
    V_pred = V_bar * sqrt(1 + CHI * (1 - delta_F))
    """
    
    # 1. Determinar el Nivel de Ramificación (delta_F)
    # En el modelo completo, esto depende de los parámetros beta, alpha, gamma.
    # Aquí simplificamos seleccionando el "escalón" del fractal.
    
    if tipo_galaxia == "tallo":
        # Galaxias masivas estables (N=0)
        delta_f = DELTA_F_BASE  # 0.921
    elif tipo_galaxia == "rama_1":
        # Galaxias espirales típicas o corrientes estelares (N=1)
        # Aproximación: delta_f decae por la dimensión fractal
        delta_f = 0.548 
    elif tipo_galaxia == "rama_2":
        # Galaxias enanas o LSB (Low Surface Brightness) (N=2)
        # Aquí la impedancia domina, delta_f es bajo.
        delta_f = 0.315
    else:
        # Por defecto, usamos el Tallo
        delta_f = DELTA_F_BASE

    # 2. Aplicar la Ecuación Maestra (La fórmula del Libro)
    # Factor de Amplificación = Raíz Cuadrada de la Impedancia efectiva
    impedancia_efectiva = 1 + CHI * (1 - delta_f)
    factor_amplificacion = math.sqrt(impedancia_efectiva)
    
    # 3. Velocidad Final
    v_pred = v_bar * factor_amplificacion
    
    return v_pred, delta_f, factor_amplificacion

# --- SIMULACIÓN DE DATOS (Ejemplo SPARC) ---
# Datos ficticios basados en perfiles reales para probar el motor

print(f"{'GALAXIA':<15} | {'V_BAR (km/s)':<12} | {'TIPO':<10} | {'DELTA_F':<8} | {'FACTOR':<8} | {'V_MFSU (km/s)':<15}")
print("-" * 85)

datos_prueba = [
    ("Masiva A", 200, "tallo"),    # Galaxia grande, mucha materia bariónica
    ("Espiral B", 150, "rama_1"),  # Galaxia media, necesita empuje
    ("Enana C", 50, "rama_2")      # Galaxia enana, necesita MUCHO empuje
]

for nombre, v_bar, tipo in datos_prueba:
    v_final, df_usado, factor = calcular_velocidad_mfsu(v_bar, tipo)
    
    print(f"{nombre:<15} | {v_bar:<12} | {tipo:<10} | {df_usado:<8.3f} | {factor:<8.3f} | {v_final:<15.2f}")

# --- VALIDACIÓN INVERSA (Lo que pedía el crítico) ---
# Si tenemos V_obs (dato real) y V_bar, ¿recuperamos el delta_F correcto?
print("\n--- PRUEBA INVERSA (Recuperando el ADN Fractal) ---")
v_obs_real_enana = 118.5  # Supongamos que Gaia/SPARC ve esto para la Enana C
v_bar_enana = 50.0

# Fórmula inversa del Cap 3: delta_F = 1 - [((V_obs/V_bar)^2 - 1) / CHI]
ratio_sq = (v_obs_real_enana / v_bar_enana)**2
delta_f_calculado = 1 - ((ratio_sq - 1) / CHI)

print(f"Observado: {v_obs_real_enana} km/s | Bariónico: {v_bar_enana} km/s")
print(f"Delta_F Recuperado: {delta_f_calculado:.3f}")
if abs(delta_f_calculado - 0.315) < 0.1:
    print(">> RESULTADO: La galaxia está confirmada en la RAMA 2.")
