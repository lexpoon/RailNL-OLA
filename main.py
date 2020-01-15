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
from visualize import visualisation

def main(map, routes, time):

    data = RailNL(map).data

    best_score_random = 0
    for i in range(1):
        solution_random = randomize(routes, time, map)
        if solution_random.score > best_score_random:
            best_sol_random = solution_random
            best_score_random = best_sol_random.score

    best_score_greedy = 0
    for i in range(1):
        solution_greedy = greedy(routes, time, "connections", map)
        if solution_greedy.score > best_score_greedy:
            best_sol_greedy = solution_greedy
            best_score_greedy = best_sol_greedy.score

    print(best_sol_random)
    print(best_sol_greedy)

    visualize_random = visualisation(best_sol_random.routes, map)
    visualize_greedy = visualisation(best_sol_greedy.routes, map)

    return visualize_random, visualize_greedy

if __name__ == "__main__":
    solution = main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
