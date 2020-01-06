class Connection(object):
    """ Class that hodls a station and their neighbor stations. """

    def __init__(self, origin, destination, time):
        """ Initialise class."""
        self.origin = Station(name=origin)
        self.destination = Station(name=destination)
        self.time = time

    def __str__(self):
        return f"{self.origin} - {self.destination}: {self.time} min"
