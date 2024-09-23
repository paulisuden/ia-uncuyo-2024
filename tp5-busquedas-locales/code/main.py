import numpy as np
import simmulatedAnnealing as s
import hillClimbing as h
import board as b
import csv_file as c
import genetic as g


def cargar_info(result, info_list, reina_size, nombre):
    attacks, time, iterations, _ = result
    info = {
        'algorithm_name': nombre,
        'reinas': reina_size,
        'solución óptima': attacks,
        'tiempo ejecución': time,
        'iteraciones': iterations
    }
    info_list.append(info)

def ejecutar_algoritmos(seeds, reina_size, info_list_s, info_list_h):
    for i, seed in enumerate(seeds):
        np.random.seed(seed)  # usar la semilla para recrear el entorno
        board = b.createBoard(reina_size)
        result_sa = s.simulated_annealing(board)
        cargar_info(result_sa, info_list_s, reina_size, 'Simulated Annealing')

        result_hc = h.hillClimbing(board)
        cargar_info(result_hc, info_list_h, reina_size, 'Hill Climbing')
        if i == 10:
            _, _, _, H = result_hc
            variacionH = H
            _, _, _, H = result_sa
            variacionS = H
    return variacionS, variacionH
            

# Cargar las semillas guardadas
reinas4 = np.load('4reinas.npy')
reinas8 = np.load('8reinas.npy')
reinas10 = np.load('10reinas.npy')

info_list4s = []
info_list4h = []
info_list8s = []
info_list8h = []
info_list10s = []
info_list10h = []

variacionS4, variacionH4 = ejecutar_algoritmos(reinas4, 4, info_list4s, info_list4h)
variacionS8, variacionH8 = ejecutar_algoritmos(reinas8, 8, info_list8s, info_list8h)
variacionS, variacionH = ejecutar_algoritmos(reinas10, 10, info_list10s, info_list10h)



#* graficar 
# Calcula las estadísticas para ambos algoritmos
print("4 reinas")
stats_h4 = c.calculate_statistics(info_list4h)
stats_s4 = c.calculate_statistics(info_list4s)
print("8 reinas")
stats_h8 = c.calculate_statistics(info_list8h)
stats_s8 = c.calculate_statistics(info_list8s)
print("10 reinas")
stats_h10 = c.calculate_statistics(info_list10h)
stats_s10 = c.calculate_statistics(info_list10s)

# recoger los datos para graficar
stats_to_ploth1 = {
    'Algoritmo H 4 reinas': stats_h4['tiempos'],
    'Algoritmo H 8 reinas': stats_h8['tiempos'],
    'Algoritmo H 10 reinas': stats_h10['tiempos']
}

stats_to_plots1 = {
    'Algoritmo S 4 reinas': stats_s4['tiempos'],
    'Algoritmo S 8 reinas': stats_s8['tiempos'],
    'Algoritmo S 10 reinas': stats_s10['tiempos']
}


stats_to_ploth2 = {
    'Algoritmo H 4 reinas': stats_h4['iteraciones'],
    'Algoritmo H 8 reinas': stats_h8['iteraciones'],
    'Algoritmo H 10 reinas': stats_h10['iteraciones']
}

stats_to_plots2 = {
    'Algoritmo S 4 reinas': stats_s4['iteraciones'],
    'Algoritmo S 8 reinas': stats_s8['iteraciones'],
    'Algoritmo S 10 reinas': stats_s10['iteraciones']
}



# Graficar
c.boxplot(stats_to_ploth1, 'Tiempos de ejecución hill climbing')
c.boxplot(stats_to_plots1, 'Tiempos de ejecución simmulating')
c.boxplot(stats_to_ploth2, 'Iteraciones hill climbing')
c.boxplot(stats_to_plots2, 'Iteraciones simmulating')


#* GRAFICAR CURVAS

c.graficar_historial_h(variacionH, variacionS, 'H() 10 reinas', 'Hill climbing', 'Simmulated Annealing')
c.graficar_historial_h(variacionH4, variacionS4, 'H() 4 reinas', 'Hill climbing', 'Simmulated Annealing')
c.graficar_historial_h(variacionH8, variacionS8, 'H() 8 reinas', 'Hill climbing', 'Simmulated Annealing')




#* GENETICOS

def ejecutarAG(dates, size, results, iValue):
    long = len(dates)
    for i in range (long):
        lista = dates[i]
        result = g.genetics(lista)
        cargar_info(result, results, size, 'GA')
        if i == iValue:
            _, _, _, H = result
    return H


lista4 = []
lista8 = []
lista10 = []

def population_as_lists(lista):
    return [individual.tolist() for individual in lista]

##################################

arrays = np.load('10reinasGA.npy', allow_pickle=True)
data = population_as_lists(arrays)
variacion10 = ejecutarAG(data, 10, lista10, 15)
statsGA = c.calculate_statistics(lista10)

#################################

arrays = np.load('8reinasGA.npy', allow_pickle=True)
data = population_as_lists(arrays)
variacion8 = ejecutarAG(data, 8, lista8, 15)
statsGA8 = c.calculate_statistics(lista8)


###################################

arrays = np.load('4reinasGA.npy', allow_pickle=True)
data = population_as_lists(arrays)
variacion = ejecutarAG(data, 4, lista4, 15)
statsGA4 = c.calculate_statistics(lista4)

c.graficar_historial_h(variacion8, variacion10, 'Variación H()', 'H() 8 reinas GA', 'H() 10 reinas GA')


graficarT = {
    'Algoritmo G 10 reinas': statsGA['tiempos'],
    'Algoritmo G 8 reinas': statsGA8['tiempos'],
    'Algoritmo G 4 reinas': statsGA4['tiempos']
}

graficarI = {
    'Algoritmo G 10 reinas': statsGA['iteraciones'],
    'Algoritmo G 8 reinas': statsGA8['iteraciones'],
    'Algoritmo G 4 reinas': statsGA4['iteraciones']
}

c.boxplot(graficarT, 'Tiempos alg. genético')
c.boxplot(graficarI, 'Iteraciones alg. genético')

c.save_csv(info_list10s, info_list8s, info_list4s, "simulated_annealing_results.csv")
c.save_csv(info_list10h, info_list8h, info_list4h, "hill_climbing_results.csv")
c.save_csv(lista4, lista8, lista10, "genetic_algorithm_results.csv")
print("Resultados guardados en CSV.")