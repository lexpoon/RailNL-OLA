class Station(object):
    """Station class that gives its coordinates and connections."""

    def __init__(self, id, name, coordinates):
        """Initialise class."""

        self.id = id
        self.name = name
        self.coordinates = coordinates
        self.connections = []

    def add_connection(self, destination, time):
        self.connections.append((destination, time))

    def __str__(self):
        return f"{self.name}"
