import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "functions"))

from station import Station
from route import Route
from solution import Solution
from import_data import RailNL
from calculations import calc_stations, calc_connections
from randomize import solution

def main():
    data = RailNL()
    solution_random = solution(7, 120)

    return solution_random

if __name__ == "__main__":
    solution = main()
    print(solution)
