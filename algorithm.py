"""
Two kinds of algorithms.
Student number: 20082675
Student name: Jenny Sun
"""
import random

import initialization
import evaluation
import variation
import parent_selection
import survivor_selection

def genetic_algo(start_city_id,selected_cities_id,dist_matrix):
    """Genetic algorithm solver.

    Args:
        start_city_id: int - the home city's id (i.e. the city we start at)
        selected_cities_id: list - contains the random selected cities' id we will visit
        dist_matrix: nparray - disance matrix that shown the distance from a city to others
    Output:
        Print out best and average fitness value of each generation. 
        Eventually print out the best solution and its fitness value.
    """
    # Genetic algorithm parameters:
    pop_size = 40
    mating_pool_size = int(pop_size*0.5)
    xover_rate = 0.9
    mutation_rate = 0.2
    gen_limit = 25
    
    gen = 0
    # Initialize the population
    population = initialization.initialize(pop_size, selected_cities_id)

    # Evaluate the fitness of each individual
    fitness_list = []
    for individual in population:
        fitness_list.append(evaluation.evaluate(individual,start_city_id,dist_matrix))
    print("generation", gen, ": best fitness", min(fitness_list), "\taverage fitness", sum(fitness_list)/len(fitness_list))

    # Evolution starts
    while gen < gen_limit:

        # Select parent (store in a list)
        parent_idx = parent_selection.MPS(fitness_list,mating_pool_size)
        #parent_idx = parent_selection.tournament(fitness_list,mating_pool_size,tournament_size=5)

        random.shuffle(parent_idx)

        # Reproduction
        offspring_list = []
        offspring_fitness_list = []

        i = 0
        while len(offspring_list) < mating_pool_size:
            p1 = parent_idx[i]
            p2 = parent_idx[i+1]

            # Crossover
            if random.random() < xover_rate:
                off1,off2 = variation.permutation_cut_and_crossfill(population[p1],population[p2])
                #off1,off2 = variation.order_xover(population[p1],population[p2])
            else:
                off1 = population[p1].copy()
                off2 = population[p2].copy()
            
            # Mutation
            if random.random() < mutation_rate:
                off1 = variation.inversion_mutation(off1)
            if random.random() < mutation_rate:
                off2 = variation.inversion_mutation(off2)
            offspring_list.append(off1)
            offspring_list.append(off2)

            off1_fitness = evaluation.evaluate(off1,start_city_id,dist_matrix)
            off2_fitness = evaluation.evaluate(off2,start_city_id,dist_matrix)
            offspring_fitness_list.append(off1_fitness)
            offspring_fitness_list.append(off2_fitness)
            i += 2

        population, fitness_list = survivor_selection.mu_plus_lambda(population,fitness_list,offspring_list,offspring_fitness_list)
        # population, fitness_list = survivor_selection.replacement(population,fitness_list,offspring_list,offspring_fitness_list)

        gen += 1
        print("generation", gen, ": best fitness", min(fitness_list), "\taverage fitness", sum(fitness_list)/len(fitness_list))
    # Evolution ends

    # Print best solutions
    # print(len(fitness_list))
    # print('Final fitness',fitness_list)
    # print('Final population',population)
    k = 0
    for i in range (0, pop_size):
        if fitness_list[i] == min(fitness_list):
            print("EA best solution:", k, population[i], fitness_list[i])
            k += 1


def greedy_algo(curr_city_id,selected_cities_id,dist_matrix):
    """Greedy algorithm solver.

    Args:
        curr_city_id: int - current city's id
        selected_citis_id: list - contains the random selected cities' id we will visit
        dist_matrix: nparray - disance matrix that shown the distance from a city to others
    Returns:
        closest_city_id: int - the id of the closest city to current city
    """

    # The list of distance from current city to all other cities
    available_list = list(dist_matrix[curr_city_id])
    init_distance_list = available_list.copy() # Store the initial distance list to find the index of the smallest one later

    # Delete all non-selected city's (city that will not be visited) distance from the list
    for i in range(len(init_distance_list)): 
        if i not in selected_cities_id:
            available_list.remove(init_distance_list[i])
    
    available_list.sort()
    smallest_distance = available_list[1] # Get the second smallest distance from the list (smallest is 0 which is itself)

    closest_city_id = init_distance_list.index(smallest_distance)

    return closest_city_id

