from functions.calculations import calc_connections, calc_used_connections, calc_used_connections_route

class Solution(object):
    """Solution class with a possible output and its score."""

    def __init__(self, routes, map):
        """Initial class."""

        self.routes = routes
        self.time = self.calc_min()
        self.score = self.score(map)

    def score(self, map):
        """Compute score of the solution"""

        p = self.calc_p(map)
        t = self.calc_t()
        min = self.calc_min()

        score = p*10000 - (t*100 + min)

        return round(score)

    def calc_p(self, map):
        """Calculate the fraction of the compounds ridden."""

        used_connections = len(calc_used_connections(self.routes))
        all_connections = len(calc_connections(map))

        p = used_connections / all_connections

        return p

    def calc_t(self):
        """Calculate the number of routes."""

        t = len(self.routes)

        return t

    def calc_min(self):
        """Calculate the number of minutes in all sections together."""

        total_time = 0
        for route in self.routes:
            total_time += route.time

        return total_time

    def __repr__(self):
        return f"Solution ({self.score}/10000): {self.routes}"
