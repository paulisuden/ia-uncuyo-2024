import numpy as np
import board as b

# establecer una semilla para obtener consistencia
np.random.seed(42)
seeds = []
boards = []
# generar 30 entornos con diferentes semillas
for i in range(30):
    seed = np.random.randint(0, 1000000)
    board = b.createBoard(4)
    seeds.append(seed)
    boards.append(board)
np.save('4reinas.npy', seeds)

seeds = []
boards = []
for i in range(30):
    seed = np.random.randint(0, 1000000)
    board = b.createBoard(8)
    seeds.append(seed)
    boards.append(board)
np.save('8reinas.npy', seeds)

seeds = []
boards = []
for i in range(30):
    seed = np.random.randint(0, 1000000)
    board = b.createBoard(10)
    seeds.append(seed)
    boards.append(board)
np.save('10reinas.npy', seeds)


print("Entornos generados y semillas guardadas.")