"""
The main function that runs two different algorithm on the same dataset.
Student number: 20082675
Student name: Jenny Sun
"""
# imports
import read_data
import initialization
import evaluation
import algorithm

def main():
    # Common Parameters:
    city_name_path = "uk-12/uk12name.txt"
    distance_path = "uk-12/uk12dist.txt"

    # All cities name and id
    city_list,city_id_list = read_data.get_city_names(city_name_path)
    dist_matrix = read_data.get_distance(distance_path)
    # Can be changed based on preference: how many cities want to visit? which city is the home city?
    num_cities = 11
    start_city = 'London'

    start_city_id = city_list.index(start_city)

    # Cities that we will visit
    selected_cities_id = initialization.select_travel_city(city_id_list, num_cities, start_city_id) 

    # Genetic algorithm result:
    print("Genetic Algorithm Results:")
    algorithm.genetic_algo(start_city_id,selected_cities_id,dist_matrix)
    print()

    # Greedy algorithm result:
    greedy_solution = [start_city_id]
    curr_city_id = start_city_id
    selected_cities_id.append(curr_city_id)
    num_visited_city = 0
    
    while num_visited_city < num_cities:
    
        next_city_id = algorithm.greedy_algo(curr_city_id,selected_cities_id,dist_matrix)
        selected_cities_id.remove(curr_city_id)
        greedy_solution.append(next_city_id)
        
        curr_city_id = next_city_id
        num_visited_city += 1

    greedy_fitness = evaluation.evaluate(greedy_solution,start_city_id,dist_matrix)
    print("Greedy Fitness:",greedy_fitness)
    print("Greedy Solution:",greedy_solution)

main()
    
