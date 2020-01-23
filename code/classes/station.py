class Station(object):
    """Station class that gives its coordinates and connections"""

    def __init__(self, id, name, coordinates):
        """Initialise class"""

        self.id = id
        self.name = name
        self.coordinates = coordinates
        self.connections = []

    def add_connection(self, destination, time):
        """Add connections to corresponding station"""

        self.connections.append((destination, time))

    def __repr__(self):
        return f"{self.name}"
