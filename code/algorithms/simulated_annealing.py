from functions.calculations import all_connections, all_used_connections, update_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution
from randomize import randomize, random_route
from greedy import greedy, greedy_route
from depth_first import depth_first, depth_first_route
from breadth_first import breadth_first, breadth_first_route

import random, copy

def simulated_annealing(map, max_routes, max_time, algorithm, min_score, iterations, depth, ratio, remove_routes, solution):
    """"Create hillclimber solution based on greedy output"""

    #
    data = RailNL(map).data
    best_solution = copy.deepcopy(solution.routes)
    best_score = solution.score

    #
    for i in range(iterations):

        #
        last_solution = copy.deepcopy(best_solution)

        for j in range(remove_routes):
            last_solution.remove(random.choice(last_solution))

        for k in range(remove_routes):

            #
            connections = update_connections(last_solution, data, map)

            #
            if algorithm == "random":
                last_solution.append(random_route(connections, max_time, last_solution, data, map))
            elif algorithm == "greedy":
                last_solution.append(greedy_route(connections, max_time, "connections", last_solution, data, map))
            elif algorithm == "depth_first":
                last_solution.append(depth_first_route(max_time, map, data, last_solution, depth, min_score, ratio))
            elif algorithm == "breadth_first":
                last_solution.append(breadth_first_route(max_time, map, data, last_solution, depth, min_score, ratio))

        new_solution = Solution(last_solution, map)
        new_score = new_solution.score

        temperatuur = 1
        acceptatiekans = 2^((best_score - new_score)/temperatuur)
        randomkans = random.random()
        if acceptatiekans > randomkans:
            best_score = new_score
            best_solution = new_solution.routes

    best_solution = Solution(best_solution, map)

    return best_solution
