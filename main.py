import os, sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))
sys.path.append(os.path.join(directory, "code", "functions"))
sys.path.append(os.path.join(directory, "data"))

from station import Station
from connection import Connection
from route import Route
from solution import Solution
from import_data import RailNL
# from random import random_solution

def main():
    data = RailNL()
    print(data.data)

if __name__ == "__main__":
    main()
