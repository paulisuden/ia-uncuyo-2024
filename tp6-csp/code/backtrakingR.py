import random

def es_consistente(fila, columna, asignacion):
    """Verifica si la reina en (fila, columna) no ataca a las reinas en la asignación."""
    for r, c in enumerate(asignacion):
        if c == columna or abs(r - fila) == abs(c - columna):
            return False
    return True

def mrv(asignacion, n):
    """Selecciona la fila con el menor número de valores restantes (Minimum Remaining Values)."""
    fila_mas_restringida = -1
    menor_tamano_dominio = n + 1  # Inicializar con un valor mayor que n
    
    # Iterar sobre las filas ya asignadas para determinar la fila más restringida
    for fila in range(n):
        if fila not in asignacion:  # Si la fila no está asignada
            # Contar el número de valores disponibles para esta fila
            opciones_disponibles = sum(1 for col in range(n) if es_consistente(fila, col, asignacion))
            if opciones_disponibles < menor_tamano_dominio:
                menor_tamano_dominio = opciones_disponibles
                fila_mas_restringida = fila

    return fila_mas_restringida

def vuelta_atras_recursiva(asignacion, n):
    if len(asignacion) == n:
        return asignacion  # Solución completa encontrada

    fila = mrv(asignacion, n)  # Selecciona la fila con MRV

    # Crear una lista de columnas y barajarla aleatoriamente
    columnas = list(range(n))
    random.shuffle(columnas)  # Barajar las columnas
    
    # Intentamos colocar la reina en cada columna posible (en orden aleatorio)
    for columna in columnas:
        if es_consistente(fila, columna, asignacion):
            asignacion.append(columna)  # Hacemos una asignación (decisión)
            resultado = vuelta_atras_recursiva(asignacion, n)  # Llamada recursiva
            if resultado != "fallo":
                return resultado  # Solución encontrada
            asignacion.pop()  # Retrocedemos
    return "fallo"  # No se encontró solución para esta rama

def buscar_solucion(n):
    """Función principal que inicia la búsqueda de solución para N reinas."""
    # Seleccionar una fila aleatoria para la primera columna
    primera_fila = random.randint(0, n - 1)
    asignacion = [primera_fila]  # Colocar la reina en la fila seleccionada en la primera columna

    return vuelta_atras_recursiva(asignacion, n)

# Ejemplo de uso
n = 12
solucion = buscar_solucion(n)
print(f"Solución encontrada para {n} reinas: {solucion}")
