import random
import numpy as np

class Board:
    def __init__(self, board):
        if isinstance(board, int):  # si se pasa un entero, crear el tablero
            self.board = createBoard(board)
        else: 
            self.board = board
            
        self.representation = representation(self)
        self.attacks = h(self.board)
    
    def printBoard(self):
        for fila in self.representation:
            print(' '.join(fila))
    
def h(board):
    N = len(board)
    attacks = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def createBoard(size):
    return np.random.permutation(size)

def representation(self):
    size = len(self.board)
    matriz = [['0' for _ in range(size)] for _ in range(size)]
    
    for col in range(size):
        row = self.board[col]
        matriz[row][col] = 'R'  
    
    return matriz



