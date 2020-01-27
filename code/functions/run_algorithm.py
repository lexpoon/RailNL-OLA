from solution import Solution
from import_data import RailNL
from functions.calculations import all_connections, connections_station, update_connections
from randomize import randomize
from greedy import greedy
from depth_first import depth_first
from breadth_first import breadth_first
from short_route_swap import short_route_swap
from hillclimber import hillclimber
from simulated_annealing import simulated_annealing
from visualize import visualisation

def run_algorithm(map, max_routes, max_time, solution, algorithm, iterations, key, depth, ratio, remove_routes, formula, definition):
    """Run algorithm of choice for user"""
    
    data = RailNL(map).data
    min_score = 10000/len(all_connections(map)) - 105

    # Run algorithm based on input
    if definition == 'create':
        solution_algorithm = start_algorithm(map, max_routes, max_time, min_score, algorithm, iterations, key, depth, ratio)
    else:
        solution_algorithm = improve_algorithm(map, max_routes, max_time, min_score, solution, algorithm, iterations, key, depth, ratio, remove_routes, formula, definition)

    return solution_algorithm

def start_algorithm(map, max_routes, max_time, min_score, algorithm, iterations, key, depth, ratio):
    """Find best routes based on input algorithm"""

    # Run random algorithm and find best solution
    if algorithm == "random":
        best_score = 0
        for i in range(iterations):
            solution = randomize(map, max_routes, max_time)
            if solution.score > best_score:
                best_solution = solution
                best_score = solution.score

    # Run greedy algorithm and find best solution
    if algorithm == "greedy":
        best_score = 0
        for i in range(iterations):
            solution = greedy(map, max_routes, max_time, key)
            if solution.score > best_score:
                best_solution = solution
                best_score = solution.score

    # Run depth first algorithm and find best solution
    if algorithm == "depth_first":
        best_score = 0
        for i in range(iterations):
            solution = depth_first(map, max_routes, max_time, min_score, depth, ratio)
            if solution.score > best_score:
                best_solution = solution
                best_score = solution.score

    # Run breadth first algorithm and find best solution
    if algorithm == "breadth_first":
        best_score = 0
        for i in range(iterations):
            solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio)
            if solution.score > best_score:
                best_solution = solution
                best_score = solution.score

    print(f"Score: ", best_solution.score)

    visualisation(map, best_solution.routes)

    return best_solution


def improve_algorithm(map, max_routes, max_time, min_score, solution, algorithm, iterations, key, depth, ratio, remove_routes, formula, definition):
    """Improve solution based on algorithm"""

    # Run short route swap algorithm and find best solution
    if algorithm == "short_route_swap":
        best_score = 0
        for i in range(iterations):
            solution = short_route_swap(map, max_time, min_score, solution)
            if solution.score > best_score:
                best_solution = solution
                best_score = solution.score

    # Run hillclimber algorithm and find best solution
    elif algorithm[0] == "hillclimber":
        best_score = 0
        for i in range(iterations):
            solution = hillclimber(map, max_routes, max_time, min_score, solution, algorithm[1], iterations, depth, ratio, remove_routes)
            if solution.score > best_score:
                best_solution = solution
                best_score = solution.score

    # Run simulated annealing algorithm and find best solution
    elif algorithm[0] == "simulated_annealing":
        best_score = 0
        for i in range(iterations):
            solution = simulated_annealing(map, max_routes, max_time, min_score, solution, algorithm[1], iterations, depth, ratio, remove_routes, formula)
            if solution.score > best_score:
                best_solution = solution
                best_score = solution.score

    print(f"Improved score: ", best_solution.score)

    visualisation(map, best_solution.routes)

    return best_solution
