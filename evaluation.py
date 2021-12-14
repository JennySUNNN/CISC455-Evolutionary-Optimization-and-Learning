"""
Evaluate fitness (distance) of solution individual.
Student number: 20082675
Student name: Jenny Sun
"""

def evaluate(individual,start_city_id,dist_matrix):
    """Evaluate individual's fitness based on the total travel distance of the path.
    Fitness value aim to be minimized.

    Args:
        individual: list - contains id of cities we will visit in order
        start_city_id: int - the home city's id (i.e. the city we start at) 
        dist_matrix: numpy array - array arrays of distances from each city to other city.
    Returns:
        distance: int - the total travel distance of the individual path
    """

    first_city_id = individual[0]
    last_city_id = individual[-1]

    # Sum the distance  of 'the start city to the first city' and 'the last city to the start(home) city' 
    distance = dist_matrix[start_city_id][first_city_id] + dist_matrix[last_city_id][start_city_id]
    
    for i in range(len(individual)-1):
        curr_city = individual[i]
        next_city = individual[i+1]

        # Add the distance from the 1st-2nd & 2nd-3rd & 3rd-4th ...
        dist = dist_matrix[curr_city][next_city]
        distance += dist
    
    return distance