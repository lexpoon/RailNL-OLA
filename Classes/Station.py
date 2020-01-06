class Station(object):
    """ Class that hodls a station and their neighbor stations. """

    def __init__(self, id, name, coordinates, destinations):
        """ Initialise class."""

        self.id = id
        self.name = name
        self.coordinates = coordinates
        self.destinations = []

    def add_connections(self, destinations):
        for destination in destinations:
            self.destinations.append(Connection(destination[0], destination[1], destination[2]))

    def __str__(self):
        return f"Station {self.name}"
