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
from functions.calculations import calc_stations, calc_connections, calc_used_connections, calc_used_connections_route, connections_station, update_connections
from randomize import randomize
from greedy import greedy
from depth_first import depth_first
from hillclimber import hillclimber
from visualize import visualisation

def main(map, routes, time, iterations):

    data = RailNL(map).data

    min_score = 10000/len(calc_connections(map)) - 105

    start = timeit.default_timer()
    best_score_depth = 0
    depth = 4
    ratio = 1.5
    for i in range(iterations):
        solution_depth = depth_first(map, time, routes, depth, min_score, ratio)
        if solution_depth.score > best_score_depth:
            best_sol_depth = solution_depth
            best_score_depth = best_sol_depth.score
    print(best_sol_depth)
    stop = timeit.default_timer()
    print('Time Depth First: ', stop - start)

    # start = timeit.default_timer()
    # best_score_random = 0
    # for i in range(iterations):
    #     solution_random = randomize(routes, time, map)
    #     if solution_random.score > best_score_random:
    #         best_sol_random = solution_random
    #         best_score_random = best_sol_random.score
    # stop = timeit.default_timer()
    # print('Time Random: ', stop - start)

    start = timeit.default_timer()
    best_score_greedy = 0
    for i in range(iterations):
        solution_greedy = greedy(routes, time, "connections", map)
        if solution_greedy.score > best_score_greedy:
            best_sol_greedy = solution_greedy
            best_score_greedy = best_sol_greedy.score
    print(best_sol_greedy)
    stop = timeit.default_timer()
    print('Time Greedy: ', stop - start)

    # start = timeit.default_timer()
    # best_score_greedy1 = 0
    # for i in range(iterations):
    #     solution_greedy1 = greedy(routes, time, "time", map)
    #     if solution_greedy1.score > best_score_greedy1:
    #         best_sol_greedy1 = solution_greedy1
    #         best_score_greedy1 = best_sol_greedy1.score
    # stop = timeit.default_timer()
    # print('Time Greedy1: ', stop - start)
    #
    # start = timeit.default_timer()
    # best_score_greedy2 = 0
    # for i in range(iterations):
    #     solution_greedy2 = greedy(routes, time, "quality", map)
    #     if solution_greedy2.score > best_score_greedy2:
    #         best_sol_greedy2 = solution_greedy2
    #         best_score_greedy2 = best_sol_greedy2.score
    # stop = timeit.default_timer()
    # print('Time Greedy2: ', stop - start)

    # print(best_sol_random.score)
    # improve_random = hillclimber(best_sol_random.routes, time, map, min_score, best_sol_random)
    # print(best_sol_greedy.score)
    # improve_greedy = hillclimber(best_sol_greedy.routes, time, map, min_score, best_sol_greedy)
    # print(best_sol_greedy1.score)
    # improve_greedy1 = hillclimber(best_sol_greedy1.routes, time, map, min_score, best_sol_greedy1)
    # print(best_sol_greedy2.score)
    # improve_greedy2 = hillclimber(best_sol_greedy2.routes, time, map, min_score, best_sol_greedy2)
    # print(best_sol_depth.score)
    # improve_depth = hillclimber(best_sol_depth.routes, time, map, min_score, best_sol_depth)

    # visualize_random = visualisation(best_sol_random.routes, map)
    # visualize_random_improvement = visualisation(improve_random.routes, map)
    # visualize_greedy = visualisation(best_sol_greedy.routes, map)
    # visualize_greedy_improvement = visualisation(improve_greedy.routes, map)
    # visualize_greedy1 = visualisation(best_sol_greedy1.routes, map)
    # visualize_greedy1_improvement = visualisation(improve_greedy1.routes, map)
    # visualize_greedy2 = visualisation(best_sol_greedy2.routes, map)
    # visualize_greedy2_improvement = visualisation(improve_greedy2.routes, map)
    # visualize_depth = visualisation(best_sol_depth.routes, map)
    # visualize_depth_improvement = visualisation(improve_depth.routes, map)

if __name__ == "__main__":
    solution = main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
