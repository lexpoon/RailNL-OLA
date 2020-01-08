# import functions.helpfunction as help_fn

class Solution(object):
    """Solution class with a possible output and its score."""

    def __init__(self, id, routes):
        """Initial class."""

        self.id = id
        self.routes = routes
        self.time = self.calc_min()
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

        for route in self.routes:
            for connection in route.route:
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
            total_time += route.route.time

        return total_time

    def __str__(self):
        return f"Solution {self.id}, {self.routes}"
