from functions.calculations import all_connections, all_used_connections


class Solution(object):
    """Solution class with a possible output and its score."""

    def __init__(self, map, routes):
        """Initial class"""

        self.routes = routes
        self.time = self.calc_min()
        self.score = self.score(map)

    def score(self, map):
        """Compute score of the solution"""

        p = self.calc_p(map)
        t = self.calc_t()
        min = self.calc_min()

        # Formula to calcucate the quality over all routes
        score = p * 10000 - (t * 100 + min)

        return round(score)

    def calc_p(self, map):
        """Calculate the fraction of used connections."""

        used_connections = len(all_used_connections(self.routes))
        total_num_connections = len(all_connections(map))
        p = used_connections / total_num_connections

        return p

    def calc_t(self):
        """Calculate the number of routes."""

        t = len(self.routes)

        return t

    def calc_min(self):
        """Calculate the number of minutes in all sections together."""

        total_time = 0

        # Get total time by sum of time of all routes
        for route in self.routes:
            total_time += route.time

        return total_time

    def __repr__(self):
        return f"Solution ({self.score}/10000): {self.routes}"
