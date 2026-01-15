import numpy as np

class DimensionalReductionLaw:
    """
    Motor matemático de la Ley de Reducción Dimensional (MFSU).
    Deriva la pérdida de coherencia cósmica a partir de la geometría del vacío.
    """
    def __init__(self):
        # Constantes Geométricas Fundamentales
        self.delta_F_0 = 0.921        # Semilla primordial (Coherencia n=0)
        self.D_f = 3 - self.delta_F_0 # Dimensión de Hausdorff (2.079)
        self.chi = 5.85               # Impedancia Topológica del vacío
        self.tau = 2.221               # Factor de Tortuosidad (medio poroso)
        
        # Dimensión de Interacción (Complejidad del camino fractal)
        self.alpha = self.D_f + self.tau 
        
        # Derivación de la Constante de Ramificación (Rf)
        # Rf = (Defecto Dimensional) / (Resistencia del Vacío ^ Complejidad)
        self.Rf = (1 - self.delta_F_0) / (self.chi ** self.alpha)

    def get_coherence(self, n):
        """
        Calcula la coherencia delta_F para una generación 'n' dada.
        n=0 es el tronco original (máxima coherencia).
        """
        return self.delta_F_0 * (1 - self.Rf)**n

    def get_acceleration_factor(self, n):
        """
        Calcula el factor de corrección gravitacional basado en la coherencia.
        Útil para simulaciones de curvas de rotación galáctica.
        """
        delta_n = self.get_coherence(n)
        return (self.D_f - 1)**delta_n


