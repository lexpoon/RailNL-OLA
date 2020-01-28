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
from plots import boxplot, histogram_bar, lineplot_iterations, histogram_multiple

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

def main(map, max_routes, max_time, iterations, algorithm=None, key=None, min_score=None, depth=None, ratio=None):
    boxplot(map, max_routes, max_time, iterations, algorithm, key, min_score, depth, ratio)

def histogram_basic(map, max_routes, max_time, iterations, key=None, min_score=None, depth=None, ratio=None):

    score_random = []
    for i in range(iterations):
        random_solution = randomize(map, max_routes, max_time)
        score_random.append(random_solution.score)

    score_greedy = []
    for i in range(iterations):
        greedy_solution = greedy(map, max_routes, max_time, key)
        score_greedy.append(greedy_solution.score)

    score_depth_first = []
    for i in range(iterations):
        depth_first_solution = depth_first(map, max_routes, max_time, min_score, depth, ratio)
        score_depth_first.append(depth_first_solution.score)

    score_breadth_first = []
    for i in range(iterations):
        breadth_first_solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio)
        score_breadth_first.append(breadth_first_solution.score)

    histogram_bar(score_random, score_greedy, score_depth_first, score_breadth_first)

def histogram_extended(map, max_routes, max_time, iterations, key=None, min_score=None, depth=None, ratio=None):
    best_score_random = 0
    for i in range(iterations):
        randomize_solution = randomize(map, max_routes, max_time)
        if randomize_solution.score > best_score_random:
            best_score_random = randomize_solution.score
            best_solution_random = randomize_solution

    # print ("random", best_solution_random)
    # print ("------")
    # print ("hillclimber", hillclimber(map, max_routes, max_time, min_score, best_solution_random, "depth_first", iterations, depth, ratio, 4))

    best_score_greedy = 0
    for i in range(iterations):
        greedy_solution = greedy(map, max_routes, max_time, key)
        if greedy_solution.score > best_score_greedy:
            best_score_greedy = greedy_solution.score
            best_solution_greedy = greedy_solution

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

    best_score_depth_first = 0
    for i in range(iterations):
        depth_first_solution = depth_first(map, max_routes, max_time, min_score, depth, ratio)
        if depth_first_solution.score > best_score_depth_first:
            best_score_depth_first = depth_first_solution.score
            best_solution_depth_first = depth_first_solution

    # print ("depth first" , best_solution_depth_first)
    # print ("hillclimber", hillclimber(map, max_routes, max_time, min_score, best_solution_depth_first, "depth_first", iterations, depth, ratio, 4))
    # print ("------")

    best_score_breadth_first = 0
    for i in range(iterations):
        breadth_first_solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio)
        if breadth_first_solution.score > best_score_breadth_first:
            best_score_breadth_first = breadth_first_solution.score
            best_solution_breadth_first = breadth_first_solution

    # print ("breadth first" , best_solution_breadth_first)
    # print ("hillclimber", hillclimber(map, max_routes, max_time, min_score, best_solution_breadth_first, "depth_first", iterations, depth, ratio, 4))
    # print ("------")

    histogram_multiple(best_solution_random, best_solution_greedy, best_solution_depth_first, best_solution_breadth_first)

if __name__ == "__main__":
    # main("Nationaal", 20, 180, 1, "connections", 100, 3, 1.5)

    # histogram_basic("Nationaal", 20, 180, 100, "connections", 100, 3, 1.2)

    """iterations"""
    # in main:     # lineplot_iterations(map, max_routes, max_time, iterations, algorithm, key, min_score, depth, ratio)
    # main("Nationaal", 20, 180, 10, "random")
    # main("Nationaal", 20, 180, 10, "greedy", "connections")
    # main("Nationaal", 20, 180, 10, "greedy", "time")
    # main("Nationaal", 20, 180, 10, "greedy", "score")
    # main("Nationaal", 20, 180, 2, "depth first", None, 100, 3, 1.2)
    # main("Nationaal", 20, 180, 10, "breadth first", None, 100, 3, 1.2)

    """boxplot"""
    main("Nationaal", 20, 180, 10, algorithm=None, key=None, min_score=None, depth=None, ratio=None)


    # histogram_extended("Nationaal", 20, 180, 1, "connections", 100, 3, 1.5)
