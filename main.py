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
from functions.user_interface import welcome, get_map_info, get_create_algorithm, get_improve_algorithm, check_score, next_step, get_int, get_float
from randomize import randomize
from greedy import greedy
from depth_first import depth_first
from breadth_first import breadth_first
from short_route_swap import short_route_swap
from hillclimber import hillclimber
from simulated_annealing import simulated_annealing
from visualize import visualisation
from plots import histogram_bar, histogram_multiple, iteration_lineplot

def main(map, max_routes, max_time, iterations, key=None, min_score=None, depth=None, ratio=None):

    # best_score_random = 0
    # for i in range(iterations):
    #     randomize_solution = randomize(map, max_routes, max_time)
    #     if randomize_solution.score > best_score_random:
    #         best_score_random = randomize_solution.score
    #         best_solution_random = randomize_solution
    #
    # print ("random", best_solution_random)
    # print ("hillclimber", hillclimber(map, max_routes, max_time, min_score, best_solution_random, "depth_first", iterations, depth, ratio, 4))
    # print ("------")
    #
    # best_score_greedy = 0
    # for i in range(iterations):
    #     greedy_solution = greedy(map, max_routes, max_time, key)
    #     if greedy_solution.score > best_score_greedy:
    #         best_score_greedy = greedy_solution.score
    #         best_solution_greedy = greedy_solution
    #
    # print ("greedy connections", best_solution_greedy)
    # print ("hillclimber", hillclimber(map, max_routes, max_time, min_score, best_solution_greedy, "depth_first", iterations, depth, ratio, 4))
    # print ("------")
    #
    # best_score_greedy = 0
    # for i in range(iterations):
    #     greedy_solution = greedy(map, max_routes, max_time, "time")
    #     if greedy_solution.score > best_score_greedy:
    #         best_score_greedy = greedy_solution.score
    #         best_solution_greedy = greedy_solution
    #
    # print ("greedy time", best_solution_greedy)
    # print ("hillclimber", hillclimber(map, max_routes, max_time, min_score, best_solution_greedy, "depth_first", iterations, depth, ratio, 4))
    # print ("------")
    #
    # best_score_greedy = 0
    # for i in range(iterations):
    #     greedy_solution = greedy(map, max_routes, max_time, "score")
    #     if greedy_solution.score > best_score_greedy:
    #         best_score_greedy = greedy_solution.score
    #         best_solution_greedy = greedy_solution
    #
    # print ("greedy score", best_solution_greedy)
    # print ("hillclimber", hillclimber(map, max_routes, max_time, min_score, best_solution_greedy, "depth_first", iterations, depth, ratio, 4))
    # print ("------")
    #
    best_score_depth_first = 0
    for i in range(iterations):
        depth_first_solution = depth_first(map, max_routes, max_time, min_score, depth, ratio)
        if depth_first_solution.score > best_score_depth_first:
            best_score_depth_first = depth_first_solution.score
            best_solution_depth_first = depth_first_solution

    print ("depth first" , best_solution_depth_first)
    print ("hillclimber", hillclimber(map, max_routes, max_time, min_score, best_solution_depth_first, "depth_first", iterations, depth, ratio, 4))
    print ("------")

    best_score_breadth_first = 0
    for i in range(iterations):
        breadth_first_solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio)
        if breadth_first_solution.score > best_score_breadth_first:
            best_score_breadth_first = breadth_first_solution.score
            best_solution_breadth_first = breadth_first_solution

    print ("breadth first" , best_solution_breadth_first)
    print ("hillclimber", hillclimber(map, max_routes, max_time, min_score, best_solution_breadth_first, "depth_first", iterations, depth, ratio, 4))
    print ("------")


if __name__ == "__main__":
    main("Nationaal", 20, 180, 10, "connections", 100, 3, 1.5)
