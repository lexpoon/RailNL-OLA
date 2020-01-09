from functions.calculations import calc_stations, calc_connections, calc_used_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution

import random

def solution(routes, time):
    """Create solution consisting of random routes."""

    max_routes = routes
    max_time = time

    data = RailNL().data
    solution = {}
    solution["routes"] = []

    all_connections = calc_connections()
    used_connections = set()

    route = 0
    while len(solution["routes"]) < max_routes and len(used_connections) < all_connections:
        solution["routes"].append(random_route(solution))
        used_connections.update(calc_used_connections(solution["routes"]))
        route += 1

    random_solution = Solution(solution["routes"])
    solution["time"] = random_solution.time
    solution["quality"] = random_solution.score

    return solution

def random_route(solution):
    """Randomize a route."""

    data = RailNL().data
    route_list = []
    total_time = 0
    route_list.append(data[random.choice(list(data.keys()))])
    while total_time < 120:
        current_station = route_list[-1].name
        destination = random.choice(data[current_station].connections)
        route_list.append(data[destination[0]])
        total_time += int(destination[1])

    route = Route(len(solution["routes"]), route_list)

    return route

# solution = {
#     "routes":
#         [{"id": 1, "route": [Station(1), Station(2), Station(3), Station(4)], "time": 100},
#         {"id": 2, "route": [Station(1), Station(2), Station(3), Station(4)], "time": 100},
#         {"id": 3, "route": [Station(1), Station(2), Station(3), Station(4)], "time": 100},
#         {"id": 4, "route": [Station(1), Station(2), Station(3), Station(4)], "time": 100},
#         {"id": 5, "route": [Station(1), Station(2), Station(3), Station(4)], "time": 100},
#         {"id": 6, "route": [Station(1), Station(2), Station(3), Station(4)], "time": 100},
#         {"id": 7, "route": [Station(1), Station(2), Station(3), Station(4)], "time": 100},
#         ],
#     "time": 250,
#     "quality": 10000
# }
