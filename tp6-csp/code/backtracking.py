import time

def busqueda_con_vuelta_atras(n):
    start = time.time()
    estados = 0
    solucion, estados = vuelta_atras_recursiva([], n, estados)
    end = time.time()
    final_time = end - start
    return solucion, estados, final_time

def vuelta_atras_recursiva(asignacion, n, estados):
    estados += 1
    if len(asignacion) == n:
        return asignacion, estados
    
    fila = selecciona_variable_mas_restringida(asignacion, n)
    if fila is None:
        return "fallo", estados

    for columna in range(n):
        if es_consistente(fila, columna, asignacion):
            asignacion.append(columna)
            resultado, estados = vuelta_atras_recursiva(asignacion, n, estados)
            if resultado != "fallo":
                return resultado, estados
            asignacion.pop()
    
    return "fallo", estados

def selecciona_variable_mas_restringida(asignacion, n):
    mejor_fila = None
    menor_numero_de_opciones = float('inf')
    
    for fila in range(n):
        if fila in range(len(asignacion)):
            continue
        
        num_opciones_validas = 0
        for columna in range(n):
            if es_consistente(fila, columna, asignacion):
                num_opciones_validas += 1
        
        if num_opciones_validas < menor_numero_de_opciones:
            menor_numero_de_opciones = num_opciones_validas
            mejor_fila = fila
    
    return mejor_fila

def es_consistente(fila, columna, asignacion):
    for fila_existente in range(len(asignacion)):
        columna_existente = asignacion[fila_existente]
        if columna_existente == columna:
            return False
        if abs(columna_existente - columna) == abs(fila_existente - fila):
            return False
    return True
