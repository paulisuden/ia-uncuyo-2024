import numpy as np
import board as b

# establecer una semilla para obtener consistencia
np.random.seed(42)

def environments(size, nombre):
    seeds = []
    boards = []
    for i in range(30):
        seed = np.random.randint(0, 1000000)
        board = b.createBoard(size)
        seeds.append(seed)
        boards.append(board)
    np.save(nombre, seeds)

environments(4, '4reinas.npy')
environments(8, '8reinas.npy')
environments(10, '10reinas.npy')
print("Entornos generados y semillas guardadas.")

def geneticEnvironments(size,population,nombre):
    general = []
    for i in range(30):
        boards = []  
        for j in range(population):
            board = b.createBoard(size)
            boards.append(board)
        general.append(boards)
    np.save(nombre, general)  

geneticEnvironments(4, 16, '4reinasGA.npy')
geneticEnvironments(8, 64,  '8reinasGA.npy')
geneticEnvironments(10, 100, '10reinasGA.npy')