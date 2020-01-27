from functions.calculations import all_connections, update_connections, convert_object_to_string
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution
from randomize import randomize, random_route
from greedy import greedy, greedy_route
from depth_first import depth_first, depth_first_route
from breadth_first import breadth_first, breadth_first_route

import random, copy

def hillclimber(map, max_routes, max_time, min_score, solution, algorithm, iterations, depth, ratio, change_routes):
    """"Create hillclimber solution based on greedy output"""

    #
    data = RailNL(map).data
    best_solution = solution

    #
    for i in range(iterations):

        #
        last_solution = copy.deepcopy(best_solution)

        #
        last_solution = remove_routes(last_solution, change_routes)

        # Keep track of fraction of used connections
        num_connections = len(all_connections(map))
        connections = update_connections(map, data, last_solution.routes)

        for k in range(change_routes):

            # Stop adding routes if all connections are used in solution
            if len(connections["used_connections"]) > num_connections:
                break

            # Add route following input algorithm
            if algorithm == "random":
                andom_route(map, max_time, data, last_solution.routes)
            elif algorithm == "greedy":
                greedy_route(map, max_time, data, last_solution.routes, "connections")
            elif algorithm == "depth_first":
                depth_first_route(map, max_time, min_score, data, last_solution.routes, depth, ratio, "improve")
            elif algorithm == "breadth_first":
                breadth_first_route(map, max_time, min_score, data, last_solution.routes, depth, ratio, "improve")

            # Update used connections
            connections = update_connections(map, data, last_solution.routes)

        new_solution = Solution(map, last_solution.routes)

        if new_solution.score > last_solution.score:
            best_solution = new_solution

    best_solution = Solution(map, best_solution.routes)

    return best_solution

def remove_routes(solution, change_routes):
    """Remove routes of the solution"""

    while change_routes > 0:
        route = random.choice(solution.routes)
        solution.routes.remove(route)
        change_routes -= 1

        while depending_route_options(solution.routes, route) != [] and change_routes > 0:
            options = depending_route_options(solution.routes, route)
            option = random.choice(options)
            solution.routes.remove(option)
            change_routes -= 1

    return solution

def depending_route_options(routes, main_route):
    """Return routes which are connected to the main route"""

    options = set()
    main_route = convert_object_to_string(main_route)

    for route in routes:
        for station1 in main_route:
            for station in route.route:
                if station.name == station1:
                    options.add(route)
                    break

    return list(options)
