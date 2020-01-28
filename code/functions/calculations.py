import csv
from random import choice as rd_choice


def all_stations(map):
    """Determine the stations based on map"""

    # Get stations by lines of CSV file
    with open(f"data/Stations{map}.csv", "r") as f:
        csv_reader = csv.reader(f)
        stations = set()
        for line in csv_reader:
            stations.add(line)

        return stations


def all_connections(map):
    """Determine the connections based on map"""

    # Get connections of map from CSV file
    with open(f"data/Connecties{map}.csv", "r") as f:
        csv_reader = csv.reader(f)
        connections = set()

        # Remove duplicate connections
        for line in csv_reader:
            connection = (line[0], line[1])
            connection = tuple(sorted(connection))
            connections.add(connection)

        return connections


def all_used_connections(routes):
    """Determine used connections in solution"""

    used_connections = set()

    # Find all used routes in solution and remove duplicates
    for route in routes:
        for i in range(len(route.route) - 1):
            connection = (route.route[i].name, route.route[i + 1].name)
            connection = tuple(sorted(connection))
            used_connections.add(connection)

    return used_connections


def all_used_connections_route(routes):
    """Determine new used connections in last route"""

    # Check if any was route created earlier, and determine used connections
    if len(routes) > 1:
        already_used_connections = all_used_connections(routes[:-1])
    else:
        already_used_connections = set()

    # Create set of new connections in this route
    used_connections = set()

    # Find used routes and remove duplicates
    for i in range(len(routes[-1]) - 1):
        connection = (routes[-1][i].name, routes[-1][i + 1].name)
        connection = tuple(sorted(connection))
        if connection not in already_used_connections:
            used_connections.add(connection)

    return used_connections


def connections_station(data):
    """Determine overview of amount of connections for each station based on used connections"""

    connections = {"amount_connections": {}, "used_connections": set()}

    # Add number of connections value to dict
    for key in data.keys():
        connections["amount_connections"][key] = len(data[key].connections)

    return connections


def update_connections(map, data, routes):
    """Update amount of possible connections with new station in route"""

    # Get overview of amount of connections and used connections
    connections = connections_station(data)

    # Decrease number of connections of station after making a connection in route
    for route in routes:

        # Check if connections are made in route
        if len(route.route) >= 2:
            for i in range(1, len(route.route)):

                # Check if connection already been used
                if tuple(sorted((route.route[i - 1].name, route.route[i].name))) not in connections["used_connections"]:

                    # Add to set of used connections
                    new_connection = tuple(sorted((route.route[i - 1].name, route.route[i].name)))
                    connections["used_connections"].add(new_connection)

                    # Decrease amount of connections from origin by 1
                    # Delete station if every posible connection is used
                    if route.route[i - 1].name in connections["amount_connections"].keys():
                        connections["amount_connections"][route.route[i - 1].name] -= 1
                        if connections["amount_connections"][route.route[i - 1].name] == 0:
                            connections["amount_connections"].pop(route.route[i - 1].name)

                    # Decrease amount of connections from destination by 1
                    # Delete station if every posible connection is used
                    if route.route[i].name in connections["amount_connections"].keys():
                        connections["amount_connections"][route.route[i].name] -= 1
                        if connections["amount_connections"][route.route[i].name] == 0:
                            connections["amount_connections"].pop(route.route[i].name)

    return connections

def choose_best_route(route, best_route):
    """Return route with best score"""

    if route.score > best_route.score:
        best_route = route
    elif route.score == best_route.score:
        best_route = rd_choice([route, best_route])

    return best_route

def convert_object_to_string(route):
    """Convert a route of station objects to a route of station names"""

    route_list = []
    for station in route.route:
        route_list.append(station.name)

    return route_list

def remove_routes(solution, change_routes):
    """Remove routes of the solution"""

    while change_routes > 0:
        route = rd_choice(solution.routes)
        solution.routes.remove(route)
        change_routes -= 1

        while depending_route_options(solution.routes, route) != [] and change_routes > 0:
            options = depending_route_options(solution.routes, route)
            option = rd_choice(options)
            solution.routes.remove(option)
            change_routes -= 1

    return solution

def depending_route_options(routes, main_route):
    """Return routes which are connected to the main route"""

    options = set()
    main_route = convert_object_to_string(main_route)

    for route in routes:
        for station1 in main_route:
            for station in route.route:
                if station.name == station1:
                    options.add(route)
                    break

    return list(options)
