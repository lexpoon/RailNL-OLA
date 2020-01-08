class Solution(object):
    """Solution class with a possible output and its score."""

    def __init__(self, data, routes, trains, time):
        """Initial class."""

        self.data = data
        self.max_trains = trains
        self.max_time = time
        self.routes = routes
        self.score = self.score()

    def score(self):
        """Compute score of the solution"""

        p = self.calc_p()
        t = self.calc_t()
        min = self.calc_min()
        score = p*10000 - (t*100 + min)

        return score

    def calc_p(self):
        """Calculate the fraction of the compounds ridden."""

        used_connections = 0
        all_connections = 0

        for station in self.data:
            for connection in station.connections:
                all_connections += 1
                for route in self.routes:
                    if connection == route:
                        used_connections += 1

        p = used_connections / all_connections

        return p

    def calc_t(self):
        """Calculate the number of routes."""

        t = len(self.routes)

        return t
#
    def calc_min(self):
        """Calculate the number of minutes in all sections together."""

        total_time = 0
        for route in self.routes:
            total_time += route.time

        return total_time

    def __str__(self):
        solution = {}
        for route in self.routes:
            solution["train "]
        return f"" + len({length}) + "routes with total time of" + calc_min() + "min and score of" + {self.score}
