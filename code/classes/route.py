from functions.calculations import all_connections, all_used_connections_route


class Route(object):
    """Route class with a possible train route and its travel time."""

    def __init__(self, map, routes):
        """Initial class"""

        self.id = len(routes)
        self.route = routes[-1]
        self.time = self.calc_time()
        self.score = self.calc_score(map, routes)

    def calc_time(self):
        """Determine traveling time of complete route."""

        # Set start time of route
        self.time = 0

        # Get total route time by sum of each connection's duration
        for i in range(len(self.route) - 1):
            for connection in self.route[i].connections:
                if connection[0] == self.route[i + 1].name:
                    self.time += int(connection[1])

        return self.time

    def calc_score(self, map, routes):
        """Determine score of current route."""

        # Fraction of based on used connections
        p = len(all_used_connections_route(routes)) / len(all_connections(map))

        # Formula to calcucate the quality of route
        self.score = 10000 * p - (100 + self.time)

        return self.score

    def __repr__(self):
        return f"Route {self.id} ({self.time} min.): {self.route}"
