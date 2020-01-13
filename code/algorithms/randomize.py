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
        solution["routes"].append(random_route(solution))
        used_connections.update(calc_used_connections(solution["routes"]))

    random_solution = Solution(solution["routes"])
    solution["time"] = random_solution.time
    solution["quality"] = random_solution.score

    return random_solution

def random_route(solution):
    """Randomize a route."""

    data = RailNL().data
    route_list = []
    total_time = 0
    route_list.append(data[random.choice(list(data.keys()))])
    # print (f"de huidige route: {route_list}")

    while total_time < 120:
        print (f"the current route: {route_list}")
        current_station = route_list[-1].name
        # for x in route_list:
        #     print (f"stations used: {x}")
        for y in data[current_station].connections:
            print (f"connections are: {y}")
            # print (data[current_station].connections[0])
            # if x in data[current_station].connections:
            #     print (f"these is a match: {x}")
            # else:
            #     print ("nothing found")

        # print (f"dit zijn de opties: {data[current_station].connections}")
        destination = random.choice(data[current_station].connections)
        # print (f"dit wordt toegevoerd: {data[destination[0]]}")
        route_list.append(data[destination[0]])
        # print (route_list)
        total_time += int(destination[1])

    route = Route(len(solution["routes"]) + 1, route_list)

    return route
