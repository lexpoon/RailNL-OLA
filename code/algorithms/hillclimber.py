from functions.calculations import all_connections, all_used_connections, update_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution
from greedy import greedy

import copy

def hillclimber(greedy_output, time, map, min_score):
    """"Create hillclimber solution based on greedy output"""

    old_score = greedy_output.score

    # Check if routes contribute to overall score, else delete route
    for route in greedy_output.routes:
        if route.score < min_score:
            greedy_output.routes.remove(route)

    # Update route object
    routes = []
    for i in range(len(greedy_output.routes)):
        greedy_output.routes[i] = greedy_output.routes[i].route
        greedy_output.routes[i] = Route(greedy_output.routes[:i+1], map)

    # Calculate new score
    new_score = Solution(greedy_output.routes, map).score
    improvement = new_score - old_score

    # If all connections are already used, return solution
    unused_connections = all_connections(map) - all_used_connections(Solution(greedy_output.routes, map).routes)
    if unused_connections == set():
        return Solution(greedy_output.routes, map)

    # Update connections that are unused
    data = RailNL(map).data
    solution = Solution(greedy_output.routes, map)
    connections_left = update_connections(solution.routes, data, map)['amount_connections']

    # Find station in route that has an unused connection
    for traject in solution.routes:
        for station in traject.route:
            if str(station) in connections_left.keys():
                if connections_left[str(station)] >= 1:

                    # Create set of tuples with unused connections
                    unused_connections = all_connections(map) - all_used_connections(solution.routes)

                    # If all connections are used, break
                    if unused_connections == set():
                        break

                    # Find neighbour station that has no connection
                    for connection in unused_connections:
                        if str(connection[0])==str(station):
                            new_station = data[str(connection[1])]

                        if str(connection[1])==str(station):
                            new_station = data[str(connection[0])]

                    # Create temporary route with unconnected station added and calculate new score
                    index = traject.route.index(station)
                    first_part = list(traject.route[:index+1])
                    last_part = list(traject.route[index:])
                    temp_route = first_part + [new_station] + last_part

                    # Calculate score based on temporary route added to solution
                    copy_routes = copy.deepcopy(solution)
                    route_index = solution.routes.index(traject)
                    copy_routes.routes[route_index].route = Route([temp_route], map).route
                    temp_score = Solution(copy_routes.routes, map).score
                    score_original = solution.score

                    # If score has improved in temporary route, add station to actual route
                    if temp_score > score_original:
                        greedy_output.routes[route_index] = copy_routes.routes[route_index]

                    break

    return Solution(greedy_output.routes, map)
