import nodo as n
from collections import deque
import frozenLake as e
import time
import bfs as b

def dfs(env):
    nombre = "DFS"
    start_time = time.time()
    # Crear el nodo inicial
    nodo = n.Nodo(env.initial_state, None)
    
    # Caso en que initial_state = final_state
    if nodo.goal_test(env.final_state):
        return nodo
    
    # Crear una cola FIFO (frontera)
    frontier = deque([nodo])
    
    # Diccionario para almacenar los estados explorados
    explored = set()
    
    
    while frontier:
        # Extraer el nodo de la frontera
        node = frontier.popleft()
        
        # Guardarlo en los explorados (clave primaria su ubicacion (x, y))
        explored.add(node.estado)
        
        actions, action_number = node.possible_actions(env)
        
        for action in actions:
            action_cost = action_number.popleft()
            child = n.Nodo(action, node, action_cost)
            if child.estado not in explored and child.estado not in (n.estado for n in frontier):
                if child.goal_test(env.final_state):
                    explored_amount = len(explored)
                    path, moves = b.solution(child)
                    end_time = time.time()
                    final_time = end_time-start_time
                    first_cost, second_cost = b.calculate_costs(moves)
                    if len(moves) <= 1000: found = True 
                    else: found = False                    
                    return path, moves, explored_amount, first_cost, second_cost, final_time, found, nombre
                
                frontier.appendleft(child)

    end_time = time.time()
    final_time = end_time-start_time                     
    path, moves = b.solution(node)    
    first_cost, second_cost = b.calculate_costs(moves)              
    return path, moves, explored_amount, first_cost, second_cost, final_time, False, nombre

env = e.Environment(100, 0.08)
result = dfs(env)

path, moves, explored_amount, first_cost, second_cost, final_time, found, nombre = result
info = {
        'algorithm_name': 'UCS',
        'env_n': 1,
        'states_n': explored_amount,
        'cost_e1': first_cost,
        'cost_e2': second_cost,
        'time': final_time,
        'solution_found': True
    }
print(info)

"""
if found:
    b.showMoves(moves, env)
"""








