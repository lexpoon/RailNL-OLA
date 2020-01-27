from functions.run_algorithm import run_algorithm, start_algorithm, improve_algorithm
from functions.calculations import all_connections, connections_station, update_connections

def user_interface():
    """Start user interface"""

    welcome()
    map_info = get_map_info()
    algorithm_info = get_create_algorithm()

    map = map_info[0]
    max_routes = map_info[1]
    max_time = map_info[2]
    solution = None
    algorithm = algorithm_info[0]
    iterations = ''
    key = algorithm_info[1]
    depth = algorithm_info[2]
    ratio = algorithm_info[3]
    remove_routes = None
    formula = None
    definition = "create"

    while isinstance(iterations, int) == False:
        iterations = get_int("Hoevaak wil je een nieuwe oplossing genereren?\n")

    solution = run_algorithm(
            map, max_routes, max_time, solution, algorithm, iterations, key, depth, 
            ratio, remove_routes, formula, definition)

    best_solution = {"solution": '', "score": 0}
    best_solution = check_score(best_solution, solution)

    while True:
        next = next_step()
        solution = solution
        algorithm = next[0]
        iterations = ''
        key = next[1]
        depth = next[2]
        ratio = next[3]
        remove_routes = None
        formula = next[4]
        definition = next[5]

        if next == "stop":
            break

        elif next[5] == "improve" and algorithm!="short_route_swap":
            while isinstance(remove_routes, int) == False and remove_routes==None:
                remove_routes = get_int("Hoeveel nieuwe routes per keer wil je genereren?\n")
                if remove_routes >= max_routes:
                    remove_routes = None

        while isinstance(iterations, int) != True and algorithm!="short_route_swap":
            iterations = get_int("Hoevaak wil je een oplossing genereren?\n")

        solution = run_algorithm(
            map, max_routes, max_time, solution, algorithm, iterations, key, depth, 
            ratio, remove_routes, formula, definition)

        best_solution = check_score(best_solution, solution)


def welcome():
    """Welcome user"""

    print("Welkom bij RailNL!")
    print("We gaan proberen een zo goed mogelijke intercity dienstregeling vinden.")


def get_map_info():
    """Ask user for map preferences"""

    map = ''

    while map != "holland" and map != "h" and map != "nationaal" and map != "n":
        map = input(
            "Voor welke map wil je een oplossing generen? Holland (h/H) of Nationaal (n/N)? \n"
        ).lower()

    if map == "holland" or map == "h":
        map = "Holland"
        max_routes = 7
        max_time = 120

    else:
        map = "Nationaal"
        max_routes = 20
        max_time = 180

    return [map, max_routes, max_time]


def get_create_algorithm():
    """Ask user for algorithm preferences"""

    algorithm = ''

    while algorithm != "random" and algorithm != "r" and algorithm != "greedy" and algorithm != "g" and algorithm != "depth_first" and algorithm != "d" and algorithm != "breadth_first" and algorithm != "b":
        algorithm = input(
            "Met welk algoritme wil je een oplossing generen? Random (R/r), Greedy (G/g), Depth First (D/p) of Bread First (B/b)?\n"
        ).lower()

        if algorithm == "random" or algorithm == "r":
            algorithm = "random"
            key = depth = ratio = None

        elif algorithm == "greedy" or algorithm == "g":
            algorithm = "greedy"
            key = ''
            depth = ratio = None

            while key != "connecties" and key != "c" and key != "tijd" and key != "t" and key != "score" and key != "s":
                key = input(
                    "Op basis waarvan wil je het Greedy algoritme runnen? Connecties (C/c), Tijd (T/t) of Score (S/s)?\n"
                ).lower()

            if key == "connecties" or key == "c":
                key = "connections"

            elif key == "tijd" or key == "t":
                key = "time"

            else:
                key = "quality"

        elif algorithm == "depth first" or algorithm == "d":
            algorithm = "depth_first"
            key = None
            depth = ratio = ''

            while isinstance(depth, int) != True:
                depth = get_int("Na hoeveel stations wil je beginnen met prunen?\n")

            while isinstance(ratio, float) != True:
                ratio = get_float(
                    "Bij welke ratio (score/lengte route) achterstand op de beste score wil je stoppen met zoeken?\n"
                )

        elif algorithm == "breadth first" or algorithm == "b":
            algorithm = "breadth_first"
            key = None
            depth = ratio = ''

            while isinstance(depth, int) != True:
                depth = get_int("Na hoeveel stations wil je beginnen met prunen?\n")

            while isinstance(ratio, float) != True:
                ratio = get_float(
                    "Bij welke ratio (score/lengte route) achterstand op de beste score wil je stoppen met zoeken?\n"
                )

    return [algorithm, key, depth, ratio]


def get_improve_algorithm():
    """Ask user for preferences for improvement algorithm"""

    algorithm = ''
    formula = None

    while algorithm != "hillclimber" and algorithm != "h" and algorithm != "short route swap" and algorithm != "s" and algorithm != "simulated annealing" and algorithm != "a":
        algorithm = input(
            "Met welk algoritme wil je een oplossing generen? Short Route Swap (S/s), Hillclimber (H/h), Simulated Annealing (A/a)?\n"
        ).lower()

    if algorithm == "hillclimber" or algorithm == "h" or algorithm == "simulated annealing" or algorithm == "a":
        route_info = get_create_algorithm()

        if algorithm == "hillclimber" or algorithm == "h":
            algorithm = "hillclimber"

        else:
            algorithm = "simulated_annealing"

            while formula != "linear" and formula != "l" and formula != "exponential" and formula != "e":
                formula = input(
                    "Met welk temperatuur wil je de temperatuur generen? Linear (L/l) of Exponentieel (E/e)\n"
                ).lower()

                if formula == "linear" or formula == "l":
                    formula = "linear"

                else:
                    formula = "exponential"

        route_info[0] = [algorithm, route_info[0]]

    else:
        route_info = ["short_route_swap", None, None, None]

    return [route_info[0], route_info[1], route_info[2], route_info[3], formula]


def check_score(best_solution, solution):
    """Update best score history"""

    if solution.score > best_solution["score"]:
        best_solution = {"solution": solution.routes, "score": solution.score}

    return best_solution


def next_step():
    """Ask user for next step"""

    next_step = ''

    while next_step != "v" and next_step != "n" and next_step != "q":
        next_step = input(
            "Gebruik verbeter algoritme (V/v), Nieuwe oplossing genereren (N/n), of Stoppen (Q/q)\n"
            ).lower()

    if next_step == 'v':
        info = get_improve_algorithm()
        definition = "improve"

    elif next_step == 'n':
        info = get_create_algorithm()
        info.append(None)
        definition = "create"

    else:
        return "stop"

    return [info[0], info[1], info[2], info[3], info[4], definition]


def get_int(text):
    """Check if input is integer"""

    iterations = input(text)

    try:
        iterations = int(iterations)
    except:
        iterations = iterations

    return iterations


def get_float(text):
    """Check if input is float"""

    iterations = input(text)

    try:
        iterations = float(iterations)
    except:
        iterations = iterations

    return iterations
