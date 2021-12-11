
import random


# Crossover:
def permutation_cut_and_crossfill (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []
    
    # student code begin
    # method: cut and crossfill
    individual_length = len(parent1)

    # generate a random crossover point
    cut_point = random.randint(0,individual_length-1)

    # preserve the first half before the cut point for both offspring
    offspring1 = parent1[0:cut_point]
    offspring2 = parent2[0:cut_point]

    for i in range(cut_point,individual_length):
        if parent2[i] not in offspring1:
            offspring1.append(parent2[i])

        if parent1[i] not in offspring2:
            offspring2.append(parent1[i])    

    if len(offspring1) != individual_length:
        for i in range(0,cut_point):
            if parent2[i] not in offspring1:
                offspring1.append(parent2[i])
            
            if parent1[i] not in offspring2:
                offspring2.append(parent1[i]) 

    # student code end
    
    return offspring1, offspring2



# Mutation:
def inversion_mutation (individual):

    rand1 = random.randint(0,len(individual)-1)
    rand2 = random.randint(0,len(individual)-1)
    print(rand1,rand2)

    # Avoid two random integers are same
    while rand2 == rand1:
        rand2 = random.randint(0,len(individual)-1)
    
    if rand1 <= rand2:
        segment = individual[rand1:rand2]
        # Reverse the selected segment
        segment.reverse()
        mutant = individual[0:rand1]+segment+individual[rand2:]
    else:
        segment = individual[rand2:rand1]
        # Reverse the selected segment
        segment.reverse()
        mutant = individual[0:rand2]+segment+individual[rand1:]

    return mutant


# p1 = [9, 0, 4, 3, 5, 2, 6, 7, 8, 10, 11]
# p2 = [3, 11, 9, 0, 2, 6, 5, 8, 7, 4, 10]

# print(permutation_cut_and_crossfill(p1,p2))

#print(inversion_mutation([6, 0, 5, 11, 4, 3, 7, 8, 2, 10, 9]))