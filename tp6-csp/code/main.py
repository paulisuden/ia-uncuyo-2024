import numpy as np
import backtracking as b
import forward_checking as f
import csv_file as c



def cargar_info(result, info_list, reina_size, nombre):
    solucion, estados, final_time = result
    info = {
        'algorithm_name': nombre,
        'reinas': reina_size,
        'solución óptima': solucion,
        'tiempo ejecución': final_time,
        'iteraciones': estados
    }
    info_list.append(info)

def ejecutar_algoritmos(reina_size, info_list_f, info_list_b):
    for i in range(30):
        resultado = b.busqueda_con_vuelta_atras(reina_size)
        cargar_info(resultado,info_list_b, reina_size, 'Backtraking')
        resultado = f.busqueda_con_forward_checking(reina_size)
        cargar_info(resultado,info_list_f, reina_size, 'Forward checking')




info_list4f = []
info_list4b = []
info_list8f = []
info_list8b = []
info_list10f = []
info_list10b = []

ejecutar_algoritmos(4, info_list4f, info_list4b)
ejecutar_algoritmos(8, info_list8f, info_list8b)
ejecutar_algoritmos(10, info_list10f, info_list10b)


# Calcula las estadísticas para ambos algoritmos
print("4 reinas")
stats_f4 = c.calculate_statistics(info_list4f)
stats_b4 = c.calculate_statistics(info_list4b)
print("8 reinas")
stats_f8 = c.calculate_statistics(info_list8f)
stats_b8 = c.calculate_statistics(info_list8b)
print("10 reinas")
stats_f10 = c.calculate_statistics(info_list10f)
stats_b10 = c.calculate_statistics(info_list10b)

# recoger los datos para graficar
stats_to_ploth1 = {
    'Algoritmo FC 4 reinas': stats_f4['tiempos'],
    'Algoritmo FC 8 reinas': stats_f8['tiempos'],
    'Algoritmo FC 10 reinas': stats_f10['tiempos']
}

stats_to_plots1 = {
    'Algoritmo B 4 reinas': stats_b4['tiempos'],
    'Algoritmo B 8 reinas': stats_b8['tiempos'],
    'Algoritmo B 10 reinas': stats_b10['tiempos']
}

# Graficar
c.boxplot(stats_to_ploth1, 'Tiempos de ejecución FORWARD CHECKING')
c.boxplot(stats_to_plots1, 'Tiempos de ejecución BACKTRACKING')


"""info_list4b.extend(info_list4f)
info_list8b.extend(info_list8f)
info_list10b.extend(info_list10f)

c.save_csv(info_list4b, info_list8b, info_list10b, " tp6-Nreinas.csv")
print("Resultados guardados en CSV.")"""