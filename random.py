from classes.station import Station
from classes.connection import Connection
from classes.solution import Solution

import random

def random_solution(self, data, trains, time):
    """ """
    solution = {}

    self.data = data
    self.max_trains = trains
    self.time = time

    route = 0
    all_connections = 0
    used_connections = 0
    for station in self.data:
        for connection in station.connections:
            all_connections += 1

    while len(solution.routes) < self.max_trains or used_connections < all_connections:
        solution["routes"] = self.random_route()
        used_connections += len(solution["routes"]["route"])
        route += 1

    return

def random_route(self):
    """ """
    return

solution = {
    "routes": {
        "1": {"route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
        "2": {"route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
        "3": {"route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
        "4": {"route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
        "5": {"route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
        "6": {"route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
        "7": {"route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
        },
    "quality": 10
}
