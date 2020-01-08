class Connection(object):
    """ Class that hodls a station and their neighbor stations. """

    def __init__(self, origin, destination, time):
        """ Initialise class."""

        self.origin = origin
        self.destination = destination
        self.time = time

    def __str__(self):
        return f"{self.origin} - {self.destination}"
