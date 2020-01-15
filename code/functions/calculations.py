import csv

def calc_stations(map):
    """Determine total number of stations in the data."""

    with open(f"data/Stations{map}.csv", "r") as f:
        csv_reader = csv.reader(f)
        num_stations = 0
        for line in csv_reader:
            num_stations += 1

        return num_stations

def calc_connections(map):
    """Determine total number of connections in the data."""

    with open(f"data/Connecties{map}.csv", "r") as f:
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

def connections_station(data):
    """Determine overview of amount of connections for each station based on used connections."""

    connections = {"amount_connections": {}, "used_connections": set()}

    for key in data.keys():
        connections["amount_connections"][key] = len(data[key].connections)

    return connections

def update_connections(connections, route):
    """Update amount of possible connections with new station in route."""

    # Decrease amount of connections for both stations in each connection in route
    connections["amount_connections"][route[-1].name] -= 1
    connections["amount_connections"][route[-2].name] -= 1

    # Delete station if no connection possible anymore
    if connections["amount_connections"][route[-1].name] == 0:
            connections["amount_connections"].pop(route[-1].name)
    if connections["amount_connections"][route[-2].name] == 0:
            connections["amount_connections"].pop(route[-2].name)

    # Update used connections
    if len(route) > 1:
        last_connection = (route[-1].name, route[-2].name)
        last_connection = tuple(sorted(last_connection))
        connections["used_connections"].add(last_connection)

    return connections
