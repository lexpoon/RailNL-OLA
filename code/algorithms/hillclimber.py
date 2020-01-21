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

    # Check if routes contribute to overall score, else delete route
    for route in greedy_output.routes:
        if route.score < min_score:
            # print('slechte route: ',route, route.score)
            greedy_output.routes.remove(route)

    # Create new route object
    routes = []
    for i in range(len(greedy_output.routes)):
        greedy_output.routes[i] = greedy_output.routes[i].route
        greedy_output.routes[i] = Route(greedy_output.routes[:i+1], map)

    # Calculate new score
    new_score = Solution(greedy_output.routes, map).score
    improvement = old_score - new_score

    print (f"improvement: {improvement} with new score: {new_score}")


    ######## Hillclimber part 2: add unused connection to route #########

    # # Update amount of connections that are left
    # new_route = Solution(greedy_output.routes, map)
    # data = RailNL(map).data
    # connections_left = update_connections(new_route.routes, data, map)['amount_connections']

    # old_score2 = Solution(greedy_output.routes, map).score

    # # Find station in route that has a connection left
    # for route in new_route.routes:
    #     used = calc_used_connections(new_route.routes)
    #     for station in route.route:
    #         if str(station) in connections_left.keys():
    #             if connections_left[str(station)] >= 1:
    #                 index = route.route.index(station)
    #                 first_part = list(route.route[:index])
    #                 last_part = list(route.route[index:])

    #                 # Find neighbour station that is not used
    #                 for tuple in #all possible connections:
    #                     if tuple[0] in connections_left.keys() and tuple[1]==station:
    #                         new_station = tuple[0]
    #                     if tuple[1] in connections_left.keys() and tuple[0]==station:
    #                         new_station = tuple[1]
                                                  
    #                 # Calculate new temp score with station added to route
    #                 route_index = new_route.routes.index(route)
    #                 temp_routes = copy.deepcopy(Solution(greedy_output.routes, map))
    #                 temp = first_part.append([str(station)])
    #                 temp = temp.append(last_part)
    #                 temp_routes.routes[route_index].route = Route(temp, map)
    #                 temp_score = Solution(temp_routes, map).score

    #                 # # If score has improved, add station to actual route
    #                 if temp_score > old_score2:
    #                     updated_route = first_part + new_station + last_part

    # return
    return Solution(greedy_output.routes, map)
