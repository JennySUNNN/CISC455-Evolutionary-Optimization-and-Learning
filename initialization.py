"""
Initialize population of solution individuals.
Student number: 20082675
Student name: Jenny Sun
"""
import read_data
import random

# travel_cities_id -- contains id of cities we can visit (all cities exclude the start city)
# selected_cities_id -- contains id of cities we will visit (selected certain number of cities from the travel_cities_id)
# individual(single solution)=[city1,city2,city3...] no duplicates

def select_travel_city(city_id_list, num_cities, start_city_id):
    """Random select 'num_cities' cities id we want to travel.

    Args:
        city_id_list: list - contains integers represent all cities' id
        num_cities: int - the number of cities we want to visit
        start_city_id: int - the home city's id (i.e. the city we start at) 
    Returns:
        selected_city_id: list - contains the random selected cities' id we will visit
    """
    # Remove the start city's id from the list to form a list contains all id of cities we can visit
    travel_cities_id = city_id_list.copy()
    travel_cities_id.remove(start_city_id)
    
    # Select the number of cities from the travelable cities list
    # This list contains id of cities we will visit.
    selected_cities_id = random.sample(travel_cities_id, num_cities)
    return selected_cities_id

def initialize(pop_size, selected_cities_id):
    """Randomly initialize a population of possible path solutions.

    Args:
        pop_size: int - the size of the population
        selected_cities_id: list - contains integers represent the id of cities we will visit
    Returns:
        population: list - contains lists represent possible path solutions. 
    """
    population = []
    
    for i in range(pop_size):
        individual = selected_cities_id.copy()
        random.shuffle(individual)
        population.append(individual)

    return population


