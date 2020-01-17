import os, sys

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
from hillclimber import hillclimber
from visualize import visualisation

def main(map, routes, time):

    data = RailNL(map).data

    best_score_random = 0
    for i in range(10):
        solution_random = randomize(routes, time, map)
        if solution_random.score > best_score_random:
            best_sol_random = solution_random
            best_score_random = best_sol_random.score

    best_score_greedy = 0
    for i in range(10):
        solution_greedy = greedy(routes, time, "connections", map)
        if solution_greedy.score > best_score_greedy:
            best_sol_greedy = solution_greedy
            best_score_greedy = best_sol_greedy.score

    best_score_greedy1 = 0
    for i in range(10):
        solution_greedy1 = greedy(routes, time, "time", map)
        if solution_greedy1.score > best_score_greedy1:
            best_sol_greedy1 = solution_greedy1
            best_score_greedy1 = best_sol_greedy1.score

    best_score_greedy2 = -1000
    for i in range(10):
        solution_greedy2 = greedy(routes, time, "quality", map)
        if solution_greedy2.score > best_score_greedy2:
            best_sol_greedy2 = solution_greedy2
            best_score_greedy2 = best_sol_greedy2.score

    print(best_sol_random.score)
    hillclimber(best_sol_greedy.routes, time, map, best_sol_greedy)
    print(best_sol_greedy.score)
    hillclimber(best_sol_greedy1.routes, time, map, best_sol_greedy1)
    print(best_sol_greedy1.score)
    hillclimber(best_sol_greedy2.routes, time, map, best_sol_greedy2)
    print(best_sol_greedy2.score)

    # visualize_random = visualisation(best_sol_random.routes, map)
    # visualize_greedy = visualisation(best_sol_greedy.routes, map)
    # visualize_greedy1 = visualisation(best_sol_greedy1.routes, map)
    # visualize_greedy2 = visualisation(best_sol_greedy2.routes, map)

if __name__ == "__main__":
    solution = main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
