import numpy as np
from numba import njit

class MFSUQuaternionCore:
    """
    MFSU (Unified Stochastic Fractal Model) - Quaternion Core Solver
    Desarrollado por: Miguel Ángel Franco León
    
    Este motor calcula la rotación galáctica utilizando la métrica fractal 
    D_f = 2.079 y estabilización mediante tensores de rotación cuaterniónica.
    """
    
    def __init__(self):
        # Constantes Maestras MFSU
        self.DELTA_F = 0.921
        self.D_F = 3 - self.DELTA_F  # 2.079
        self.CHI = 5.85              # Factor de empaquetamiento de flujo
        self.G = 4.30091e-6          # Constante gravitacional (unidades galácticas)

    @staticmethod
    @njit(fastmath=True)
    def _quaternion_transform(force_vector, delta_f):
        """
        Aplica una rotación intrínseca al vector de fuerza basada en 
        la vorticidad del espacio fractal.
        """
        # Representación simplificada del operador de rotación q * F * q^-1
        # La parte imaginaria del cuaternión absorbe el déficit dimensional
        vorticidad = np.sqrt(1 + delta_f**2)
        return force_vector * vorticidad

    def solve_velocity(self, mass_barionic, radius_kpc):
        """
        Calcula la velocidad de rotación (km/s) para una masa y radio dados.
        Sustituye la necesidad de materia oscura mediante la métrica MFSU.
        """
        if radius_kpc <= 0:
            return 0.0
            
        # 1. Cálculo de la Permitividad Fractal (ε_f)
        # Basado en la Ley de Gauss Fractal para D_f = 2.079
        epsilon_f = (self.D_F - 1)**self.DELTA_F
        
        # 2. Aceleración Base MFSU (Flujo en superficie de Hausdorff)
        # g = (G * M / r^(D_f-1)) / (ε_f * χ)
        accel_base = (self.G * mass_barionic) / (radius_kpc**(self.D_F - 1))
        
        # 3. Aplicación de la Normalización Geométrica y Torsión
        # El factor CHI (5.85) corrige el empaquetamiento en los huecos del fractal
        accel_final = (accel_base / (epsilon_f * self.CHI))
        
        # 4. Estabilización Cuaterniónica (Simulada para escalares de rotación)
        accel_stabilized = self._quaternion_transform(accel_final, self.DELTA_F)
        
        # 5. Conversión a Velocidad Orbital: v = sqrt(a * r)
        velocity = np.sqrt(accel_stabilized * radius_kpc)
        
        return velocity

    def generate_curve(self, mass, r_min=1.0, r_max=40.0, points=100):
        """
        Genera una serie de datos (radios, velocidades) para graficar.
        """
        radii = np.linspace(r_min, r_max, points)
        velocities = np.array([self.solve_velocity(mass, r) for r in radii])
        return radii, velocities

# Ejemplo de uso:
if __name__ == "__main__":
    solver = MFSUQuaternionCore()
    # Caso SPARC típico (Masa visible ~ 4e10)
    r, v = solver.generate_curve(mass=4.2e10)
    print(f"MFSU Core Cargado. Velocidad en 20kpc: {solver.solve_velocity(4.2e10, 20):.2f} km/s")
