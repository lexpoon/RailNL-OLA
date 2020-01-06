import sys
import csv
# from station import Station
# from connection import Connection

class RailNL():
    """
    TEXT
    """
    def __init__(self):
        """
        Create rooms and items for the appropriate 'game' version.
        """
        self.stations = self.load_stations(f"Data/StationsHolland.csv")
        self.connections = self.load_connections(f"Data/ConnectiesHolland.csv")
        self.data = {}
        
    def load_stations(self, filename):
        """
        Load stations with their coordinates from filename.
        """
        with open(filename, "r") as f:
            csv_reader = csv.reader(f)
        counter = 0
        for line in csv_reader:
            self.data[line[0]] = Station(counter, line[0], {"long": line[1], "lat": line[2]}, [])
            counter++

        return self.data

    def load_connections(self, filename):
        """
        Load connections between stations with their duration from filename.
        """
        #
        with open(filename, "r") as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                self.data[line[0]].add_connections(line)

        return self.data

if __name__ == "__main__":
    stations = RailNL()
    print(stations.data)
