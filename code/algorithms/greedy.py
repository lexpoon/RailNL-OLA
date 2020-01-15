from functions.calculations import calc_stations, calc_connections, calc_used_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution

def greedy_solution(routes, time):
    """ Create solution consisting of based on greedy algorithm. """

    # Set algorithm constrains
    max_routes = routes
    max_time = time

    # Get all data of the stations
    data = RailNL().data

    # Make empty list for all routes
    solution_routes = []

    all_connections = calc_connections()
    used_connections = set()

    while len(solution_routes) < max_routes and len(used_connections) < all_connections:
        greedy_route(solution_routes)
        used_connections.update(calc_used_connections(solution_routes))

    # Make solution class and update attributes
    greedy_solution = Solution(solution_routes)

    return greedy_solution

def greedy_route(routes):
    """ Find route based on greedy algorithm. """

    # Get all data of the stations
    data = RailNL().data

    # Make new empty route list
    route_list = []
    total_time = 0

    # Pick random station as starting point of the route
    start = [(key, len(RailNL().data[key].connections)) for key in RailNL().data]
    first_station_start = (min(start, key = lambda t: t[1])[0])

    print (RailNL().data[first_station_start].connections)

    # route_list.append(first_station_start)
    #
    # x = first_station_start
    #
    # print (x)

    # Add (non final) route to list of routes
    routes.append(route_list)

    routes[-1] = Route(routes)

    return routes[-1]

def greedy_destinations(route):
    """Return possible destinations. Not possible to go to a station that is already on the route."""

    # Get current station and all data
    data = RailNL().data
    current_station = route[-1].name

    # Transform route of Station objects to route list of strings
    route_list = []
    for station in route:
        route_list.append(station.name)

    # Make list of all possible connections from current station
    options = []
    for connection in data[current_station].connections:
        if connection[0] not in route_list:
            options.append(data[connection[0]])

    return options
