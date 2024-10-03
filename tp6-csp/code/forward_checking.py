import time

def busqueda_con_forward_checking(n):
    start = time.time()
    # Iniciar con una asignación vacía (sin reinas ubicadas)
    # Dominio inicial de cada fila
    dominios = [set(range(n)) for _ in range(n)]
    estados = 0
    solucion, estados = forward_checking_recursivo([], n, dominios, estados)
    end = time.time()
    final_time = end - start
    return solucion, estados, final_time

def forward_checking_recursivo(asignacion, n, dominios, estados):
    estados += 1
    # Si la asignación es completa, se han ubicado todas las reinas
    if len(asignacion) == n:
        return asignacion, estados  # Devolver la solución
    
    # Seleccionamos la fila que tiene el menor número de opciones válidas
    fila = selecciona_variable_mas_restringida(asignacion, n, dominios)
    if fila is None:  # Si no hay filas disponibles, retornar "fallo"
        return "fallo", estados
    
    # Intentamos colocar la reina en cada columna posible dentro del dominio
    for columna in list(dominios[fila]):  # Usamos una copia del dominio
        if es_consistente(fila, columna, asignacion):
            # Si es consistente, agregamos la reina a esta columna
            asignacion.append(columna)
            # Guardamos una copia del dominio actual para restaurarlo más tarde
            original_dominio = [d.copy() for d in dominios]

            # Realizar Forward Checking
            if forward_checking(fila, columna, dominios):
                resultado, estados = forward_checking_recursivo(asignacion, n, dominios, estados)
                if resultado != "fallo":
                    return resultado, estados
            
            # Si no se encontró solución, deshacemos la asignación
            asignacion.pop()
            dominios = original_dominio  # Restaurar dominios
    
    return "fallo", estados  # Si no se pudo ubicar ninguna reina correctamente

def forward_checking(fila, columna, dominios):
    # Actualiza los dominios de las filas restantes
    for r in range(fila + 1, len(dominios)):
        if columna in dominios[r]:
            dominios[r].discard(columna)  # Eliminar la columna del dominio

        # Comprobar si el dominio se ha quedado vacío
        if len(dominios[r]) == 0:
            return False  # Fallo, no hay más opciones válidas
    
    return True  # Forward checking exitoso

def selecciona_variable_mas_restringida(asignacion, n, dominios):
    # Para cada fila no asignada, contamos cuántas columnas son válidas
    mejor_fila = None
    menor_numero_de_opciones = float('inf')  # Número de opciones más bajo
    
    for fila in range(n):
        if fila in range(len(asignacion)):  # Ignoramos filas ya asignadas
            continue
        
        # Contamos cuántas columnas son válidas para esta fila
        num_opciones_validas = len(dominios[fila])
        
        # Si esta fila tiene menos opciones que las anteriores, la elegimos
        if num_opciones_validas < menor_numero_de_opciones and num_opciones_validas > 0:
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

"""
# Ejemplo de uso
N = 10  # Para resolver el problema de las 10 reinas
solucion, estados, final_time = busqueda_con_forward_checking(N)

if solucion != "fallo":
    print(f"Solución encontrada: {solucion}")
    print(f"Estados explorados: {estados}")
    print(f"Tiempo total: {final_time:.4f} segundos")
else:
    print("No se encontró solución")
"""