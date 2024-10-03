import time

def busqueda_con_forward_checking(n):
    start = time.time()
    dominios = [set(range(n)) for _ in range(n)]
    estados = 0
    solucion, estados = forward_checking_recursivo([], n, dominios, estados)
    end = time.time()
    final_time = end - start
    return solucion, estados, final_time

def forward_checking_recursivo(asignacion, n, dominios, estados):
    estados += 1
    if len(asignacion) == n:
        return asignacion, estados
    
    fila = selecciona_variable_mas_restringida(asignacion, n, dominios)
    if fila is None:
        return "fallo", estados
    
    for columna in list(dominios[fila]):
        if es_consistente(fila, columna, asignacion):
            asignacion.append(columna)
            original_dominio = [d.copy() for d in dominios]

            if forward_checking(fila, columna, dominios):
                resultado, estados = forward_checking_recursivo(asignacion, n, dominios, estados)
                if resultado != "fallo":
                    return resultado, estados
            
            asignacion.pop()
            dominios = original_dominio
    
    return "fallo", estados

def forward_checking(fila, columna, dominios):
    for r in range(fila + 1, len(dominios)):
        if columna in dominios[r]:
            dominios[r].discard(columna)
        if len(dominios[r]) == 0:
            return False
    return True

def selecciona_variable_mas_restringida(asignacion, n, dominios):
    mejor_fila = None
    menor_numero_de_opciones = float('inf')
    
    for fila in range(n):
        if fila in range(len(asignacion)):
            continue
        num_opciones_validas = len(dominios[fila])
        if num_opciones_validas < menor_numero_de_opciones and num_opciones_validas > 0:
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
