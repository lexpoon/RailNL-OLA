from classes.station import Station
from csv import reader


class RailNL():
    """Importing all station and connection data into data dictionary"""

    def __init__(self, map):
        """Create stations and connections for RailNL problem"""

        self.data = {}
        self.stations = self.load_stations(f"data/Stations{map}.csv")
        self.connections = self.load_connections(f"data/Connecties{map}.csv")

    def load_stations(self, filename):
        """Load stations with their coordinates"""

        # Get stations from CSV and add to datastructure
        with open(filename, "r") as f:
            csv_reader = reader(f)
            next(csv_reader, None)
            counter = 0
            for line in csv_reader:
                self.data[line[0]] = Station(counter, line[0], {"long": line[1], "lat": line[2]})
                counter += 1

        return self.data

    def load_connections(self, filename):
        """Load connections between stations with their duration"""

        # Get connections from CSV and add to stations in datastructure
        with open(filename, "r") as f:
            csv_reader = reader(f)

            # Connection goes from both sides, A -> B and B -> A
            for line in csv_reader:
                self.data[line[0]].add_connection(line[1], float(line[2]))
                self.data[line[1]].add_connection(line[0], float(line[2]))

        return self.data


if __name__ == "__main__":
    stations = RailNL()
