from classes.connection import Connection

class Station(object):
    """Station class that gives its coordin and connections."""

    def __init__(self, id, name, coordinates):
        """Initialise class."""

        self.id = id
        self.name = name
        self.coordinates = coordinates
        self.connections = []

    def add_connection(self, origin, destination, time):
        self.connections.append(Connection(origin, destination, time))

    def __str__(self):
        return f"Station {self.name}"
