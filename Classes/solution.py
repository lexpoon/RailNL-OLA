class Solution(object):
    """Solution class with a possible output and its score."""

    def __init__(self, data, routes, trains, time):
        """Initial class."""

        self.data = data
        self.routes = routes
        self.max_trains = trains
        self.max_time = time
        self.score = self.score()

    def score(self):
        """Compute score of the solution"""

        p = self.calc_p()
        t = self.calc_t()
        min = self.calc_min()
        self.score = p*10000 - (t*100 + min)

        return score

    def calc_p(self):
        """Calculate the fraction of the compounds ridden."""

        used_connections = 0
        all_connections = 0

        for station in self.data:
            for destination in station.destinations:
                all_connections += 1
                for connection in self.routes:
                    if destination == connection:
                        used_connections += 1

        p = used_connections / all_connections

        return p

#     def calc_t(self):
#         """Calculate the number of routes."""
#
#
#
#         return t
#
#     def calc_min(self):
#         """Calculate the number of minutes in all sections together."""
#
#
#
#         return min
#
#     def __str__(self):
#         return f"{}
#
# routes = {
#     "1": {"route": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)], "time": 100}
#     "2": [Connection(1), Connection(2), Connection(3), Connection(4)]
#     "3": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5), ]
#     "4": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)]
#     "5": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)]
#     "6": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)]
#     "7": [Connection(1), Connection(2), Connection(3), Connection(4), Connection(5)]
# }
