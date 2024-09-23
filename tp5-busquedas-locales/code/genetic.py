import random
import time as t
import numpy as np
import board as b

class QueenGA:
    def __init__(self, n, population_size=100, tournament_size=5, mutation_rate=0.01, generations=1000, population=None):
        self.n = n
        self.population_size = population_size 
        self.tournament_size = tournament_size  
        self.mutation_rate = mutation_rate
        self.generations = generations
        if population is None:
            self.population = self.initialize_population()
        else:
            self.population = population

    def initialize_population(self):
        return [self.generate_random_individual() for _ in range(self.population_size)]

    def generate_random_individual(self):
        return random.sample(range(self.n), self.n) 

    def fitness(self, individual):
        not_attacked = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if individual[i] != individual[j] and abs(individual[i] - individual[j]) != j - i:
                    not_attacked += 1
        return not_attacked

    def tournament_selection(self):
        if not isinstance(self.population, list):
            raise TypeError("vacia")
        tournament = random.sample(self.population, self.tournament_size)
        tournament.sort(key=lambda x: self.fitness(x), reverse=True)
        return tournament[0]

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, self.n - 2)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return [child1, child2]

    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            i = random.randint(0, self.n - 1)
            individual[i] = random.randint(0, self.n - 1)  

    def replace_worst(self, children):
        # reemplaza a los peores individuos por los hijos generados
        self.population.sort(key=lambda x: self.fitness(x))
        self.population[:len(children)] = children

def genetics(popu):
    size = len(popu[0])
    current = QueenGA(n=size, population_size=100, tournament_size=5, mutation_rate=0.05, generations=1000, population=popu)

    variacionH = []
    start_time = t.time()
    iteration = 0
    for generation in range(current.generations):
        new_population = []
        
        while len(new_population) < current.population_size:
            iteration += 1
            parent1 = current.tournament_selection()
            parent2 = current.tournament_selection()

            children = current.crossover(parent1, parent2)
            
            for child in children:
                current.mutate(child)
                new_population.append(child)

        current.replace_worst(new_population)

        best_individual = max(current.population, key=lambda x: current.fitness(x))
        best_fitness = current.fitness(best_individual)
        attacks = b.h(best_individual)

        variacionH.append(attacks)

        if best_fitness == current.n * (current.n - 1) // 2:
            end_time = t.time()
            elapsed_time = end_time - start_time
            return attacks, elapsed_time, iteration, variacionH

    end_time = t.time()
    elapsed_time = end_time - start_time
    return attacks, elapsed_time, iteration, variacionH
"""
# Ejecutar el algoritmo genético para resolver el problema de las 8 reinas
data = np.load('4reinasGA.npy', allow_pickle=True)

def population_as_lists(lista):
    return [individual.tolist() for individual in lista]
lista = data[3]
pasar = population_as_lists(lista)
result = genetics(pasar)

#best_fitness, elapsed_time, iteration, variacionH = result
print(result)
"""