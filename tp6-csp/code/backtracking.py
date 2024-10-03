import time

def busqueda_con_vuelta_atras(n):
    start = time.time()
    # Iniciar con una asignación vacía (sin reinas ubicadas)
    estados = 0
    solucion, estados = vuelta_atras_recursiva([], n, estados)
    end = time.time()
    final_time = end-start
    return solucion, estados, final_time

def vuelta_atras_recursiva(asignacion, n, estados):
    estados += 1
    # Si la asignación es completa, se han ubicado todas las reinas
    if len(asignacion) == n:
        return asignacion, estados  # Devolver la solución
    
    # Seleccionamos la fila que tiene el menor número de opciones válidas
    fila = selecciona_variable_mas_restringida(asignacion, n)
    if fila is None:  # Si no hay filas disponibles, retornar "fallo"
        return "fallo", estados

    # Intentamos colocar la reina en cada columna posible
    for columna in range(n):
        if es_consistente(fila, columna, asignacion):
            # Si es consistente, agregamos la reina a esta columna
            asignacion.append(columna)
            # Llamada recursiva para intentar ubicar la siguiente reina
            resultado, estados = vuelta_atras_recursiva(asignacion, n, estados)
            if resultado != "fallo":
                return resultado, estados
            # Si no se encontró una solución, deshacemos la asignación
            asignacion.pop()
    
    return "fallo", estados  # Si no se pudo ubicar ninguna reina correctamente

def selecciona_variable_mas_restringida(asignacion, n):
    mejor_fila = None
    menor_numero_de_opciones = float('inf')  # Número de opciones más bajo
    
    for fila in range(n):
        if fila in range(len(asignacion)):  # Ignoramos filas ya asignadas
            continue
        
        # Contamos cuántas columnas son válidas para esta fila
        num_opciones_validas = 0
        for columna in range(n):
            if es_consistente(fila, columna, asignacion):
                num_opciones_validas += 1
        
        # Si esta fila tiene menos opciones que las anteriores, la elegimos
        if num_opciones_validas < menor_numero_de_opciones:
            menor_numero_de_opciones = num_opciones_validas
            mejor_fila = fila
    
    return mejor_fila

def es_consistente(fila, columna, asignacion):
    # Verificar si la colocación es válida (sin conflictos)
    for fila_existente in range(len(asignacion)):
        columna_existente = asignacion[fila_existente]
        
        # Chequear si hay conflictos en la misma columna
        if columna_existente == columna:
            return False
        
        # Chequear si están en la misma diagonal
        if abs(columna_existente - columna) == abs(fila_existente - fila):
            return False
    
    # Si pasa todas las verificaciones, es consistente
    return True

"""# Ejemplo de uso
N = 8  # Para resolver el problema de las 8 reinas
solucion, estados, final_time = busqueda_con_vuelta_atras(N)
if solucion != "fallo":
    print(f"Solución encontrada: {solucion}")
    print(f"Estados explorados: {estados}")
    print(f"Tiempo total: {final_time:.4f} segundos")
else:
    print("No se encontró solución")
"""