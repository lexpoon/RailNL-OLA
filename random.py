from classes.station import Station
from classes.connection import Connection
from classes.solution import Solution

import random

def random_solution(self, data, trains, time):
    """ """

    self.solution = {}

    self.data = data
    self.max_trains = trains
    self.time = time

    route = 0
    all_connections = 0
    used_connections = set()
    for station in self.data:
        for connection in station.connections:
            all_connections += 1

    while len(solution["routes"]) < self.max_trains or len(used_connections) < all_connections:
        self.solution["routes"][route]["route"] = self.random_route()
        used_connections.update(self.solution["routes"][route]["route"])
        route += 1

    return

def random_route(self):
    """ """

    self.solution["routes"][route]["route"] = []
    self.solution["routes"][route]["time"] = 0
    self.solution["routes"][route]["route"].append(random.choice(self.data[random.choice(list(self.data.keys()))].connections))
    self.solution["routes"][route]["time"] += self.solution["routes"][route]["route"][0].time

    while self.solution["routes"][route]["time"] < 200:
         self.solution["routes"][route]["route"].append(self.random_connection(self.solution["routes"][route]["route"][0].origin))
         self.solution["routes"][route]["time"] += self.solution["routes"][route]["route"][len(self.solution["routes"][route]["route"])].time
    return

def random_connection(self, origin):
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
