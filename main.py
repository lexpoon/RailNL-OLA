import os, sys, timeit

directory = os.path.dirname(os.path.realpath(_file_))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "functions"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

from station import Station
from route import Route
from solution import Solution
from import_data import RailNL
from functions.calculations import calc_connections, connections_station, update_connections
from randomize import randomize
from greedy import greedy
from depth_first import depth_first
from breadth_first import breadth_first
from hillclimber import hillclimber
from hillclimber1 import hillclimber1
from visualize import visualisation

def main(map, max_routes, max_time, algorithm, iterations, key, depth, ratio, definition):

    data = RailNL(map).data

    min_score = 10000/len(calc_connections(map)) - 105

def get_map_info():
    return map, max_routes, max_time

    if definition == 'create':
        start_algorithm(map, max_routes, max_time, algorithm, min_score, key, depth, ratio)
    else:
        improve_algorithm()

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

        visualisation(best_solution)
        return best_solution

    def improve_algorithm(map, max_routes, max_time, algorithm, min_score, key, iterations, depth, ratio, remove_routes, solution):
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
        #         solution = simulated_annealing()
        #         if solution.score > best_score:
        #             best_solution = solution

        visualisation(best_solution)
        return best_solution

if __name__ == "__main__":
    best_solution = {"solution": '', "score"; 0}

    print("Welkom bij RailNL!")
    print("We willen graag de beste oplossing zien te vinden voor onze dienstregeling. Help je ons mee op zo alle reizigers zo snel mogelijk te vervoeren?")

    info = get_map_info()
    map = info[0]
    max_routes = info[1]
    max_time = info[2]

    info = get_create_algorithm()
    algorithm = info[0]
    key = info[1]
    depth = info[2]
    ratio = info[3]

    iterations = get_int("Hoevaak zou je een nieuwe oplossing willen genereren?")

    solution = main(map, max_routes, max_time, algorithm, iterations, key, depth, ratio, "create")

    if solution.score > best_solution["score"]:
        best_solution["solution"] = solution.routes
        best_solution["score"] = solution.score

    next_step = get_string("Wil je hierop een verbeter algoritme toepassen? Of wil je een algoritme nog een keer runnen? Improve/Algorith")



    iterations = get_int("Hoevaak zou je een nieuwe oplossing willen genereren?")

    solution = main(map, max_routes, max_time, algorithm, iterations, key, depth, ratio, "improve")


    best_sol_breadth, routes, "depth_first_route", remove_routes, iteration
