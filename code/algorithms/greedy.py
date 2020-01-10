from functions.calculations import calc_stations, calc_connections, calc_used_connections
from functions.import_data import RailNL
from classes.station import Station
from classes.route import Route
from classes.solution import Solution

def greedy(routes, time):
    """ Create solution consisting of routes based on greedy algorithm. """
    