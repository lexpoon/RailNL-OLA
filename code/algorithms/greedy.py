from functions.calculations import calc_stations, calc_connections, calc_used_connections, calc_used_connections_route, connections_station, update_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution

import random

def greedy(routes, time, key):
    """ Create solution consisting of routes based on greedy algorithm. """

    # Set algorithm constrains
    max_routes = routes
    max_time = time
    key = key

    # Get all data of the stations
    data = RailNL().data

    # Make empty list for all routes
    solution_routes = []

    # Keep track of fraction of used connections
    all_connections = calc_connections()
    connections_dict = connections_station(data)

    # Make greedy routes untill it is not possible anymore due to the constrains
    while len(solution_routes) < max_routes and len(connections_dict["used_connections"]) < all_connections:
        greedy_route(connections_dict, max_time, key, solution_routes)

    # Make solution class and update attributes
    greedy_solution = Solution(solution_routes)

    return greedy_solution

def greedy_route(connections, max_time, key, routes,):
    """Create a greedy route."""

    # Get all data of the stations
    data = RailNL().data

    # Make new empty route list and add (non-final) route to list of routes
    routes.append([])
    total_time = 0

    # Pick a/the best station as starting point of the route
    routes[-1].append(greedy_option("connections", connections, []))

    # Keep adding stations to the route until ..........
    while greedy_option(key, connections, routes[-1]) != None:
        routes[-1].append(greedy_option(key, connections, routes[-1]))
        update_connections(connections, routes[-1])

        # Check if route meets time constrain, if not end route
        total_time = Route(routes).time
        if total_time > max_time:
            routes[-1] = routes[-1][:-1]
            break

    # Replace route list by final route object in list of routes
    routes[-1] = Route(routes)

    return routes[-1]

def greedy_option(key, connections, route):
    """Determine best destination."""

    # Get current station and all data
    data = RailNL().data

    # Transform route of Station objects to route list of strings
    route_list = []
    for station in route:
        route_list.append(station.name)

    # Choose best option (not yet in route) from current station based on minimum of connections
    if key == "connections":
        # Check if route has station. If so, determine (unused) connections of current station
        if route_list != []:
            options = {}
            for connection in data[route_list[-1]].connections:
                possible_connection = (route_list[-1], connection[0])
                if tuple(sorted(possible_connection)) not in connections["used_connections"]:
                    options[connection[0]] = connections["amount_connections"][connection[0]]
        # All stations possible as starting station
        else:
            options = connections["amount_connections"]

        # If any options, choose best option which has least connections
        if options:
            best_option = data[random.choice([k for k,v in options.items() if v==min(list(options.values()))])]
            return best_option

        return None

    elif key == "quality":
        pass
