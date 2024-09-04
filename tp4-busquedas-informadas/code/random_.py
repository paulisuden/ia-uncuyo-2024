import time
import frozenLake as e
import nodo as n
from bfs import showMoves, solution 
import random

def randomm(env):  
    nombre = "Random"
    start_time = time.time()
    # Crear el nodo inicial
    node = n.Nodo(env.initial_state, None)
    
    # Caso en que initial_state = final_state
    if node.goal_test(env.final_state):
        return node
    
    # Diccionario para almacenar los estados explorados
    explored = set()
    
    # Contadores
    first_cost = 0
    second_cost = 0
    stop = False
    actions = []
    move = 0
    while stop == False:    
        # Guardarlo en los explorados (clave primaria su ubicacion (x, y))
        explored.add(node.estado)
        action = random.randint(0,3)
        actions.append(action)
        first_cost += 1
        second_cost += action+1
        value, position = node.random_actions(env, action)
        move += 1
        if value == True:
            child = n.Nodo(position, node, action)
            if child.estado not in explored:
                if child.goal_test(env.final_state):
                    explored_amount = len(explored)
                    path, moves = solution(child)
                    end_time = time.time()
                    final_time = end_time-start_time
                    return path, moves, explored_amount, first_cost, second_cost, final_time, True, nombre
            node = child
        if move > 2000:
            stop = True
    end_time = time.time()
    final_time = end_time-start_time                     
    path, moves =solution(node)                  
    return path, moves, len(explored), first_cost, second_cost, final_time, False, nombre


"""env = e.Environment(4, 0.5)
result = randomm(env)



path, moves, explored_amount, first_cost, second_cost, final_time, found, nombre = result
info = {
        'algorithm_name': 'nombre',
        'env_n': '1',
        'states_n': explored_amount,
        'cost_e1': first_cost,
        'cost_e2': second_cost,
        'time': final_time,
        'solution_found': found
    }
print(info)


if found:
    showMoves(moves, env)"""
