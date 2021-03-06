from classes.route import Route
from classes.solution import Solution
from functions.calculations import all_connections, connections_station, convert_object_to_string, update_connections
from functions.import_data import RailNL
from random import choice as rd_choice


def greedy(map, max_routes, max_time, key):
    """Create solution consisting of routes based on greedy algorithm.

    Keyword arguments:
    key (str)       options: [Connections, Time, Score]. Method Greedy makes choices
    """

    # Get all data from stations in map
    data = RailNL(map).data

    # Create list where routes can be added
    routes = []

    # Keep track of fraction of used connections
    num_connections = len(all_connections(map))
    connections = connections_station(data)

    # Make greedy routes until it is not possible anymore due to the constrains
    while len(routes) < max_routes and len(connections["used_connections"]) < num_connections:
        greedy_route(map, max_time, data, routes, key)
        connections = update_connections(map, data, routes)

    return Solution(map, routes)


def greedy_route(map, max_time, data, routes, key):
    """Create a greedy route.

    Keyword arguments:
    key (str)       options:[Connections, Time, Score]. Method Greedy makes choices
    """

    # Make new empty route list and add (non-final) route to list of routes
    routes.append([])

    # Pick a/the best station as starting point of the route
    routes[-1].append(greedy_option(map, data, routes, "connections"))

    # Keep adding stations to the route until constraints are met
    while greedy_option(map, data, routes, key) != None:
        routes[-1].append(greedy_option(map, data, routes, key))

        # Check if route meets time constrain
        total_time = Route(map, routes).time
        if total_time > max_time:
            routes[-1] = routes[-1][:-1]
            break

    # Replace route list by final route object in list of routes
    routes[-1] = Route(map, routes)

    return routes[-1]


def greedy_option(map, data, routes, key):
    """Determine best destination.

    Keyword arguments:
    key (str)       options:[Connections, Time, Score]. Method Greedy makes choices
    """

    # Determine amount of connections and used connections for all stations
    routes[-1] = Route(map, routes[len(routes)-1:])
    connections = update_connections(map, data, routes)
    routes[-1] = routes[-1].route

    options = {}

    # Choose best option (not yet in route) from current station based on minimum of connections or time
    if key == "connections" or key == "time":

        # Convert route of Station objects to route list of strings
        route_list = convert_object_to_string(routes[-1])

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
            best_option = data[rd_choice([k for k, v in options.items() if v == min(list(options.values()))])]
            return best_option

        return None

    elif key == "score":

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
                    options[connection[0]] = Route(map, possible_routes).score

        # All stations possible as starting station
        else:
            options = connections["amount_connections"]

        # If any options, choose best option which has least connections
        if options:
            best_option = data[rd_choice([k for k, v in options.items() if v == max(list(options.values()))])]
            return best_option

        return None
