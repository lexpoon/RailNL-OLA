from functions.calculations import all_connections, update_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution
from randomize import randomize, random_route
from greedy import greedy, greedy_route
from depth_first import depth_first, depth_first_route
from breadth_first import breadth_first, breadth_first_route

import random, copy

def hillclimber(map, max_routes, max_time, min_score, solution, algorithm, iterations, depth, ratio, remove_routes):
    """"Create hillclimber solution based on greedy output"""

    #
    data = RailNL(map).data
    best_solution = solution

    #
    for i in range(iterations):

        #
        last_solution = copy.deepcopy(best_solution)

        for j in range(remove_routes):
            last_solution.routes.remove(random.choice(last_solution.routes))

        # Keep track of fraction of used connections
        num_connections = len(all_connections(map))
        connections = update_connections(map, data, last_solution.routes)

        for k in range(remove_routes):

            # Stop adding routes if all connections are used in solution
            if len(connections["used_connections"]) > num_connections:
                break

            # Add route following input algorithm
            if algorithm == "random":
                last_solution.routes.append(random_route(map, max_time, data, last_solution.routes))
            elif algorithm == "greedy":
                last_solution.routes.append(greedy_route(map, max_time, data, last_solution.routes, "connections"))
            elif algorithm == "depth_first":
                last_solution.routes.append(depth_first_route(map, max_time, min_score, data, last_solution.routes, depth, ratio))
            elif algorithm == "breadth_first":
                last_solution.routes.append(breadth_first_route(map, max_time, min_score, data, last_solution.routes, depth, ratio))

            # Update used connections
            connections = update_connections(map, data, last_solution.routes)


        new_solution = Solution(map, last_solution.routes)

        if new_solution.score > last_solution.score:
            best_solution = new_solution

    best_solution = Solution(map, best_solution.routes)

    return best_solution
