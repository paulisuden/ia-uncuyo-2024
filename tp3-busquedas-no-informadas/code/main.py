import numpy as np
import frozenLake as e  # Asegúrate de que este módulo contenga tu clase `Environment`
import a_star as a
import bfs as b
import dfs as d
import dfs_limited as dl
import ucs  as u 
import csv_file as c
import random_ as r

# Cargar las semillas guardadas
seeds = np.load('seeds.npy')
info_list = []

def cargar_info(result, info_list):
    path, moves, explored_amount, first_cost, second_cost, final_time, found, nombre = result
    info = {
        'algorithm_name': nombre,
        'env_n': i,
        'states_n': explored_amount,
        'cost_e1': first_cost,
        'cost_e2': second_cost,
        'time': final_time,
        'solution_found': found
    }
    info_list.append(info)

# Ejecutar algoritmos en los 30 entornos
for i, seed in enumerate(seeds):
    env = e.Environment(100, 0.08)  # Crear el entorno con el mismo tamaño y probabilidad
    np.random.seed(seed)  # Usar la semilla para recrear el entorno exactamente igual
    
    result = b.bfs(env)
    cargar_info(result, info_list)
    result = d.dfs(env)
    cargar_info(result, info_list)
    result = u.ucs(env)
    cargar_info(result, info_list)
    result = a.a_star(env, env.final_state)
    cargar_info(result, info_list)
    result = dl.dfs_limited(env)
    cargar_info(result, info_list)
    result = r.randomm(env)
    cargar_info(result, info_list)

c.save_csv(info_list)

# calcular estadísticas
stats = c.calculate_statistics(info_list)

# graficar 
c.boxplot(stats['states_explored'], 'Estados explorados')
c.boxplot(stats['cost_e1'], 'Costo total 1')
c.boxplot(stats['cost_e2'], 'Costo total 2')
c.boxplot(stats['time'], 'Tiempo empleado')
