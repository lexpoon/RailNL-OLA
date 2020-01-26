from breadth_first import breadth_first, breadth_first_route
from classes.solution import Solution
from depth_first import depth_first, depth_first_route
from functions.calculations import update_connections
from functions.import_data import RailNL
from greedy import greedy, greedy_route
from randomize import randomize, random_route

import copy
import random
from decimal import Decimal


def simulated_annealing(map, max_routes, max_time, min_score, solution, algorithm, iterations, depth, ratio, remove_routes, formula):
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
            while last_solution:
                last_solution.remove(random.choice(last_solution))

        for k in range(remove_routes):

            #
            connections = update_connections(map, data, last_solution)

            #
            if algorithm == "random":
                last_solution.append(random_route(map, max_time, data, last_solution))
            elif algorithm == "greedy":
                last_solution.append(greedy_route(map, max_time, data, last_solution, "connections"))
            elif algorithm == "depth_first":
                last_solution.append(depth_first_route(map, max_time, min_score, data, last_solution, depth, ratio))
            elif algorithm == "breadth_first":
                last_solution.append(breadth_first_route(map, max_time, min_score, data, last_solution, depth, ratio))

        new_solution = Solution(map, last_solution)
        new_score = new_solution.score

        if formula == "linear":
            temperature = iterations / 2 - 0.5 * i
        elif formula == "exponential":
            temperature = iterations * 0.92 ** i

        acceptatiekans = 2 ** Decimal((best_score - new_score) / Decimal(temperature))
        randomkans = random.random()
        if acceptatiekans > randomkans:
            best_score = new_score
            best_solution = new_solution.routes

    best_solution = Solution(map, best_solution)

    return best_solution
