from functions.calculations import calc_stations, calc_connections
from classes.station import Station
from classes.connection import Connection
from classes.route import Route
from classes.solution import Solution

import random

def solution(self, routes, time, map):
    """ """

    self.max_routes = routes
    self.max_time = time
    self.map = map

    self.data = RailNL(self.map).data

    self.solution["routes"] = []
    self.solution["time"] = 0
    self.solution["quality"] = 0

    all_connections = self.calc_connections()
    used_connections = set()

    route = 0
    while len(solution["routes"]) < self.max_trains or len(used_connections) < all_connections:
        self.solution["routes"].append(self.random_route())
        for i in range(self.solution["routes"][route]["route"] - 1):
            if i == 0:
                connection = sorted(self.solution["routes"][route]["route"][i].name, self.solution["routes"][route]["route"][i+1].destination.name)
            else:
                connection = (self.solution["routes"][route]["route"][i].destination.name, self.solution["routes"][route]["route"][i+1].destination.name)
            used_connections.add(connection)
        route += 1

    return self.solution

def random_route(self):
    """ """

    self.solution["routes"][route]["route"] = []
    self.solution["routes"][route]["time"] = 0

    # random station kiezen
    start = random.choice(self.data.keys())

    while self.solution["routes"][route]["time"] < 120:
        if self.solution["routes"][route]["route"] == []:
            self.solution["routes"][route]["route"].append(self.random_connection(self.data[start]))
        else:
            self.solution["routes"][route]["route"].append(self.random_connection(self.solution["routes"][route]["route"][-1]))
        self.solution["routes"][route]["time"] += 0

    return self.solution["routes"][route]["route"]

def random_connection(self, origin):
    """ """


    return True

# solution = {
#     "routes":
#         [{"id"; 1, "route": [Start station.name, Connection(1).destination.name, Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
#         {"id"; 2, "route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
#         {"id"; 3, "route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
#         {"id"; 4, "route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
#         {"id"; 5, "route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
#         {"id"; 6, "route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
#         {"id"; 7, "route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100},
#         ],
#     "time": 250,
#     "quality": 10000
# }
