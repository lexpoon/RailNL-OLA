from functions.calculations import calc_stations, calc_connections, calc_used_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution

def greedy(routes, time):
    """ Create solution consisting of routes based on greedy algorithm. """
    
    max_routes = routes
    max_time = time

    data = RailNL().data
    solution = {}
    solution["routes"] = []

    # Number of connections in data
    all_connections = calc_connections()
    used_connections = set()

    # While max routes not reached AND not all connections are used
    while len(solution["routes"]) < max_routes and len(used_connections) < all_connections:
        solution["routes"].append(greedy_route(solution))
        used_connections.update(calc_used_connections(solution["routes"]))

    greedy_solution = Solution(solution["routes"])
    solution["time"] = greedy_solution.time
    solution["quality"] = greedy_solution.score

    return greedy_solution

def greedy_solution(solution):
    """ Find route based on greedy algorithm. """

    data = RailNL().data
    route_list = []
    total_time = 0

    route_list.append(data[random.choice(list(data.keys()))])



    return route_list


