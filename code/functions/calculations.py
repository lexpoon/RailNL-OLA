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
    """Determine used routes in solution."""

    used_connections = set()
    for route in routes:
        for j in range(len(route.route) - 1):
            connection = (route.route[j].name, route.route[j + 1].name)
            connection = tuple(sorted(connection))
            used_connections.add(connection)

    return used_connections
