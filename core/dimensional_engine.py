import numpy as np

class DimensionalQuaternionEngine:
    """
    Motor Cuaterniónico de la Ley de Reducción Dimensional.
    Modela el vacío como un medio poroso con rotación de fase geométrica.
    """
    def __init__(self):
        self.delta_F0 = 0.921   # Semilla Primordial (Parte Real)
        self.chi = 5.85          # Impedancia (Magnitud Compleja)
        self.tau = 2.221         # Tortuosidad (Eje Vectorial)
        self.Rf = 5.03e-5        # Constante de Ramificación

    def get_coherence_quaternion(self, n):
        """
        Calcula el estado del vacío en la generación 'n'.
        El resultado es un cuaternión q = [w, x, y, z]
        donde 'w' es la coherencia escalar y [x,y,z] es la dispersión fractal.
        """
        # La coherencia decae según la Ley de Reducción
        df_n = self.delta_F0 * (1 - self.Rf)**n
        
        # El ángulo de fase representa la desviación de la "rectitud" euclidiana
        # A mayor n, más rotación hacia la parte imaginaria (caos/entropía fractal)
        angle = np.arccos(df_n)
        
        # Distribución de la tortuosidad en los ejes i, j, k
        # Representa cómo la energía se "pierde" en los poros del fractal
        axis = np.array([1, 1, 1]) / np.sqrt(3) # Vector unitario de tortuosidad
        
        w = np.cos(angle / 2)
        xyz = axis * np.sin(angle / 2)
        
        return np.array([w, xyz[0], xyz[1], xyz[2]])

    def apply_geometry_to_force(self, force_vector, n):
        """
        Corrige un vector de fuerza (o velocidad) usando la rotación del vacío.
        q * v * q_inv
        """
        q = self.get_coherence_quaternion(n)
        # Aquí la gravedad se 'estira' o 'concentra' por la impedancia chi
        coherence_factor = q[0] # Parte real
        return force_vector * (self.chi**(1 - coherence_factor))
