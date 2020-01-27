from algorithms.greedy import greedy_option
from classes.route import Route
from classes.solution import Solution
from functions.calculations import all_connections, connections_station, update_connections
from functions.import_data import RailNL

import random

def randomize(map, max_routes, max_time):
    """Create solution consisting of random routes"""

    # Get all data of  stations of current map
    data = RailNL(map).data

    # Make empty list for all routes
    routes = []

    # Keep track of fraction of used connections
    num_connections = len(all_connections(map))
    connections = connections_station(data)

    # Make random routes untill it is not possible anymore due to the constrains
    while len(routes) < max_routes and len(connections["used_connections"]) < num_connections:
        random_route(map, max_time, data, routes)
        connections = update_connections(map, data, routes)

    # Make solution class and update attributes
    random_solution = Solution(map, routes)

    return random_solution


def random_route(map, max_time, data, routes):
    """Randomize a route"""

    # Make new empty route list and add (non-final) route to list of routes
    routes.append([])
    total_time = 0

    # Pick a/the best station as starting point of the route
    routes[-1].append(greedy_option(map, data, routes, "connections"))

    # Keep adding stations to the route until no more possible destinations
    while random_options(map, data, routes) != None:
        routes[-1].append(random_options(map, data, routes))

        # Check if route meets time constrain, if not end route
        total_time = Route(map, routes).time
        if total_time > max_time:
            routes[-1] = routes[-1][:-1]
            break

    # Replace route list by final route object in list of routes
    routes[-1] = Route(map, routes)

    return routes[-1]


def random_options(map, data, routes):
    """Return possible destinations. Not possible to go to a station that is already on the route"""

    # Determine amount of connections and used connections for all Stations
    routes[-1] = Route(map, routes[len(routes)-1:])
    connections = update_connections(map, data, routes)
    routes[-1] = routes[-1].route

    # Transform route of Station objects to route list of strings
    route_list = []
    for station in routes[-1]:
        route_list.append(station.name)

    # Determine all possible connections from current station
    options = []
    for connection in data[route_list[-1]].connections:
        possible_connection = (route_list[-1], connection[0])
        if tuple(sorted(possible_connection)) not in connections["used_connections"]:
            options.append(connection[0])

    # If any options, return random option
    if options:
        random_option = data[random.choice(options)]
        return random_option

    return None
