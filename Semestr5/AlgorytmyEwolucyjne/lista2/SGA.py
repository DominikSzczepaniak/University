import time
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

class SGA:
    def __init__(self, population_size, chromosome_length, number_of_offspring, crossover_probability, mutation_probability, number_of_iterations, mutation_operator, mutation_function, objective_function):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.number_of_offspring = number_of_offspring
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.number_of_iterations = number_of_iterations
        self.mutation_operator = mutation_operator
        self.mutation_function = mutation_function
        self.objective_function = objective_function

    def run_SGA(self):
        time0 = time.time()

        best_objective_value = np.inf
        best_chromosome = np.zeros((1, self.chromosome_length))
        costs_SGA = np.zeros(self.number_of_iterations)

        # generating an initial population
        current_population = np.zeros((self.population_size, self.chromosome_length), dtype=np.int64)
        for i in range(self.population_size):
            current_population[i, :] = np.random.permutation(self.chromosome_length)

        # evaluating the objective function on the current population
        objective_values = np.zeros(self.population_size)
        for i in range(self.population_size):
            objective_values[i] = self.objective_function(current_population[i, :])

        for t in range(self.number_of_iterations):
            # selecting the parent indices by the roulette wheel method
            fitness_values = objective_values.max() - objective_values
            if fitness_values.sum() > 0:
                fitness_values = fitness_values / fitness_values.sum()
            else:
                fitness_values = np.ones(self.population_size) / self.population_size
            parent_indices = np.random.choice(self.population_size, self.number_of_offspring, True, fitness_values).astype(np.int64)

            # creating the children population
            children_population = np.zeros((self.number_of_offspring, self.chromosome_length), dtype=np.int64)
            for i in range(int(self.number_of_offspring / 2)):
                if np.random.random() < self.crossover_probability:
                    children_population[2 * i, :], children_population[2 * i + 1, :] = self.mutation_operator(
                        current_population[parent_indices[2 * i], :].copy(), 
                        current_population[parent_indices[2 * i + 1], :].copy()
                    )
                else:
                    children_population[2 * i, :], children_population[2 * i + 1, :] = (
                        current_population[parent_indices[2 * i], :].copy(), 
                        current_population[parent_indices[2 * i + 1]].copy()
                    )

            if np.mod(self.number_of_offspring, 2) == 1:
                children_population[-1, :] = current_population[parent_indices[-1], :]

            # mutating the children population
            for i in range(self.number_of_offspring):
                if np.random.random() < self.mutation_probability:
                    children_population[i, :] = self.mutation_function(children_population[i, :])

            # evaluating the objective function on the children population
            children_objective_values = np.zeros(self.number_of_offspring)
            for i in range(self.number_of_offspring):
                children_objective_values[i] = self.objective_function(children_population[i, :])

            # replacing the current population by (Mu + Lambda) Replacement
            objective_values = np.hstack([objective_values, children_objective_values])
            current_population = np.vstack([current_population, children_population])

            I = np.argsort(objective_values)
            current_population = current_population[I[:self.population_size], :]
            objective_values = objective_values[I[:self.population_size]]

            # recording some statistics
            if best_objective_value < objective_values[0]:
                best_objective_value = objective_values[0]
                best_chromosome = current_population[0, :]
            costs_SGA[t] = objective_values.mean()

            print('%3d %14.8f %12.8f %12.8f %12.8f %12.8f' % (
                t, time.time() - time0, objective_values.min(), 
                objective_values.mean(), objective_values.max(), objective_values.std()
            ))

        return costs_SGA