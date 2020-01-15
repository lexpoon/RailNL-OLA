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
from calculations import calc_stations, calc_connections, calc_used_connections, calc_used_connections_route, connections_station
from randomize import randomize
from greedy import greedy
from visualize import visualisation

def main():
    data = RailNL().data
    # solution_random = randomize(7, 120)
    # print(solution_random)
    best_score = 0
    best_sol = ''
    for i in range(100):
        solution_greedy = greedy(7, 120, "connections")
        if solution_greedy.score > best_score:
            best_score = solution_greedy.score
            best_sol = solution_greedy
    print(best_score)
    print(best_sol)

    visualize = visualisation(best_sol.routes)

    return visualize

if __name__ == "__main__":
    solution = main()
