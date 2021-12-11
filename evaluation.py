"""
Evaluate fitness of solution individual.
Student number: 20082675
Student name: Jenny Sun
"""
import read_data


def evaluate(individual,start_city_num,dist_matrix):

    first_city_num = individual[0]
    last_city_num = individual[-1]
    distance = dist_matrix[start_city_num][first_city_num] + dist_matrix[last_city_num][start_city_num]
    
    for i in range(len(individual)-1):
        curr_num = individual[i]
        next_num = individual[i+1]
        dist = dist_matrix[curr_num][next_num]
        
        distance += dist
    
    return distance

# a = fitness([4, 10, 3, 11, 7, 0, 6, 5, 2, 8, 9],1)
# b = fitness([7, 5, 0, 2, 6, 8, 11, 4, 3, 9, 10],1)
# print(a)
# print(b)
    