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
        # self.stations = self.load_stations(f"data/Stations.csv")
        # self.connections = self.load_connections(f"data/Connections.csv")
        self.data = {}
        self.stations = self.load_stations("StationsNationaal.csv")
        self.connections = self.load_connections("ConnectiesNationaal.csv")

    def load_stations(self, filename):
        """
        Load stations with their coordinates from filename.
        """
        # TEXT
        with open(filename, "r") as f:
            csv_reader = csv.reader(f)
            counter = 0
            for line in csv_reader:
                self.data[line[0]] = {"coordinates": {"long": line[1], "lat": line[2]}, "destinations": []}
                station = Station(counter, line[0], (line[1], line[2]), [])
                counter++

                station.destination

        return self.data

    def load_connections(self, filename):
        """
        Load connections between stations with their duration from filename.
        """
        #
        with open(filename, "r") as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                self.data[line[0]]["destinations"].append({"destination": line[1], "time": line[2]})
                station = Station(name=line[0])
                station.destinations.append((line[1], line[2]))
        return self.data

if __name__ == "__main__":
    stations = RailNL()
    print(stations.data)
