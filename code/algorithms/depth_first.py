from algorithms.greedy import greedy_option
from classes.route import Route
from classes.solution import Solution
from copy import deepcopy
from functions.calculations import all_connections, all_used_connections_route, connections_station, update_connections, choose_best_route
from functions.import_data import RailNL


def depth_first(map, max_routes, max_time, min_score, depth, ratio):
    """Create solution consisting of set of routes based on depth first algorithm"""

    # Get all data from stations in current map
    data = RailNL(map).data

    # Create list where routes can be added
    routes = []

    # Keep track of fraction of used connections
    num_connections = len(all_connections(map))
    connections = connections_station(data)

    # Make random routes until it is not possible anymore due to the constrains
    while len(routes) < max_routes and len(connections["used_connections"]) < num_connections:
        depth_first_route(map, max_time, min_score, data, routes, depth, ratio, definition=None)
        connections = update_connections(map, data, routes)

    return Solution(map, routes)


def depth_first_route(map, max_time, min_score, data, routes, depth, ratio, definition):
    """Create a depth first route"""

    # Starting station of route
    routes.append([])
    stack = [[greedy_option(map, data, routes, "connections")]]

    # Set details for best route with depth first algorithm
    best_route = Route(map, stack)

    # Keep searching for routes until no feasible options
    while len(stack) > 0:

        # Get top route/station from tree of routes
        state = stack.pop()
        routes[-1] = state

        # Find each possible child from state and add to tree of routes
        if routes[-1][-1] != None and depth_first_options(data, routes, definition) != None:
            for option in depth_first_options(data, routes, definition):
                child = deepcopy(state)
                child.append(option)
                routes[-1] = child
                route = Route(map, routes)

                # Check time constrains for route
                if route.time < max_time:
                    stack.append(child)

                    # Apply Greedy look-ahead with minimal score or with score-route length ratio
                    if len(route.route) > depth and (route.score < min_score
                            or ratio * route.score/len(route.route)
                            < best_route.score/len(best_route.route)):
                        stack.pop()

                    # Check if route is best solution yet
                    best_route = choose_best_route(route, best_route)

    routes[-1] = best_route

    return best_route


def depth_first_options(data, routes, definition):
    """Return possible destinations. Not possible to go to a station that is already on the route"""

    # Set details for possible destionations
    current_station = routes[-1][-1].name
    connections = []

    # Get all possible destionations from current station
    for connection in data[current_station].connections:
        possible_connection = (current_station, connection[0])

        # Only use optimal pruning based on archiving used connections, when creating solution
        if definition == None or (definition == "improve" and (routes == [] or tuple(sorted(possible_connection)) not in all_used_connections_route(routes))):
            connections.append(data[connection[0]])

    if connections == []:
        return None

    return connections
