from classes.route import Route
from classes.solution import Solution
from functions.calculations import all_connections, all_used_connections, update_connections
from functions.import_data import RailNL
import copy

def short_route_swap(map, max_time, min_score, solution_output):
    """"Create hillclimber solution based on solution output"""

    old_score = solution_output.score

    # Delete routes that don't contribute to overall K score
    for route in solution_output.routes:
        if route.score < min_score:
            solution_output.routes.remove(route)

    routes = []
    for i in range(len(solution_output.routes)):
        solution_output.routes[i] = solution_output.routes[i].route
        solution_output.routes[i] = Route(map, solution_output.routes[:i+1])

    # Calculate new K score
    new_score = Solution(map, solution_output.routes).score
    improvement = new_score - old_score

    # Return solution if all connections are already used
    unused_connections = all_connections(map) - all_used_connections(Solution(map, solution_output.routes).routes)
    if unused_connections == set():
        return Solution(map, solution_output.routes)

    # Update connections that are unused
    data = RailNL(map).data
    solution = Solution(map, solution_output.routes)
    connections_left = update_connections(map, data, solution.routes)['amount_connections']

    # Find station in route that can still make new connection
    for traject in solution.routes:
        for station in traject.route:
            if str(station) in connections_left.keys():
                if connections_left[str(station)] >= 1:
                    unused_connections = all_connections(map) - all_used_connections(solution.routes)

                    # Break if all it's connections are used
                    if unused_connections == set():
                        break

                    # Find neighbour station that has no connection
                    for connection in unused_connections:
                        if str(connection[0]) == str(station):
                            new_station = data[str(connection[1])]

                        if str(connection[1]) == str(station):
                            new_station = data[str(connection[0])]

                    # Create temporary route with unconnected station added to calculate new score
                    index = traject.route.index(station)
                    first_part = list(traject.route[:index + 1])
                    last_part = list(traject.route[index:])
                    temp_route = first_part + [new_station] + last_part

                    # Calculate score based on solution with temporary route added
                    copy_routes = copy.deepcopy(solution)
                    route_index = solution.routes.index(traject)
                    copy_routes.routes[route_index].route = Route(map, [temp_route]).route
                    temp_score = Solution(map, copy_routes.routes).score
                    score_original = solution.score

                    # Add station to route if score has improved
                    if temp_score > score_original:
                        solution_output.routes[route_index] = copy_routes.routes[route_index]

                    break

    return Solution(map, solution_output.routes)
