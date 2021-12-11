# imports
import random
import numpy

# import your own modules
import read_data
import initialization
import evaluation
import variation
import selection


def main():

    #Parameter:
    city_name_path = "uk-12/uk12_name.txt"
    distance_path = "uk-12/uk12_dist.txt"


    city_list,city_num_list = read_data.get_city_names(city_name_path)
    dist_matrix = read_data.get_distance(distance_path)

    pop_size = 20
    num_cities = 11
    start_city = 'Glasgow'
    start_city_num = city_list.index(start_city)

    gen_limit = 10

    gen = 0
    population = initialization.initialize(pop_size,city_list, city_num_list, num_cities, start_city)
    print(population)

    fitness = []
    for individual in population:
        fitness.append(evaluation.evaluate(individual,start_city_num,dist_matrix))
    print("generation", gen, ": best fitness", min(fitness), "\taverage fitness", sum(fitness)/len(fitness))

    # Evolution begins
    while gen < gen_limit:

        parent_idx = selection.MPS(fitness,10)

        random.shuffle(parent_idx)

        offspring = []
        offspring_fitness = []
        i= 0 # initialize the counter for parents in the mating pool
        
        # # offspring are generated using selected parents in the mating pool
        # while len(offspring) < mating_pool_size:
        
        #     # recombination
        #     if random.random() < xover_rate:            
        #         off1,off2 = recombination.permutation_cut_and_crossfill(population[parents_index[i]], population[parents_index[i+1]])
        #     else:
        #         off1 = population[parents_index[i]].copy()
        #         off2 = population[parents_index[i+1]].copy()

        #     # mutation
        #     if random.random() < mut_rate:
        #         off1 = mutation.permutation_swap(off1)
        #     if random.random() < mut_rate:
        #         off2 = mutation.permutation_swap(off2)
        
        #     offspring.append(off1)
        #     offspring_fitness.append(evaluation.fitness_8queen(off1))
        #     offspring.append(off2)
        #     offspring_fitness.append(evaluation.fitness_8queen(off2))
        #     i = i+2  # update the counter




main()
