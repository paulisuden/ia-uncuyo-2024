import random
import board as b 
import time
import copy

def getNeighbors(board):
    N = len(board)
    neighbors = []
    for col in range(N):
        for row in range(N):
            if row != board[col]:  # evitar que el vecino sea idéntico al estado actual
                neighbor = copy.deepcopy(board)  # hacer una copia profunda del tablero
                neighbor[col] = row  # cambiar la fila de la reina en la columna col a la nueva fila row
                neighbors.append(neighbor)  # añadir el nuevo vecino
    return neighbors

def hillClimbing(board):
    start = time.time()
    current = b.Board(board)
    currentAttacks = current.attacks
    variacionH = []
    variacionH.append(currentAttacks)
    max = 100 
    explored = 0
    while True:
        explored += 1
        neighbors = getNeighbors(current.board)
        if not neighbors:
            end = time.time()
            return currentAttacks, (end-start), explored, variacionH  # no hay vecinos disponibles
        # vecino con el menor número de ataques
        newBoard=min(neighbors, key=b.h)
        neighbor = b.Board(newBoard)
        neighborAttacks = b.h(neighbor.board)   
        variacionH.append(neighborAttacks)
        # si el mejor vecino no mejora el estado actual, hemos alcanzado un máximo local
        if neighborAttacks >= currentAttacks:
            end = time.time()
            return currentAttacks, (end-start), explored, variacionH 
        # mueve al mejor vecino
        current = neighbor
        currentAttacks = neighborAttacks
        if explored == max:
            print("Máximo alcanzado.")
            end = time.time()
            return currentAttacks, (end-start), explored, variacionH

"""attacks, time, iterations, lista = hillClimbing(10)
print("Número de ataques:", attacks)
print("Tiempo empleado:", time, "segundos")
print(iterations)
print(lista)"""
