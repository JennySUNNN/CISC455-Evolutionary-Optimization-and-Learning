"""
Initialize population of solution individuals.
Student number: 20082675
Student name: Jenny Sun
"""
import read_data
import random


#solution=[start,city1,city2,city3...,start] no duplicates

def initialize(pop_size, city_list, city_num_list, num_cities, start_city):
    """Randomly initialize a population of possible solutions.

    Args:
        pop_size: int - the size of the population
        num_cities: int - the number of city we want to visit
        start_city: string - the home city (i.e. the city we start at) 
    Returns:
        population: list - 
    """

    start_city_num = city_list.index(start_city)

    # Remove the start city from the list to 
    # form a list contains the city we want to travel
    travel_cities = city_list.copy()
    travel_cities.remove(start_city)

    travel_cities_num = city_num_list.copy()
    travel_cities_num.remove(start_city_num)
    # print("new",travel_cities)
    # print("new",travel_cities_num)

    population = []
    for i in range(pop_size):
        individual = random.sample(travel_cities_num,num_cities)
        population.append(individual)

    return population

