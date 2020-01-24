from algorithms.greedy import greedy_option
from classes.route import Route
from classes.solution import Solution
from functions.calculations import all_connections, all_used_connections_route, connections_station, update_connections
from functions.import_data import RailNL

import copy
import random


def depth_first(map, max_routes, max_time, min_score, depth, ratio):
    """Create solution consisting of routes based on depth first algorithm"""

    # Get all data of  stations of current map
    data = RailNL(map).data

    # Make empty list for all routes
    solution_routes = []

    # Keep track of fraction of used connections
    num_connections = len(all_connections(map))
    connections_dict = connections_station(data)

    # Make random routes untill it is not possible anymore due to the constrains
    while len(solution_routes) < max_routes and len(connections_dict["used_connections"]) < num_connections:
        depth_first_route(max_time, map, data, solution_routes, depth, min_score, ratio)
        connections_dict = update_connections(solution_routes, data, map)

    # Make solution class and update attributes
    depth_first_solution = Solution(solution_routes, map)

    return depth_first_solution


def depth_first_route(max_time, map, data, routes, depth, min_score, ratio):
    """Create a depth first route"""

    # Starting station of route
    routes.append([])
    stack = [[greedy_option("connections", routes, data, map)]]

    # Set details for best route with depth first algorithm
    best_route = []
    best_score = -100

    # Keep searching for routes until no feasible options
    while len(stack) > 0:

        # Get top route/station from tree of routes
        state = stack.pop()
        routes[-1] = state

        # Check time constrains for route
        if len(state) < 2 or len(state) >= 2 and Route(routes[-1:], map).time < max_time:

            # Find each possible child from state and add to tree of routes
            for option in depth_first_options(routes, state, data):
                child = copy.deepcopy(state)
                child.append(option)
                stack.append(child)
                routes[-1] = child
                route = Route(routes, map)

                # Apply Greedy look-ahead with minimal score or with score-route length ratio
                if len(route.route) > depth and (route.score < min_score or ratio * route.score/len(route.route) < best_score/len(best_route.route)):
                    stack.pop()

                # Check if route is best solution yet
                if route.score > best_score:
                    best_route = route
                    best_score = best_route.score
                elif route.score == best_score:
                    best_route = random.choice([route, best_route])
                    best_score = best_route.score

    routes[-1] = best_route

    return best_route


def depth_first_options(routes, route, data):
    """Return possible destinations. Not possible to go to a station that is already on the route"""

    # Set details for possible destionations
    current_station = route[-1].name
    connections = []

    # Get all possible destionations from current station
    for connection in data[current_station].connections:
        possible_connection = (current_station, connection[0])

        # Optimal pruning based on archiving used connections
        if routes == [] or tuple(sorted(possible_connection)) not in all_used_connections_route(routes):
            connections.append(data[connection[0]])

    return connections
