"""
My collection of parent selection methods
Student number: 20082675
Student name: Jenny Sun
"""
import random

# Parent selection
def MPS(fitness_list, mating_pool_size): 
    """Perform multipointer selection to select parent individuals.

    Args:
        fitness_list: list - contains integers represent all individuals fitness_list value.
        mating_pool_size: int - the number of parents we want to select.
    Returns:
        seleted_to_mate: list - contains integers represent the index number of selected individuals from the population list.
    """
    selected_to_mate = []

    # create the cumulative probability distribution
    probability_dist = []
    cummulative_prob = 0
    for i in range(len(fitness_list)):
        p = fitness_list[i] / sum(fitness_list)
        cummulative_prob += p
        probability_dist.append(cummulative_prob)

    current_member = 0
    i = 0
    r = random.random() * (1/mating_pool_size) # generate the random pointer 1
    while current_member < mating_pool_size:
        while r <= probability_dist[i]:
            selected_to_mate.append(i) # append the fitness_list index
            r = r + (1/mating_pool_size) # setting the next pointer
            current_member += 1
        i += 1
    
    return selected_to_mate

def tournament(fitness_list, mating_pool_size, tournament_size):
    """Perform tournament selection to select parent individuals.

    Args:
        fitness_list: list - contains integers represent all individuals fitness_list value.
        mating_pool_size: int - the number of parents we want to select.
        tournament_size: int - the number of individuals picked to compete
    Returns:
        seleted_to_mate: list - contains integers represent the index number of selected individuals from the population list.
    """
    selected_to_mate = []

    current_member = 0

    while current_member < mating_pool_size:
        population_size = len(fitness_list)

        # generate (tournament_size) number of random integers, no repetitive (without replacement)
        random_idx_list = random.sample(range(0,population_size),tournament_size) 

        random_fitness_list = []
        for i in range(len(random_idx_list)):
            random_fitness_list.append(fitness_list[random_idx_list[i]])

        best_fitness = max(random_fitness_list) # find the max fitness_list value
        fitness_index = fitness_list.index(best_fitness) # find the best fitness_list's index
        
        selected_to_mate.append(fitness_index)
        current_member += 1

    return selected_to_mate