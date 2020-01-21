from functions.calculations import calc_stations, calc_connections, calc_used_connections, calc_used_connections_route

class Route(object):
    """Route class with a possible train route and its travel time."""

    def __init__(self, routes, map):
        """Initial class."""

        self.id = len(routes)
        self.route = routes[-1]
        self.time = self.calc_time()
        self.score = self.calc_score(routes, map)

    def calc_time(self):
        """Determine traveling time of complete route."""

        self.time = 0
        for i in range(len(self.route) - 1):
            for connection in self.route[i].connections:
                if connection[0] == self.route[i + 1].name:
                    self.time += int(connection[1])

        return self.time

    def calc_score(self, routes, map):
        """Determine score of current route."""

        p = len(calc_used_connections_route(routes)) / len(calc_connections(map))
        self.score = 10000 * p - (100 + self.time)

        return self.score

    def __repr__(self):
        return f"Route {self.id}: {self.route}"
