# CISC455-Final Project:



To run and output the result: (In terminal) 
```
python3 main.py
```
It will output the evolutionary algorithm and greedy algorithm result using same data.

To adjust common parameters, adjust them in main.py - main() function.
To adjust parameters for evolutionary algorithm, go to algorithm.py - evolutionary_algo() function.

Sample output:
```
Genetic Algorithm Results:
generation 0 : best fitness 3042 	average fitness 3590.175
generation 1 : best fitness 2972 	average fitness 3441.925
generation 2 : best fitness 2972 	average fitness 3315.3
generation 3 : best fitness 2833 	average fitness 3230.25
generation 4 : best fitness 2723 	average fitness 3128.725
generation 5 : best fitness 2458 	average fitness 3023.75
generation 6 : best fitness 2458 	average fitness 2937.0
generation 7 : best fitness 2458 	average fitness 2863.45
generation 8 : best fitness 2458 	average fitness 2806.425
generation 9 : best fitness 2317 	average fitness 2740.425
generation 10 : best fitness 2317 	average fitness 2711.75
generation 11 : best fitness 2317 	average fitness 2678.1
generation 12 : best fitness 2317 	average fitness 2646.05
generation 13 : best fitness 2317 	average fitness 2594.75
generation 14 : best fitness 2127 	average fitness 2552.175
generation 15 : best fitness 2127 	average fitness 2530.375
generation 16 : best fitness 2127 	average fitness 2481.45
generation 17 : best fitness 2127 	average fitness 2441.325
generation 18 : best fitness 2127 	average fitness 2421.925
generation 19 : best fitness 2127 	average fitness 2392.025
generation 20 : best fitness 2127 	average fitness 2352.6
generation 21 : best fitness 2009 	average fitness 2299.825
generation 22 : best fitness 2009 	average fitness 2264.5
generation 23 : best fitness 2009 	average fitness 2222.0
generation 24 : best fitness 2009 	average fitness 2186.1
generation 25 : best fitness 2009 	average fitness 2142.95
EA best solution: 0 [11, 3, 1, 8, 6, 2, 4, 0, 9, 10, 5] 2009
EA best solution: 1 [11, 3, 1, 8, 6, 2, 4, 0, 9, 10, 5] 2009
EA best solution: 2 [11, 3, 1, 8, 6, 2, 4, 0, 9, 10, 5] 2009

Greedy Fitness: 2234
Greedy Solution: [7, 11, 4, 2, 6, 8, 3, 1, 5, 9, 0, 10]
```

Every module and its functions have detailed description and comments within the code. 

Below is a brief structure of all modules and functions:
### main.py
- main()

### initialization.py
- select_travel_city(city_id_list, num_cities, start_city_id)
- initialize(pop_size, selected_cities_id)

### evaluation.py
- evaluate(individual,start_city_id,dist_matrix)

### parent_selection.py
- MPS(fitness_list, mating_pool_size)
- tournament(fitness_list, mating_pool_size, tournament_size)

### survivor_selection.py
- mu_plus_lambda(current_pop, current_fitness_list, offspring, offspring_fitness_list)
- replacement(current_pop, current_fitness, offspring, offspring_fitness)

### variation.py
- permutation_cut_and_crossfill (parent1, parent2)
- order_xover(parent1,parent2)
- inversion_mutation (individual)

### algorithm.py
- genetic_algo(start_city_id,selected_cities_id,dist_matrix)
- greedy_algo(curr_city_id,selected_cities_id,dist_matrix)



