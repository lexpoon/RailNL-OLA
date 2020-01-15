from functions.calculations import calc_stations, calc_connections, calc_used_connections, calc_used_connections_route
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution

import random

def randomize(routes, time):
    """Create solution consisting of random routes."""

    # Set algorithm constrains
    max_routes = routes
    max_time = time

    # Get all data of the stations
    data = RailNL().data

    # Make empty list for all routes
    solution_routes = []

    # Keep track of fraction of used connections
    all_connections = calc_connections()
    used_connections = set()

    # Make random routes untill it is not possible anymore due to the constrains
    while len(solution_routes) < max_routes and len(used_connections) < all_connections:
        random_route(solution_routes, max_time)
        used_connections.update(calc_used_connections(solution_routes))

    # Make solution class and update attributes
    random_solution = Solution(solution_routes)

    return random_solution

def random_route(routes, max_time):
    """Randomize a route."""

    # Get all data of the stations
    data = RailNL().data

    # Make new empty route list and add (non-final) route to list of routes
    routes.append([])
    total_time = 0

    # Pick random station as starting point of the route
    routes[-1].append(data[random.choice(list(data.keys()))])

    # Keep adding stations to the route until no more possible destinations
    while destination_options(routes[-1]) != []:
        routes[-1].append(random.choice(destination_options(routes[-1])))

        # Check if route meets time constrain, if not end route
        total_time = Route(routes).time
        if total_time > max_time:
            routes[-1] = routes[-1][:-1]
            break

    # Replace route list by final route object in list of routes
    routes[-1] = Route(routes)

    return routes[-1]

def destination_options(route):
    """Return possible destinations. Not possible to go to a station that is already on the route."""

    # Get current station and all data
    data = RailNL().data
    current_station = route[-1].name

    # Transform route of Station objects to route list of strings
    route_list = []
    for station in route:
        route_list.append(station.name)

    # Make list of all possible connections from current station
    options = []
    for connection in data[current_station].connections:
        if connection[0] not in route_list:
            options.append(data[connection[0]])

    return options
