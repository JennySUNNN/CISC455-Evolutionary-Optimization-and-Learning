# imports
from os import closerange
import random
import numpy

import read_data
import initialization
import evaluation
import variation
import selection

def genetic_algo(start_city_id,selected_cities_id,dist_matrix):
    """Genetic algorithm process.

    Args:
        selected_city_id: list - contains the random selected cities' id we will visit
        start_city_id: int - the home city's id (i.e. the city we start at) 
    Output:
        Print out best and average fitness value of each generation. 
        Eventually print out the best solution and its fitness value.
    """
    # Genetic algorithm parameters:
    pop_size = 40
    mating_pool_size = int(pop_size*0.5)
    xover_rate = 0.9
    mutation_rate = 0.2
    gen_limit = 20
    
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
        parent_idx = selection.MPS(fitness_list,mating_pool_size)

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

        population, fitness_list = selection.mu_plus_lambda(population,fitness_list,offspring_list,offspring_fitness_list)

        gen += 1
        print("generation", gen, ": best fitness", min(fitness_list), "\taverage fitness", sum(fitness_list)/len(fitness_list))
    # evolution ends

    # Print best solutions
    # print(len(fitness_list))
    # print('Final fitness',fitness_list)
    # print('Final population',population)
    k = 0
    for i in range (0, pop_size):
        if fitness_list[i] == min(fitness_list):
            print("best solution", k, population[i], fitness_list[i])
            k += 1


def greedy_algo(curr_city_id,selected_cities_id,dist_matrix):

    # The list of distance from current city to all other cities
    available_list = list(dist_matrix[curr_city_id])
    init_distance_list = available_list.copy() # Store the initial distance list to find the index of the smallest one later

    # Delete all non-selected city's (city that will not be visited) distance from the list
    for i in range(len(init_distance_list)): 
        if i not in selected_cities_id:
            available_list.remove(init_distance_list[i])
    
    available_list.sort() # Delete itself distance (0) from the list

    smallest_distance = available_list[1]
    closest_city_id = init_distance_list.index(smallest_distance)

    return closest_city_id


def main():
    # Common Parameters:
    city_name_path = "uk-12/uk12_name.txt"
    distance_path = "uk-12/uk12_dist.txt"
    # All cities name and id
    city_list,city_id_list = read_data.get_city_names(city_name_path)
    dist_matrix = read_data.get_distance(distance_path)
    # Can be changed based on preference: how many cities want to visit? which city is the home city?
    num_cities = 11
    start_city = 'London'
    start_city_id = city_list.index(start_city)
    # Cities that we will visit
    selected_cities_id = initialization.select_travel_city(city_id_list, num_cities, start_city_id)


    # Genetic algorithm:
    print("Genetic Algorithm Results:")
    genetic_algo(start_city_id,selected_cities_id,dist_matrix)

    # Greedy algorithm:
    greedy_solution = [start_city_id]
    curr_city_id = start_city_id
    selected_cities_id.append(curr_city_id)
    num_visited_city = 0
    
    while num_visited_city < num_cities:
        next_city_id = greedy_algo(curr_city_id,selected_cities_id,dist_matrix)
        greedy_solution.append(next_city_id)
        selected_cities_id.remove(curr_city_id)
        curr_city_id = next_city_id

        num_visited_city += 1

    greedy_fitness = evaluation.evaluate(greedy_solution,start_city_id,dist_matrix)
    print(greedy_fitness)
    print(greedy_solution)

main()
    





# main()
