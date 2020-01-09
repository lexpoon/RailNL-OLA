class Route(object):
    """Route class with a possible train route and its travel time."""

    def __init__(self, id, route):
        """Initial class."""

        self.id = id
        self.route = route
        self.time = self.calc_time()

    def calc_time(self):
        self.time = 0
        for i in range(len(self.route) - 1):
            for connection in self.route[i].connections:
                if connection[0] == self.route[i + 1].name:
                    self.time += int(connection[1])

        return self.time

    def __repr__(self):
        return f"Route {self.id}: {self.route}"
