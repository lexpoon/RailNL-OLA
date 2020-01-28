from breadth_first import breadth_first_route
from classes.solution import Solution
from copy import deepcopy
from decimal import Decimal
from depth_first import depth_first_route
from functions.calculations import all_connections, update_connections, remove_routes
from functions.import_data import RailNL
from greedy import greedy_route
from random import random
from randomize import random_route


def simulated_annealing(map, max_routes, max_time, min_score, solution, algorithm, depth, ratio, change_routes, i, iterations, formula):
    """"Create hillclimber solution based on greedy output"""

    # Get all data from stations in map
    data = RailNL(map).data

    # Set best solution which can should be improved
    best_solution = solution

    # Remove routes that needs to be changed
    last_solution = deepcopy(best_solution)
    last_solution = remove_routes(last_solution, change_routes)

    # Add routes to solution to get new solution
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
    connections = update_connections(map, data, solution.routes)

    # Keep adding new routes untill all connections have been added to a route
    while i < change_routes and len(connections["used_connections"]) < num_connections:

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
