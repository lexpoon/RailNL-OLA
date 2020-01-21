from functions.calculations import calc_stations, calc_connections, calc_used_connections, calc_used_connections_route, connections_station, update_connections
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
            print('Removed route: ', route)

    # Create new route object
    routes = []
    for i in range(len(greedy_output.routes)):
        greedy_output.routes[i] = greedy_output.routes[i].route
        greedy_output.routes[i] = Route(greedy_output.routes[:i+1], map)

    # Calculate new score
    new_score = Solution(greedy_output.routes, map).score
    improvement = new_score - old_score

    print (f"Improvement: {improvement} with new score: {new_score}")

    # If all connections are used, return solution
    unused_connections = calc_connections(map) - calc_used_connections(Solution(greedy_output.routes, map).routes)
    if unused_connections == set():
        return Solution(greedy_output.routes, map)

    data = RailNL(map).data
    solution = Solution(greedy_output.routes, map)

    while True:

        # Update connections that are left
        connections_left = update_connections(solution.routes, data, map)['amount_connections']

        # Find station in route that has an unused connection
        for route in solution.routes:
            for station in route.route:
                if str(station) in connections_left.keys():
                    if connections_left[str(station)] >= 1:
                        index = route.route.index(station)
                        first_part = list(route.route[:index+1])
                        last_part = list(route.route[index:])
                        
                        # Find neighbour station that has no connection
                        unused_connections = calc_connections(map) - calc_used_connections(solution.routes)
                        
                        for connection in unused_connections:
                            if str(connection[0])==str(station):
                                new_station = data[str(connection[1])]

                            if str(connection[1])==str(station):
                                new_station = data[str(connection[0])]
                                                    
                        # Create temporary route with unconnected station added and calculate new score
                        temp_route = first_part + [new_station] + last_part
                        route_index = solution.routes.index(route) 
                        copy_routes = copy.deepcopy(solution)
                        copy_routes.routes[route_index].route = Route([temp_route], map).route
                        temp_score = Solution(copy_routes.routes, map).score
                        score_original = solution.score

                        # If score has improved in temporary route, add station to actual route
                        if temp_score > score_original:
                            greedy_output.routes[route_index] = copy_routes.routes[route_index]
                            solution = Solution(greedy_output.routes, map)

                            print('Old score:', score_original)
                            print('Added station:', new_station)
                            print('Improved new score:', temp_score)
                                                  
                        else:
    
                            solution = 'Final score: ' + str(Solution(greedy_output.routes, map).score)
                            print(solution)
                            return Solution(greedy_output.routes, map)