import nodo as n
from collections import deque
import frozenLake as e
import time

def bfs(env):
    nombre = "BFS"
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
                    path, moves = solution(child)
                    first_cost, second_cost = calculate_costs(moves)
                    end_time = time.time()
                    final_time = end_time-start_time
                    return path, moves, explored_amount, first_cost, second_cost, final_time, True, nombre
                
                frontier.append(child)

    end_time = time.time()
    final_time = end_time-start_time                     
    path, moves = solution(node)    
    first_cost, second_cost = calculate_costs(moves)              
    return path, moves, explored_amount, first_cost, second_cost, final_time, False, nombre

def calculate_costs(moves):
    first_cost = 0
    second_cost = 0
    for i in range(1,len(moves)):
        first_cost += 1
        second_cost += moves[i]+1
    return first_cost, second_cost


def solution(child):
    path = []
    moves = []
    # Añadir el estado del nodo objetivo
    path.append(child.estado)
    moves.append(child.action_number)
    # Recorrer hacia atrás hasta llegar al nodo raíz
    node = child.parent
    while node is not None:
        path.append(node.estado)
        moves.append(node.action_number)
        node = node.parent
    path.reverse()
    moves.reverse()
    return path, moves

env = e.Environment(100, 0.08)
result = bfs(env)

def showMoves(moves, env):
    #  Resetear el entorno para iniciar un nuevo episodio
    state = env.environment.reset()
    # Renderizar el entorno inicial
    env.environment.render()
    time.sleep(2)
    for i in range(1,len(moves)):
        time.sleep(0.5)
        next_state, reward, done, truncated, info = env.environment.step(moves[i])  
    env.environment.render()
    time.sleep(0.5)


"""path, moves, explored_amount, first_cost, second_cost, final_time, found, nombre = result
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
    showMoves(moves, env)
"""


