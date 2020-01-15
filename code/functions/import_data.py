import sys, csv
from classes.station import Station
from classes.route import Route
from classes.solution import Solution

class RailNL():
    """Importing all station and connection data into data dictionary."""

    def __init__(self):
        """Create rooms and items for the appropriate 'game' version."""

        self.data = {}

        self.stations = self.load_stations(f"data/StationsHolland.csv")
        self.connections = self.load_connections(f"data/ConnectiesHolland.csv")

    def load_stations(self, filename):
        """Load stations with their coordinates from filename."""

        with open(filename, "r") as f:
            csv_reader = csv.reader(f)
            next(csv_reader, None)  # skip the header
            counter = 0
            for line in csv_reader:
                self.data[line[0]] = Station(counter, line[0], {"long": line[1], "lat": line[2]})
                counter += 1

        return self.data

    def load_connections(self, filename):
        """Load connections between stations with their duration from filename."""

        with open(filename, "r") as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                self.data[line[0]].add_connection(line[1], line[2])
                self.data[line[1]].add_connection(line[0], line[2])

        return self.data

if __name__ == "__main__":
    stations = RailNL()
