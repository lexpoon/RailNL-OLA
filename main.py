import os, sys, timeit

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "functions"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

from station import Station
from route import Route
from solution import Solution
from import_data import RailNL
from functions.calculations import all_connections, connections_station, update_connections
from functions.user_interface import get_map_info, get_create_algorithm, get_improve_algorithm, next_step
from randomize import randomize
from greedy import greedy
from depth_first import depth_first
from breadth_first import breadth_first
from short_route_swap import short_route_swap
from hillclimber import hillclimber
# from simulated_annealing import simulated_annealing
from visualize import visualisation

def main(map, max_routes, max_time, algorithm, iterations, key, depth, ratio, remove_routes, solution, definition):

    #
    data = RailNL(map).data
    min_score = 10000/len(all_connections(map)) - 105

    #
    if definition == 'create':
        solution_algorithm = start_algorithm(map, max_routes, max_time, algorithm, min_score, key, depth, ratio)
    else:
        solution_algorithm = improve_algorithm()

    return solution_algorithm

def start_algorithm(map, max_routes, max_time, algorithm, min_score, key, depth, ratio):
    """Find best routes based on input algorithm"""

    if algorithm == "random":
        best_score = 0
        for i in range(iterations):
            solution = randomize(map, max_routes, max_time)
            if solution.score > best_score:
                best_solution = solution

    if algorithm == "greedy":
        best_score = 0
        for i in range(iterations):
            solution = greedy(map, max_routes, max_time, key)
            if solution.score > best_score:
                best_solution = solution

    if algorithm == "depth_first":
        best_score = 0
        for i in range(iterations):
            solution = depth_first(map, max_routes, max_time, min_score, depth, ratio)
            if solution.score > best_score:
                best_solution = solution

    if algorithm == "breadth_first":
        best_score = 0
        for i in range(iterations):
            solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio)
            if solution.score > best_score:
                best_solution = solution

    visualisation(best_solution.routes, map)

    return best_solution

def improve_algorithm(map, max_routes, max_time, algorithm, min_score, key, iterations, depth, ratio, remove_routes, solution, definition):
    """Improve solution based on algorithm"""

    if algorithm == "less_is_more":
        best_score = 0
        for i in range(iterations):
            solution = less_is_more(map, max_time, min_score, solution)
            if solution.score > best_score:
                best_solution = solution

    if algorithm == "hillclimber":
        best_score = 0
        for i in range(iterations):
            solution = hillclimber(map, max_routes, max_time, algorithm, min_score, iterations, depth, ratio, remove_routes, solution)
            if solution.score > best_score:
                best_solution = solution

    # if algorithm == "simulated_annealing":
    #     best_score = 0
    #     for i in range(iterations):
    #         solution = simulated_annealing(map, max_routes, max_time, algorithm, min_score, iterations, depth, ratio, remove_routes, solution)
    #         if solution.score > best_score:
    #             best_solution = solution

    visualisation(best_solution.routes, map)

    return best_solution

if __name__ == "__main__":
    best_solution = {"solution": '', "score": 0}
    iterations = ''

    print("Welkom bij RailNL!")
    print("We gaan proberen een zo goed mogelijke dienstregeling vinden.")

    info = get_map_info()
    map = info[0]
    max_routes = info[1]
    max_time = info[2]

    info = get_create_algorithm()
    algorithm = info[0]
    key = info[1]
    depth = info[2]
    ratio = info[3]

    while isinstance(iterations, int) == False:
        iterations = input("Hoevaak wil je een nieuwe oplossing genereren?\n")
        try:
            iterations = int(iterations)
        except:
            iterations = iterations

    solution = main(map, max_routes, max_time, algorithm, iterations, key, depth, ratio, remove_routes=None, solution=None, definition="create")

    if solution.score > best_solution["score"]:
        best_solution["solution"] = solution.routes
        best_solution["score"] = solution.score

    while True:
        next_step = next_step()
        if next_step == "Stoppen":
            break

        algorithm = next_step[0]
        key = next_step[1]
        depth = next_step[2]
        ratio = next_step[3]
        definition = next_step[4]

        while isinstance(iterations, int) != True:
            iterations = input("Hoevaak wil je een route/oplossing genereren?\n")

        solution = main(map, max_routes, max_time, algorithm, iterations, key, depth, ratio, remove_routes, solution, definition)

        if solution.score > best_solution["score"]:
            best_solution["solution"] = solution.routes
            best_solution["score"] = solution.score
