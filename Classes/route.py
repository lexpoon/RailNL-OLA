class Route(object):
    """Solution class with a possible output and its score."""

    def __init__(self, id, routes):
        """Initial class."""

        self.id = id
        self.route = route
        self.time = calc_time()

    def calc_time(self):
        for connection in self.route:
            self.time += connection.time

    def __str__(self):
        return f"Route {self.id}: {self.route}"
