import csv

def calc_stations():
    """Retrieve info from StationsHolland csv data."""

    with open("data/StationsHolland.csv", "r") as f:
        csv_reader = csv.reader(f)
        num_stations = 0
        for line in csv_reader:
            num_stations += 1

        return num_stations

def calc_connections():
    """Retrieve info from ConnectiesHolland csv data."""

    with open("data/ConnectiesHolland.csv", "r") as f:
        csv_reader = csv.reader(f)
        num_connections = 0
        for line in csv_reader:
            num_connections += 1

        return num_connections

def calc_used_connections(routes):
    """Determine used routes in solution"""

    used_connections = set()
    for i in range(len(routes)):
        for j in range(len(routes[i].route) - 1):
            connection = (routes[i].route[j].name, routes[i].route[j + 1].name)
            connection = sorted(connection)
            connection = tuple(sorted(connection))
            used_connections.add(connection)

    return used_connections
