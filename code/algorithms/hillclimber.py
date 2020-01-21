from functions.calculations import calc_stations, calc_connections, calc_used_connections, calc_used_connections_route, connections_station, update_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution
from greedy import greedy

import copy

def hillclimber(routes, time, map, min_score, greedy_output):
    """"Create hillclimber solution based on greedy output"""

    old_score = greedy_output.score

    # Check if routes contribute to overall score
    for route in greedy_output.routes:
        if route.score < min_score:
            # print('slechte route: ',route, route.score)
            greedy_output.routes.remove(route)

    routes = []
    for i in range(len(greedy_output.routes)):
        greedy_output.routes[i] = greedy_output.routes[i].route
        greedy_output.routes[i] = Route(greedy_output.routes[:i+1], map)

    new_score = Solution(greedy_output.routes, map).score
    improvement = old_score - new_score

    print (f"improvement: {improvement} with new score: {new_score}")

    return Solution(greedy_output.routes, map)
