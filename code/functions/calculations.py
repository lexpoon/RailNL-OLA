import csv

def calc_stations():
    """retrieve info from StationsHolland csv data"""
    with open("data/StationsHolland.csv", "r") as f:
        csv_reader = csv.reader(f)
        num_stations = 0
        for line in csv_reader:
            num_stations += 1
        return num_stations

def calc_connections():
    """retrieve info from ConnectiesHolland csv data"""
    with open("data/ConnectiesHolland.csv", "r") as f:
        csv_reader = csv.reader(f)
        num_connections = 0
        for line in csv_reader:
            num_connections += 1
        return num_connections
