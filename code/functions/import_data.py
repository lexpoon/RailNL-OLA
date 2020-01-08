import sys, csv
from classes.station import Station
from classes.connection import Connection
from classes.solution import Solution

class RailNL():
    """
    TEXT
    """
    def __init__(self, map):
        """
        Create rooms and items for the appropriate 'game' version.
        """
        self.data = {}
        self.stations = self.load_stations(f"data/Stations{map}.csv")
        self.connections = self.load_connections(f"data/Connecties{map}.csv")

    def load_stations(self, filename):
        """
        Load stations with their coordinates from filename.
        """
        with open(filename, "r") as f:
            csv_reader = csv.reader(f)
            counter = 0
            for line in csv_reader:
                self.data[line[0]] = Station(counter, line[0], {"long": line[1], "lat": line[2]})
                counter += 1

        return self.data

    def load_connections(self, filename):
        """
        Load connections between stations with their duration from filename.
        """
        with open(filename, "r") as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                self.data[line[0]].add_connection(self.data[line[0]], self.data[line[1]], line[2])
                self.data[line[1]].add_connection(self.data[line[1]], self.data[line[0]], line[2])
        return self.data

if __name__ == "__main__":
    stations = RailNL()

    # for station in stations.data:
    #     stat = stations.data[station]
    #     print(f"Station {stat.id}: {stat.name}")
    #     print(f"Coordinates: {stat.coordinates['long']}, {stat.coordinates['lat']}")
    #     if len(stat.connections) > 0:
    #         print("Connections:")
    #     else:
    #         print("No connections")
    #     for destination in stat.connections:
    #         print(f"- {destination.origin} - {destination.destination}: {destination.time} min")
    #     print("----------------------------------------------------------------------------")
    # print(stations.data)
