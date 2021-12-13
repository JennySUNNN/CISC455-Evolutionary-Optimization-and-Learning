import random
#Parent selection
def MPS(fitness_list, mating_pool_size): 
    """Multi-pointer selection (MPS)"""

    selected_to_mate = []

    # student code starts
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
    
    # student code ends
    
    return selected_to_mate

# print(MPS([100,200,140,500,200,300,200,340,450,450],6))

# survivor selection
def mu_plus_lambda(current_pop, current_fitness_list, offspring, offspring_fitness_list):
    """mu+lambda selection"""
    population = []
    fitness_list = []

    # student code starts
    mu = len(current_pop) 

    # pool all current generation and offspring
    all = current_pop + offspring # mu + lambda
    all_fitness_list = current_fitness_list + offspring_fitness_list 

    # zip the population with its fitness_list into tuple, stored in a list 
    # [(individual1,fitness_list1),(individual2,fitness_list2),...]
    all_tuple_list = list(zip(all,all_fitness_list)) 

    # ranking current individuals and offsprings according to its fitness_list, in descending order
    # sort the list of tuples [(individual1,fitness_list1),(individual2,fitness_list2),...] based on fitness_list
    #all_tuple_list.sort(reverse=True, key=lambda y:y[1])

    all_tuple_list.sort(key=lambda y:y[1])


    # pick the top mu individuals to be survivors
    survivor_tuple_list = all_tuple_list[0:mu]

    # upzip the sorted list of tuples from [(individual1,fitness_list1),(individual2,fitness_list2),...] --> [[individual1,individual2,...],[fitness_list1,fitness_list2,...]]
    survivor_list = [list(i) for i in zip(*survivor_tuple_list)]

    population = survivor_list[0]
    fitness_list = survivor_list[1]
    
    # student code ends
    
    return population, fitness_list