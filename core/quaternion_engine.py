import numpy as np

class QuaternionMFSU:
    def __init__(self, delta_F=0.921):
        self.delta_F = delta_F # Parte real (Escalar de coherencia)
        # El vector (i, j, k) representa la tortuosidad en las 3 dimensiones
        self.chi = 5.85
        
    def get_dimensional_quaternion(self, n):
        """
        Calcula el cuaternión de estado para la generación n.
        Representa la rotación del flujo a través del fractal.
        """
        # La reducción actúa como una rotación hacia el eje imaginario (caos/dispersión)
        theta = np.arccos(self.delta_F) * (1 - (5e-5)**n)
        
        # q = cos(theta) + u*sin(theta)
        q_real = np.cos(theta)
        q_imag = np.sin(theta) / np.sqrt(3) # Distribuido en i, j, k
        
        return np.array([q_real, q_imag, q_imag, q_imag])

    def apply_reduction(self, vector, n):
        """
        Aplica la rotación de la Ley de Reducción a un vector de fuerza/velocidad.
        """
        q = self.get_dimensional_quaternion(n)
        # Aquí se realizaría la multiplicación de cuaterniones qvq*
        # Esto ajusta la magnitud y dirección basado en la porosidad geométrica
        return vector * (self.delta_F**(n*1e-5)) # Versión simplificada para el test
