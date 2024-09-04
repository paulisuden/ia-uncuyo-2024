import numpy as np

def create_matrix(filas, columnas, proporcion):
    # Calcular la cantidad de 1s y 0s
    total_casilleros = filas * columnas
    hole_amount = int(total_casilleros * proporcion)
    frozen_amount = total_casilleros - hole_amount

    # Crear la matriz con la cantidad adecuada de 1s y 0s
    matriz = np.array(['H'] * hole_amount + ['F'] * frozen_amount)

    # Mezclar la matriz para distribuir aleatoriamente los 1s y 0s
    np.random.shuffle(matriz)

    # Redimensionar la matriz a la forma deseada
    matriz = matriz.reshape(filas, columnas)

    return matriz
