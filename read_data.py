import numpy as np

def get_city_names(city_name_path):
# Get the list of codes for all cities
    code_file = open(city_name_path,"r")
    city_list = []
    for city in code_file:
        city = city.rstrip('\n')
        city_list.append(city)
    
    city_num_list = []
    for i in range(len(city_list)):
        city_num_list.append(i)

    return city_list,city_num_list
    

def get_distance(distance_path):
# Obtain the distance data matrix (numpy array)
    dist_file = open(distance_path,"r")
    dist_list = []
    for dist in dist_file:
        city_dist = dist.split()
        for i in range(len(city_dist)):
            city_dist[i] = int(city_dist[i])
        dist_list.append(city_dist)
    dist_list = np.array(dist_list)

    return dist_list

# a = get_distance(distance_path)
# print(a)
# print(a[0][1])
