import csv
import matplotlib.pyplot as plt
import numpy as np


def save_csv(results):
    # Definir los encabezados del archivo CSV
    headers = ["algorithm_name", "env_n", "states_n", "cost_e1", "cost_e2", "time", "solution_found"]

    # Crear el archivo CSV y escribir los encabezados
    with open("no-informada-results.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)

    # Escribir los datos en el archivo CSV
    with open("no-informada-results.csv", "a", newline='') as f:
        writer = csv.writer(f)
        # Convertir cada diccionario en una lista de valores en el orden de los encabezados
        writer.writerows([[result[header] for header in headers] for result in results])

    print(f'Archivo no-informada-results.csv creado con éxito.')
    



def calculate_statistics(results):
    # Filtrar resultados donde se encontró una solución (found = True)
    filtered_results = [res for res in results if res['solution_found']]
    
    # Diccionarios para almacenar las estadísticas por algoritmo
    stats = {
        'states_explored': {},
        'cost_e1': {},
        'cost_e2': {},
        'time': {}
    }
    
    for res in filtered_results:
        algorithm_name = res['algorithm_name']
        
        if algorithm_name not in stats['states_explored']:
            stats['states_explored'][algorithm_name] = []
            stats['cost_e1'][algorithm_name] = []
            stats['cost_e2'][algorithm_name] = []
            stats['time'][algorithm_name] = []
        
        # Agregar valores a las listas correspondientes
        stats['states_explored'][algorithm_name].append(res['states_n'])
        stats['cost_e1'][algorithm_name].append(res['cost_e1'])
        stats['cost_e2'][algorithm_name].append(res['cost_e2'])
        stats['time'][algorithm_name].append(res['time'])
    
    # Calcular media y desviación estándar
    for key in stats:
        for algorithm_name in stats[key]:
            data = np.array(stats[key][algorithm_name])
            mean = np.mean(data)
            std_dev = np.std(data)
            print(f"{algorithm_name} - {key} -> Media: {mean:.2f}, Desviación estándar: {std_dev:.2f}")
    
    return stats


def boxplot(stats, metric):
    # Extraer etiquetas y datos para graficar
    labels = list(stats.keys())
    data = [stats[label] for label in labels]
    
    # Crear el gráfico de cajas y bigotes
    fig, ax = plt.subplots()
    bplot = ax.boxplot(data, vert=True, labels=labels, patch_artist=True)
    ax.set_title(f'Comparación de {metric}')
    ax.set_ylabel(metric.capitalize())
    ax.set_xlabel('Algoritmo')
    ax.yaxis.grid(True)

    """# Colores para las cajas
    colors = ['lightgreen', 'lightblue', 'pink', 'lightgrey']
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)"""

    plt.savefig(f'{metric}_boxplot.png')
    plt.show()


