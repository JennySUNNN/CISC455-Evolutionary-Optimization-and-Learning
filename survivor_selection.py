"""
My collection of survivor selection methods.
Student number: 20082675
Student name: Jenny Sun
"""
import random

# survivor selection
def mu_plus_lambda(current_pop, current_fitness_list, offspring, offspring_fitness_list):
    """Perform mu+lambda selection on current population to select survivors.

    Args:
        current_pop: list - contains lists represent possible path solutions. 
        current_fitness_list: list - contains integers represent all individuals fitness_list value.
        offspring: list - contains lists represent newly generated individuals (offsprings).
        offspring_fitness_list: list - contains integers represent offsprings fitness_list value.
    Returns:
        population: list - contains individuals after doing survivor selection.
        fitness_list: list - contains integers represent populations' individual's fitness_list value.
    """
    population = []
    fitness_list = []

    mu = len(current_pop) 

    # Pool all current generation and offspring
    all = current_pop + offspring # mu + lambda
    all_fitness_list = current_fitness_list + offspring_fitness_list 

    # zip the population with its fitness_list into tuple, stored in a list 
    # [(individual1,fitness_list1),(individual2,fitness_list2),...]
    all_tuple_list = list(zip(all,all_fitness_list)) 

    # ranking current individuals and offsprings according to its fitness_list, in ascending order
    # sort the list of tuples [(individual1,fitness_list1),(individual2,fitness_list2),...] based on fitness_list
    all_tuple_list.sort(key=lambda y:y[1])

    # pick the top mu individuals to be survivors
    survivor_tuple_list = all_tuple_list[0:mu]

    # upzip the sorted list of tuples from [(individual1,fitness_list1),(individual2,fitness_list2),...] --> [[individual1,individual2,...],[fitness_list1,fitness_list2,...]]
    survivor_list = [list(i) for i in zip(*survivor_tuple_list)]

    population = survivor_list[0]
    fitness_list = survivor_list[1]
    
    return population, fitness_list


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """Perform replacement selection on current population to select survivors. 
       Use lambda offspring replace worst current generation individuals.

    Args:
        current_pop: list - contains lists represent possible path solutions. 
        current_fitness_list: list - contains integers represent all individuals fitness_list value.
        offspring: list - contains lists represent newly generated individuals (offsprings).
        offspring_fitness_list: list - contains integers represent offsprings fitness_list value.
    Returns:
        population: list - contains individuals after doing survivor selection.
        fitness_list: list - contains integers represent populations' individual's fitness_list value.
    """

    population = []
    fitness_list = []

    mu = len(current_pop)
    lbd = len(offspring)

    # zip the current population with its fitness_list into tuple, stored in a list.
    current_pop_tuple_list = list(zip(current_pop,current_fitness)) 

    # same for offspring
    offspring_tuple_list = list(zip(offspring,offspring_fitness))

    # rank current population with its fitness_list (descending order)
    current_pop_tuple_list.sort(reverse=True, key=lambda y:y[1])

    # remove the worst lambda from current generation individuals 
    new_tuple_list = current_pop_tuple_list[0:(mu-lbd)]

    # add offspring to replace the removed individuals
    survivor_tuple_list = new_tuple_list + offspring_tuple_list

    # unzip the survivor list of tuples
    survivor_list = [list(i) for i in zip(*survivor_tuple_list)]

    population = survivor_list[0]
    fitness_list = survivor_list[1]

    return population, fitness_list