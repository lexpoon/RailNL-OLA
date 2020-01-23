from functions.calculations import all_connections, connections_station, update_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution

import random

def greedy(map, max_routes, max_time, key):
    """ Create solution consisting of routes based on greedy algorithm. """

    # Get all data of the stations
    data = RailNL(map).data

    # Make empty list for all routes
    solution_routes = []

    # Keep track of fraction of used connections
    num_connections = len(all_connections(map))
    connections_dict = connections_station(data)

    # Make greedy routes untill it is not possible anymore due to the constrains
    while len(solution_routes) < max_routes and len(connections_dict["used_connections"]) < num_connections:
        greedy_route(connections_dict, max_time, key, solution_routes, data, map)
        connections_dict = update_connections(solution_routes, data, map)

    # Make solution class and update attributes
    greedy_solution = Solution(solution_routes, map)

    return greedy_solution

def greedy_route(connections, max_time, key, routes, data, map):
    """Create a greedy route."""

    # Make new empty route list and add (non-final) route to list of routes
    routes.append([])
    total_time = 0

    # Pick a/the best station as starting point of the route
    routes[-1].append(greedy_option("connections", routes, data, map))

    # Keep adding stations to the route until ..........
    while greedy_option(key, routes, data, map) != None:
        routes[-1].append(greedy_option(key, routes, data, map))

        # Check if route meets time constrain, if not end route
        total_time = Route(routes, map).time
        if total_time > max_time:
            routes[-1] = routes[-1][:-1]
            break

    # Replace route list by final route object in list of routes
    routes[-1] = Route(routes, map)

    return routes[-1]

def greedy_option(key, routes, data, map):
    """Determine best destination."""

    # Determine amount of connections and used connections for all stations
    routes[-1] = Route(routes[len(routes)-1:], map)
    connections = update_connections(routes, data, map)
    routes[-1] = routes[-1].route

    options = {}

    # Choose best option (not yet in route) from current station based on minimum of connections or time
    if key == "connections" or key == "time":

        # Transform route of Station objects to route list of strings
        route_list = []
        for station in routes[-1]:
            route_list.append(station.name)

        # Check if route has station. If so, determine (unused) connections of current station
        if route_list != []:
            for connection in data[route_list[-1]].connections:
                possible_connection = (route_list[-1], connection[0])
                # Check if connection has not yet been made, then add station to dict with corresponding amount of connections
                if tuple(sorted(possible_connection)) not in connections["used_connections"]:
                    if key == "connections":
                        options[connection[0]] = connections["amount_connections"][connection[0]]
                    elif key == "time":
                        options[connection[0]] = connection[1]
        # All stations possible as starting station
        else:
            options = connections["amount_connections"]

        # If any options, choose best option which has least connections
        if options:
            best_option = data[random.choice([k for k,v in options.items() if v==min(list(options.values()))])]
            return best_option

        return None

    elif key == "quality":
        # Check if route has station. If so, determine (unused) connections of current station
        if routes[-1] != []:
            # Make list of already used connections in current route
            for connection in routes[-1][-1].connections:
                possible_connection = (routes[-1][-1].name, connection[0])
                # Check if connection has not yet been made, then add station to dict with corresponding amount of connections
                if tuple(sorted(possible_connection)) not in connections["used_connections"]:
                    possible_routes = []
                    possible_route = routes[-1].copy()
                    possible_routes.append(possible_route)
                    possible_route.append(data[connection[0]])
                    options[connection[0]] = Route(possible_routes, map).score
        # All stations possible as starting station
        else:
            options = connections["amount_connections"]

        # If any options, choose best option which has least connections
        if options:
            best_option = data[random.choice([k for k,v in options.items() if v==max(list(options.values()))])]
            return best_option

        return None
