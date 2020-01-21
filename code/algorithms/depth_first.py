from functions.calculations import calc_stations, calc_connections, calc_used_connections, calc_used_connections_route, connections_station, update_connections, unused_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution
from algorithms.greedy import greedy_option

import random, copy

def depth_first(map, time, routes):
  """Create solution consisting of routes based on depth first algorithm."""

  # Set algorithm constrains
  max_routes = routes
  max_time = time

  # Get all data of  stations of current map
  data = RailNL(map).data

  # Make empty list for all routes
  solution_routes = []

  # Keep track of fraction of used connections
  all_connections = len(calc_connections(map))
  connections_dict = connections_station(data)

  # Make random routes untill it is not possible anymore due to the constrains
  while len(solution_routes) < max_routes and len(connections_dict["used_connections"]) < all_connections:
      depth_first_route(max_time, map, data, solution_routes)
      print(solution_routes)
      connections_dict = update_connections(solution_routes, data, map)

  # Make solution class and update attributes
  depth_first_solution = Solution(solution_routes, map)

  return depth_first_solution

def depth_first_route(max_time, map, data, routes):
    """Create a depth first route."""

    # Starting station of route
    stack = [[]]
    routes.append([])
    stack[0].append(greedy_option("connections", routes, data, map))

    #
    best_route = []
    best_score = -100

    while len(stack) > 0:
        depth_route = stack.pop()
        routes[-1] = depth_route
        if len(depth_route) < 2 or len(depth_route) >= 2 and Route(routes[-1:], map).time < max_time:
            for option in depth_first_options(routes, depth_route, data):
                child = copy.deepcopy(depth_route)
                child.append(option)
                stack.append(child)
                route = Route(stack[-1:], map)
                if route.score > best_score:
                    best_route = route
                    best_score = best_route.score
                elif route.score == best_score:
                    best_route = random.choice([route, best_route])
                    best_score = best_route.score

    routes[-1] = best_route

    return best_route

def depth_first_options(routes, last_station, data):
    """Return possible destinations. Not possible to go to a station that is already on the route"""

    current_station = last_station[-1].name
    connections = []
    for connection in data[current_station].connections:
        possible_connection = (current_station, connection[0])
        if routes == [] or tuple(sorted(possible_connection)) not in calc_used_connections_route(routes):
            connections.append(data[connection[0]])

    return connections
