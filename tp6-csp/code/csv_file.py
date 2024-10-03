import csv
import matplotlib.pyplot as plt
import numpy as np


import csv

def save_csv(results_4, results_8, results_10, name):
    # Definir los encabezados del archivo CSV
    headers = ["algorithm_name", "reinas", "solución óptima", "tiempo ejecución", "iteraciones"]

    # Crear el archivo CSV y escribir los encabezados
    with open(name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)

    # Combinar los resultados de las tres listas
    combined_results = results_4 + results_8 + results_10

    # Escribir los datos en el archivo CSV
    with open(name, "a", newline='') as f:
        writer = csv.writer(f)
        # Convertir cada diccionario en una lista de valores en el orden de los encabezados
        writer.writerows([[result[header] for header in headers] for result in combined_results])

    print("Archivo ", name, "creado con éxito.")




def calculate_statistics(resultados):
    attacks_list = [result['solución óptima'] for result in resultados]
    time_list = [result['tiempo ejecución'] for result in resultados]
    iterations_list = [result['iteraciones'] for result in resultados]

    # porcentaje de veces que se llega a un estado de solución óptima (attacks == 0)
    optimo_count = sum(1 for attack in attacks_list if attack != "fallo")
    porcentaje_optimo = (optimo_count / len(attacks_list)) #*100

    # tiempo de ejecución promedio
    tiempo_promedio = np.mean(time_list)

    # iteraciones promedio
    iteraciones_promedio = np.mean(iterations_list)

    # desviación estándar del tiempo y de las iteraciones
    desviacion_tiempo = np.std(time_list)
    desviacion_iteraciones = np.std(iterations_list)

    algorithm_name = resultados[0]['algorithm_name'] if resultados else 'Desconocido'

    print(f"Algoritmo: {algorithm_name}")   
    print(f"Porcentaje de soluciones óptimas: {porcentaje_optimo:.2f}")
    print(f"Tiempo de ejecución promedio: {tiempo_promedio:.4f} segundos")
    print(f"Iteraciones promedio: {iteraciones_promedio:.2f}")
    print(f"Desviación estándar del tiempo de ejecución: {desviacion_tiempo:.4f} segundos")
    print(f"Desviación estándar de las iteraciones: {desviacion_iteraciones:.2f}")

    # Devolver tiempos de ejecución e iteraciones para graficar
    return {
        'tiempos': time_list,
        'iteraciones': iterations_list,
        'solución óptima': attacks_list
    }



def boxplot(stats, metric):
    # Extraer etiquetas y datos para graficar
    labels = list(stats.keys())
    data = [stats[label] for label in labels]
    
    # Crear el gráfico de cajas y bigotes
    fig, ax = plt.subplots()
    bplot = ax.boxplot(data, vert=True, labels=labels, patch_artist=True)
    ax.set_title(f'Comparación para {metric}')
    ax.set_ylabel(metric.capitalize())
    ax.set_xlabel(stats)
    ax.yaxis.grid(True)

    colors = ['lightgreen', 'lightblue', 'pink', 'lightgrey']
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    plt.savefig(f'{metric}_boxplot.png')

def graficar_historial_h(lista1, lista2, nombre_archivo, nombre_curva1, nombre_curva2):

    plt.figure(figsize=(12, 8))
    
    # Graficar la primera lista
    plt.plot(lista1, marker='o', label=nombre_curva1)
    
    # Graficar la segunda lista
    plt.plot(lista2, marker='s', label=nombre_curva2)
    
    # Título del gráfico
    plt.title(nombre_archivo, fontsize=18)
    
    # Etiquetas de los ejes
    plt.xlabel('Iteraciones', fontsize=14)
    plt.ylabel('Pares de reinas amenazadas', fontsize=14)
    
    # Mostrar la cuadrícula
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Mostrar la leyenda
    plt.legend(fontsize=12)
    
    # Guardar la gráfica como archivo PNG
    #plt.savefig(nombre_archivo, format='png', dpi=300)
    plt.savefig(f'{nombre_archivo}_boxplot.png')

    #plt.show()