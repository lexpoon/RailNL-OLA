import csv

def calc_stations():
    """Determine total number of stations in the data."""

    with open("data/StationsHolland.csv", "r") as f:
        csv_reader = csv.reader(f)
        num_stations = 0
        for line in csv_reader:
            num_stations += 1

        return num_stations

def calc_connections():
    """Determine total number of connections in the data."""

    with open("data/ConnectiesHolland.csv", "r") as f:
        csv_reader = csv.reader(f)
        num_connections = 0
        for line in csv_reader:
            num_connections += 1

        return num_connections

def calc_used_connections(routes):
    """Determine used connections in solution."""
    used_connections = set()
    for route in routes:
        for i in range(len(route.route) - 1):
            connection = (route.route[i].name, route.route[i + 1].name)
            connection = tuple(sorted(connection))
            used_connections.add(connection)

    return used_connections

def calc_used_connections_route(routes):
    """Determine used connections in last route."""

    # Check if any route created earlier, and determine used connections
    if len(routes) > 1:
        already_used_connections = calc_used_connections(routes[:-1])
    else:
        already_used_connections = set()

    # Create set of new connections in this route
    used_connections = set()

    for i in range(len(routes[-1]) - 1):
        connection = (routes[-1][i].name, routes[-1][i + 1].name)
        connection = tuple(sorted(connection))
        if connection not in already_used_connections:
            used_connections.add(connection)

    return used_connections
