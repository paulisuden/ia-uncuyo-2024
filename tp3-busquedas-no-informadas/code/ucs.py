import time
import frozenLake as e
import nodo as n
from queue import PriorityQueue
import bfs as b

def ucs(env):
    nombre = "UCS"
    start_time = time.time()
    # Crear el nodo inicial
    nodo_inicial = n.Nodo(env.initial_state,None,None, 0)
    
    # Caso en que initial_state = final_state
    if nodo_inicial.goal_test(env.final_state):
        return nodo_inicial
    
    # Crear la cola de prioridad (frontera) y un diccionario auxiliar
    frontier = PriorityQueue()
    frontier_dict = {}  # Diccionario para búsqueda rápida
    frontier.put((0, nodo_inicial))
    frontier_dict[nodo_inicial.estado] = nodo_inicial
    
    # Conjunto para almacenar los estados explorados
    explored = set()

    
    while not frontier.empty():
        # Extraer el nodo de menor costo de la frontera
        priority, node = frontier.get()
        if node.estado in frontier_dict:
            del frontier_dict[node.estado]  # Remover del diccionario
        
        # Si ya hemos llegado al estado objetivo, retornar el camino
        if node.goal_test(env.final_state):
            explored_amount = len(explored)
            path, moves = b.solution(node)
            end_time = time.time()
            final_time = end_time-start_time
            first_cost, second_cost = b.calculate_costs(moves)
            return path, moves, explored_amount, first_cost, second_cost, final_time, True, nombre
        
        # Guardar el estado en explorados
        explored.add(node.estado)
        
        # posibles acciones ordenadas por costo menor
        actions, amount = node.possible_actions_p(env)
        
        for action in actions:
            child = n.Nodo(action[1], node, action[0], priority + action[0])
            
            if child.estado not in explored:
                if child.estado not in frontier_dict:
                    # Añadir el nodo hijo a la frontera y al diccionario
                    frontier.put((child.path_cost, child))
                    frontier_dict[child.estado] = child
                else:
                    # Si el nuevo nodo tiene un menor costo, reemplaza el nodo existente
                    existing_node = frontier_dict[child.estado]
                    if child.path_cost < existing_node.path_cost:
                        # Remover el nodo existente
                        # no se puede remover del PriorityQueue pero se ignora cuando se extraiga más adelante
                        frontier.put((child.path_cost, child))
                        frontier_dict[child.estado] = child 
    end_time = time.time()
    final_time = end_time-start_time                     
    path, moves = b.solution(node)   
    first_cost, second_cost = b.calculate_costs(moves)               
    return path, moves, explored_amount, first_cost, second_cost, final_time, False, nombre

env = e.Environment(100, 0.08)
result = ucs(env)

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





