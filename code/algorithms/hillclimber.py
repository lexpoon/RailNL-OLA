from functions.calculations import calc_connections, calc_used_connections, calc_used_connections_route, connections_station, update_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution
from greedy import greedy

import copy
import random

def hillclimber(greedy_output, time, map, min_score):
    """"Create hillclimber solution based on greedy output"""

    old_score = greedy_output.score

    # Check if routes contribute to overall score, else delete route
    for route in greedy_output.routes:
        if route.score < min_score:
            greedy_output.routes.remove(route)
            print('Removed route: ', route)

    # Create new route object
    routes = []
    for i in range(len(greedy_output.routes)):
        greedy_output.routes[i] = greedy_output.routes[i].route
        greedy_output.routes[i] = Route(greedy_output.routes[:i+1], map)

    # Calculate new score
    new_score = Solution(greedy_output.routes, map).score
    improvement = new_score - old_score

    print (f"First improvement: {improvement} with new score: {new_score}")

    # If all connections are used, return solution
    unused_connections = calc_connections(map) - calc_used_connections(Solution(greedy_output.routes, map).routes)
    if unused_connections == set():
        return Solution(greedy_output.routes, map)

    data = RailNL(map).data
    solution = Solution(greedy_output.routes, map)

    improving = True

    while True:

        solution = Solution(greedy_output.routes, map)

        # Update connections that are left
        connections_left = update_connections(solution.routes, data, map)['amount_connections']

        # Find station in route that has an unused connection
        for traject in solution.routes:
            for station in traject.route:
                if str(station) in connections_left.keys():
                    if connections_left[str(station)] >= 1:
                        index = traject.route.index(station)
                        first_part = list(traject.route[:index+1])
                        last_part = list(traject.route[index:])

                        # Find neighbour station that has no connection
                        unused_connections = calc_connections(map) - calc_used_connections(solution.routes)

                        if unused_connections == set():
                            return False
                            print('no unused connections anymore')
                            # improving = False

                        for connection in unused_connections:
                            if str(connection[0])==str(station):
                                new_station = data[str(connection[1])]

                            if str(connection[1])==str(station):
                                new_station = data[str(connection[0])]

                        # Create temporary route with unconnected station added and calculate new score
                        temp_route = first_part + [new_station] + last_part
                        route_index = solution.routes.index(traject)
                        copy_routes = copy.deepcopy(solution)
                        copy_routes.routes[route_index].route = Route([temp_route], map).route
                        temp_score = Solution(copy_routes.routes, map).score
                        score_original = solution.score

                        # If score has improved in temporary route, add station to actual route
                        if temp_score > score_original:
                            greedy_output.routes[route_index] = copy_routes.routes[route_index]
                            solution = Solution(greedy_output.routes, map)
                            print('Added station:', new_station)
                            print('Improved to:', temp_score)
                            # continue

                        else:
                            return False
                            print('not improving, end while loop')
                            # improving = False
                            test(greedy_output.routes, map)
                            # break

    # s = ('Final score: ', str(Solution(greedy_output.routes, map).score))
    # return s

    # print(Solution(greedy_output.routes, map))

# def test(solution, map):
#     print(Solution(greedy_output.routes, map))

    # for i in range(20):

    #     # Create list of stations that are end/begin stations and have more than 1 possible connection
    #     stations = []
    #     for traject in greedy_output.routes:
    #         for station in traject.route:
    #             if (traject.route.index(station)==0 or traject.route.index(station)==len(traject.route)) and len(station.connections) > 1:
    #                 stations.append(station)

    #     # Get random station from stations list
    #     station = random.choice(stations)

    #     # Find route to which random station belongs
    #     route_object = [traject for traject in greedy_output.routes if (station in traject.route) and (traject.route.index(station)==0 or traject.route.index(station)==len(traject.route)) and len(station.connections)>1][0]
    #     route_list = route_object.route
    #     route_index = greedy_output.routes.index(route_object)

    #     # Randomly choose station to connect with
    #     connection = random.choice(station.connections)

        # Create new route with station added at the start or end of the original route
        # if route_list.index(station) == len(route_list):
        #     # new_connection = (station, connection[0])
        #     new_station = str(connection[0])
        #     print('---', new_station)
        #     print('///', route_list)
        #     new_route = route_list.append(new_station)
        #     print('new route:', new_route)
        #     # if Route(new_route).time < time:
        #     print('Swapped: ', new_station)
        #     greedy_output.routes[route_index].route = Route(new_route, map).route

        # if route_list.index(station) == 0:
        #     # new_connection = (connection[0], station)
        #     new_station = str(connection[0])
        #     print('---', new_station)
        #     print('///', route_list)
        #     # print('list:',route_list)
        #     # print('connection:',connection[0])
        #     new_route = [new_station] + route_list
        #     print('new route:', new_route)
        #     # if ...:
        #     print('Swapped: ', new_station)
        #     greedy_output.routes[route_index].route = Route(new_route, map).route

        # check op tijd
        # als je in het midden komt,


        # Delete first or last station from route
        # for route in greedy_output.routes:
        #     for connection in route.route:
        #         if connection = new_connection:
        #             if new_connection[0] == station:
        #                 routes[route].route = route[:-1]
        #             routes[route].route = route[1:]

        # solution = solution

        # return Solution(greedy_output.routes, map)
