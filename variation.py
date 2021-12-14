"""
My collection of all variation operators functions, including crossover and mutation.
Student number: 20082675
Student name: Jenny Sun
"""
import random

# Crossover:
def permutation_cut_and_crossfill (parent1, parent2):
    """Perform cut and crossfill crossover on two given parents to produce offsprings.

    Args:
        parent1, parent2: list - individual solution that been selected as parent
    Returns:
        offspring1, offspring2: list - individual solution that been created by performing crossover of two parents.
    """
    offspring1 = []
    offspring2 = []
    
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
    
    return offspring1, offspring2

def order_xover(parent1,parent2):
    """Perform order crossover on two given parents to produce offsprings.

    Args:
        parent1, parent2: list - individual solution that been selected as parent
    Returns:
        offspring1, offspring2: list - individual solution that been created by performing crossover of two parents.
    """
    offspring1 = []
    offspring2 = []
    individual_length = len(parent1)

    # Generate random cut points
    random_points = random.sample(range(0,individual_length),2)
    cut1 = min(random_points)
    cut2 = max(random_points)

    # Copy the selected segment
    seg1 = parent1[cut1:cut2]
    seg2 = parent2[cut1:cut2]

    # Copy rest from the other parent in order
    order1= []
    for element in parent2[cut2:]:
        if element not in seg1:
            order1.append(element)
    for element in parent2[0:cut2]:
        if element not in seg1:
            order1.append(element)
    
    order2 = []
    for element in parent1[cut2:]:
        if element not in seg2:
            order2.append(element)
    for element in parent1[0:cut2]:
        if element not in seg2:
            order2.append(element)

    ends1 = []
    ends2 = []
    for i in range(len(parent2[cut2:])):
        ends1.append(order1[0])
        order1.pop(0)
        ends2.append(order2[0])
        order2.pop(0)

    front1 = []
    front2 = []
    for i in range(len(parent2[0:cut1])):
        front1.append(order1[0])
        order1.pop(0)
        front2.append(order2[0])
        order2.pop(0)
  
    # offspring[0:cut1]+seg1+offspring[cut2:]
    offspring1 = front1 + seg1 + ends1
    offspring2 = front2 + seg2 + ends2
    return offspring1,offspring2
  

# Mutation:
def inversion_mutation (individual):
    """Perform inversion mutation on the given individual.

    Args:
        individual: list - contains integers represent an individual solution
    Returns:
        mutant: list - a mutated individual solution
    """
    rand1 = random.randint(0,len(individual)-1)
    rand2 = random.randint(0,len(individual)-1)

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
