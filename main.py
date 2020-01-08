import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "functions"))
sys.path.append(os.path.join(directory, "data"))

from station import Station
from connection import Connection
from route import Route
from solution import Solution
from import_data import RailNL
from calculations import calc_stations, calc_connections
from random_alg import solution

def main():
    data = RailNL("Holland")
    solution_random = solution(7, 120, "Holland")

    return solution_random

if __name__ == "__main__":
    main()
