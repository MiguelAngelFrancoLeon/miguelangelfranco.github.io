from core.reduction_law import DimensionalReductionLaw

def run_simulation():
    engine = DimensionalReductionLaw()
    
    print("--- Simulación MFSU: Ley de Reducción Dimensional ---")
    print(f"Semilla: {engine.delta_F_0} | Impedancia: {engine.chi}")
    print(f"Rf Calculado: {engine.Rf:.8e}\n")
    
    generations = [0, 100, 1000, 5000, 10000, 20000]
    
    print(f"{'Generación (n)':<15} | {'Coherencia (delta_F)':<20} | {'Estado'}")
    print("-" * 55)
    
    for n in generations:
        df = engine.get_coherence(n)
        estado = "Primordial" if n == 0 else "Evolución"
        if n == 20000: estado = "Universo Local (Actual)"
        
        print(f"{n:<15} | {df:<20.5f} | {estado}")

if __name__ == "__main__":
    run_simulation()
