class Station(object):
    """ Class that hodls a station and their neighbor stations. """

    def __init__(self, id, name, coordinates, destinations):
        """ Initialise class."""

        self.id = id
        self.name = name
        self.coordinates = coordinates
        self.destinations = destinations
