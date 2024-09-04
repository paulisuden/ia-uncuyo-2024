import numpy as np
import frozenLake as e  

# establecer una semilla para obtener consistencia
np.random.seed(42)

# generar 30 entornos con diferentes semillas
seeds = []
environments = []

for i in range(30):
    seed = np.random.randint(0, 1000000)
    env = e.Environment(100, 0.08)  # Crear el entorno con la semilla generada
    seeds.append(seed)
    environments.append(env)

# guardar las semillas en un archivo para recrear los entornos después
np.save('seeds.npy', seeds)

print("Entornos generados y semillas guardadas.")
