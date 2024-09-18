import numpy as np
import random
import math
import time
import board as b 
import copy

def randomNeighbor(board):
    #neighbor = np.random.permutation(board)   # --> OTRA FORMA DE PERMUTAR TODAS LAS REINAS DE LUGAR
    #* cambia la posición de una reina aleatoriamente
    neighbor = board.copy()
    i, j = random.sample(range(len(board)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def simulated_annealing(board):
    T = 1000 #initial temp
    alfa = 0.95 
    max_iterations = 1000
    current = b.Board(board)
    best_board = copy.copy(current) #aca se van a ir guardando las "mejores" opciones de tablero
    iteration = 0
    variacionH = []
    variacionH.append(current.attacks)
    start = time.time()

    while iteration < max_iterations and T > 1e-10 and best_board.attacks != 0:
        newBoard = randomNeighbor(current.board)  #creo el tablero random
        neighbor = b.Board(newBoard) #creo un nuevo objeto Board 
        variacionH.append(neighbor.attacks)
        E = neighbor.attacks - current.attacks #calculo delta E

        if E < 0 or random.uniform(0, 1) < math.exp(-E / T):
            current = neighbor
            if current.attacks < best_board.attacks:
                best_board = copy.copy(current)   

        T *= alfa
        iteration += 1

    end= time.time()
    finalTime = end - start
    return best_board.attacks, finalTime, iteration, variacionH

"""ataque, time, states_evaluated = simulated_annealing(8)
print("ataque:", ataque)
print("Número de estados evaluados:", states_evaluated)
print("Tiempo empleado:", time)"""

#! T = 584