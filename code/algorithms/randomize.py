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

    while len(solution["routes"]) < max_routes and len(used_connections) < all_connections:
        solution["routes"].append(random_route(len(solution["routes"]) + 1))
        used_connections.update(calc_used_connections(solution["routes"]))

    random_solution = Solution(solution["routes"])
    solution["time"] = random_solution.time
    solution["quality"] = random_solution.score

    return random_solution

def random_route(route_id):
    """Randomize a route."""

    data = RailNL().data
    route_list = []
    total_time = 0
    route_list.append(data[random.choice(list(data.keys()))])

    while total_time < 120 and destination_options(route_list):
        route_list.append(random.choice(destination_options(route_list)))
        total_time = Route(route_id, route_list).time

    route = Route(route_id, route_list)

    return route

def destination_options(route):
    """Return possible destinations. Not possible to go to a station that is already on the route."""

    options = []
    data = RailNL().data
    current_station = route[-1].name

    route_list = []
    for station in route:
        route_list.append(station.name)

    for option in data[current_station].connections:
        if data[option[0]].name not in route_list:
            options.append(data[option[0]])

    return options
