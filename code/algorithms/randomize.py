from functions.calculations import calc_stations, calc_connections, calc_used_connections, calc_used_connections_route, connections_station, update_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution

import random

def randomize(routes, time, map):
    """Create solution consisting of random routes."""

    # Set algorithm constrains
    max_routes = routes
    max_time = time

    # Get all data of  stations of current map
    data = RailNL(map).data

    # Make empty list for all routes
    solution_routes = []

    # Keep track of fraction of used connections
    all_connections = calc_connections(map)
    connections_dict = connections_station(data)

    # Make random routes untill it is not possible anymore due to the constrains
    while len(solution_routes) < max_routes and len(connections_dict["used_connections"]) < all_connections:
        random_route(connections_dict, max_time, solution_routes, data, map)

    # Make solution class and update attributes
    random_solution = Solution(solution_routes, map)

    return random_solution

def random_route(connections, max_time, routes, data, map):
    """Randomize a route."""

    # Make new empty route list and add (non-final) route to list of routes
    routes.append([])
    total_time = 0

    # Pick random station as starting point of the route
    routes[-1].append(random.choice(list(data.values())))

    # Keep adding stations to the route until no more possible destinations
    while random_options(connections, routes[-1], data) != None:
        routes[-1].append(random_options(connections, routes[-1], data))
        update_connections(connections, routes[-1])

        # Check if route meets time constrain, if not end route
        total_time = Route(routes, map).time
        if total_time > max_time:
            routes[-1] = routes[-1][:-1]
            break

    # Replace route list by final route object in list of routes
    routes[-1] = Route(routes, map)

    return routes[-1]

def random_options(connections, route, data):
    """Return possible destinations. Not possible to go to a station that is already on the route."""

    # Transform route of Station objects to route list of strings
    route_list = []
    for station in route:
        route_list.append(station.name)

    # Determine all possible connections from current station
    options = []
    for connection in data[route_list[-1]].connections:
        possible_connection = (route_list[-1], connection[0])
        if tuple(sorted(possible_connection)) not in connections["used_connections"]:
            options.append(connection[0])

    # If any options, return random option
    if options:
        return data[random.choice(options)]

    return None
