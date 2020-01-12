from functions.calculations import calc_stations, calc_connections, calc_used_connections

class Solution(object):
    """Solution class with a possible output and its score."""

    def __init__(self, routes):
        """Initial class."""

        self.routes = routes
        self.time = self.calc_min()
        self.score = self.score()

    def score(self):
        """Compute score of the solution"""

        p = self.calc_p()
        t = self.calc_t()
        min = self.calc_min()

        score = p*10000 - (t*100 + min)

        return round(score)

    def calc_p(self):
        """Calculate the fraction of the compounds ridden."""

        used_connections = len(calc_used_connections(self.routes))
        all_connections = calc_connections()

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
