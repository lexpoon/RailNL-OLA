class Station(object):
    """ Class that hodls a station and their neighbor stations. """

    def __init__(self, id, name, coordinates, destinations):
        """ Initialise class."""

        self.id = id
        self.name = name
        self.coordinates = self.coordinates(coordinates)
        self.destinations = []
        self.destinations(destinations)

        def coordinates(self, coordinates):
            self.long = coordinates[1]
            self.lat = coordinates[2]
            return

        def destinations(self, destinations):
            for destination in destinations:
                self.destination = Station()
                self.time = destination[1]
            return


        self.destinations = destinations
