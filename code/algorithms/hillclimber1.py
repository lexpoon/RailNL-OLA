from functions.calculations import calc_stations, calc_connections, calc_used_connections, calc_used_connections_route, connections_station, update_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution
from randomize import randomize
from greedy import greedy
from depth_first import depth_first
from breadth_first import breadth_first

import random, copy

def hillclimber1(solution, max_routes, max_time, map, algorithm, remove_routes, iterations, depth, min_score, ratio):
    """"Create hillclimber solution based on greedy output"""

    #
    data = RailNL(map).data
    best_solution = copy.deepcopy(solution.routes)
    best_score = solution.score
    print(solution)
    #
    for i in range(iterations):

        #
        last_solution = best_solution

        for j in range(remove_routes):
            last_solution.remove(random.choice(last_solution))

        for k in range(remove_routes):

            #
            connections = update_connections(last_solution, data, map)

            #
            if algorithm == "random":
                last_solution.append(random_route(connections, max_time, last_solution, data, map))
            elif algorithm == "greedy":
                last_solution.append(greedy_route(connections, max_time, key, last_solution, data, map))
            elif algorithm == "depth_first":
                last_solution.append(depth_first_route(max_time, map, data, last_solution, depth, min_score, ratio))
            elif algorithm == "breadth_first":
                last_solution.append(breadth_first_route(max_time, map, data, last_solution, depth, min_score, ratio))

        new_solution = Solution(last_solution, map)
        new_score = new_solution.score
        print(new_solution)
        print("-----")
        if new_score > best_score:
            best_score = new_score
            best_solution = new_solution.routes

    best_solution = Solution(best_solution, map)
    print("--------------")
    print(best_solution)

    return best_solution
