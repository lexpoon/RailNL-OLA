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
from calculations import calc_stations, calc_connections
from randomize import solution
from visualize import visualisation

def main():
    data = RailNL()
    solution_random = solution(7, 120)

    # return solution_random

    # TEST
    test_routes_visualisation = {'1': ['Amsterdam Zuid', 'Amsterdam Amstel', 'Schiphol Airport'], '2': ['Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag Centraal', 'Leiden Centraal']}
    visualize = visualisation(test_routes_visualisation)

    return visualize

if __name__ == "__main__":
    solution = main()
    print(solution)
