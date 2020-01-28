from breadth_first import breadth_first_route
from classes.solution import Solution
from copy import deepcopy
from decimal import Decimal
from depth_first import depth_first_route
from functions.calculations import all_connections, update_connections, convert_object_to_string, remove_routes
from functions.import_data import RailNL
from greedy import greedy_route
from random import random
from randomize import random_route


def simulated_annealing(map, max_routes, max_time, min_score, solution, algorithm, depth, ratio, change_routes, i, iterations, formula):
    """"Create hillclimber solution based on greedy output"""

    #
    data = RailNL(map).data
    best_solution = solution

    last_solution = deepcopy(best_solution)
    last_solution = remove_routes(last_solution, change_routes)

    # Create solution of new routes
    new_routes = add_routes(map, max_time, min_score, data, last_solution,
        algorithm, depth, ratio, change_routes, "improve")

    new_solution = Solution(map, new_routes)

    # Set temperature depending of formula
    if formula == "linear":
        temperature = iterations / 2 - 0.5 * i
    elif formula == "exponential":
        temperature = iterations * 0.92 ** i

    # Determine if new solution needs to be accepted
    acceptation_probability = 2 ** Decimal((last_solution.score - new_solution.score) / Decimal(temperature))
    random_probability = random()
    if acceptation_probability > random_probability:
        best_solution = new_solution

    return best_solution

def add_routes(map, max_time, min_score, data, solution, algorithm, depth, ratio,
        change_routes, definition):
    """."""

    # Keep track of fraction of used connections
    num_connections = len(all_connections(map))
    connections = update_connections(map, data, last_solution.routes)

    for k in range(change_routes):

        # Stop adding routes if all connections are used in solution
        if len(connections["used_connections"]) > num_connections:
            break

        # Add route following input algorithm
        if algorithm == "random":
            random_route(map, max_time, data, solution.routes)
        elif algorithm == "greedy":
            greedy_route(map, max_time, data, solution.routes, "connections")
        elif algorithm == "depth_first":
            depth_first_route(map, max_time, min_score, data, solution.routes, depth, ratio, "improve")
        elif algorithm == "breadth_first":
            breadth_first_route(map, max_time, min_score, data, solution.routes, depth, ratio, "improve")

        # Update used connections
        connections = update_connections(map, data, solution.routes)

    return solution.routes
