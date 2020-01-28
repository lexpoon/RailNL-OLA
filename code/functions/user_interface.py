from functions.calculations import all_connections, connections_station, update_connections
from functions.run_algorithm import improve_algorithm, run_algorithm, start_algorithm

def user_interface():
    """Interaction with user to run, improve and visualize all algorithms"""

    # Welcome user and start first algorithm
    welcome()
    map_info = get_map_info()
    algorithm_info = get_create_algorithm()

    # Set variables to user input
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

    # Ask user for iterations
    while type(iterations) != int:
        iterations = get_int("Hoevaak wil je een nieuwe oplossing genereren?\n")

    # Create solution with input algorithm
    solution = run_algorithm(
            map, max_routes, max_time, solution, algorithm, iterations, key, depth,
            ratio, remove_routes, formula, definition)

    # Update best score
    best_solution = {"solution": '', "score": 0}
    best_solution = check_score(best_solution, solution)


    while True:
        next = next_step()

        if next == "stop":
            break

        # Set variables to user input
        algorithm = next[0]
        iterations = ''
        key = next[1]
        depth = next[2]
        ratio = next[3]
        remove_routes = None
        formula = next[4]
        definition = next[5]

        # Ask for amount of routes
        if next[5] == "improve" and algorithm != "short_route_swap":
            while remove_routes == None:
                while type(remove_routes) != int:
                    remove_routes = get_int("Hoeveel nieuwe routes per keer wil je genereren?\n")
                if remove_routes >= max_routes:
                    remove_routes = None


        # Ask for amount of solutions
        while type(iterations) != int:
            iterations = get_int("Hoevaak wil je een oplossing genereren?\n")

        # Create solution
        solution = run_algorithm(
            map, max_routes, max_time, solution, algorithm, iterations, key, depth,
            ratio, remove_routes, formula, definition)

        # Update best solution
        best_solution = check_score(best_solution, solution)


def welcome():
    """Welcome user"""

    print("Welkom bij RailNL!")
    print("We gaan proberen een zo goed mogelijke intercity dienstregeling vinden.")


def get_map_info():
    """Ask user for map preferences"""

    map = ''
    options = ['holland', 'h', 'nationaal', 'n']

    while map not in options:
        map = input("Voor welke map wil je een oplossing generen? Holland (h/H) of Nationaal (n/N)? \n").lower()

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
    options = ['random', 'r', 'greedy', 'g', 'depth_first', 'd', 'breadth_first', 'b']

    # Ask user for algorithm
    while algorithm not in options:
        algorithm = input(
            "Met welk algoritme wil je een oplossing generen? Random (R/r), Greedy (G/g), Depth First (D/p) of Breadth First (B/b)?\n"
        ).lower()

    # Set input variables for random algorithm
    if algorithm == "random" or algorithm == "r":
        algorithm = "random"
        key = depth = ratio = None

    # Set input variables for greedy algorithm
    elif algorithm == "greedy" or algorithm == "g":
        algorithm = "greedy"
        key = ''
        depth = ratio = None
        options = ['connecties', 'c', 'tijd', 't', 'score', 's']

        # Ask user for greedy type
        while key not in options:
            key = input(
                "Op basis waarvan wil je het Greedy algoritme runnen? Connecties (C/c), Tijd (T/t) of Score (S/s)?\n"
            ).lower()

        if key == "connecties" or key == "c":
            key = "connections"

        elif key == "tijd" or key == "t":
            key = "time"

        else:
            key = "score"

    # Set input variables for depth first algorithm
    elif algorithm == "depth first" or algorithm == "d":
        algorithm = "depth_first"
        key = None
        depth = ratio = ''

        while type(depth) != int:
            depth = get_int("Na hoeveel stations wil je beginnen met prunen?\n")

        while type(ratio) != float:
            ratio = get_float(
                "Bij welke ratio (score/lengte route) achterstand op de beste score wil je stoppen met zoeken?\n"
            )

    # Set input variables for breadth first algorithm
    elif algorithm == "breadth first" or algorithm == "b":
        algorithm = "breadth_first"
        key = None
        depth = ratio = ''

        while type(depth) != int:
            depth = get_int("Na hoeveel stations wil je beginnen met prunen?\n")

        while type(ratio) != float:
            ratio = get_float(
                "Bij welke ratio (score/lengte route) achterstand op de beste score wil je stoppen met zoeken?\n"
            )

    return [algorithm, key, depth, ratio]


def get_improve_algorithm():
    """Ask user for preferences for improvement algorithm"""

    algorithm = ''
    formula = None
    options = ['hillclimber', 'h', 'short route swap', 's', 'simulated annealing', 'a']

    # Ask user for improvement algorithm
    while algorithm not in options:
        algorithm = input(
            "Met welk algoritme wil je een oplossing generen? Short Route Swap (S/s), Hillclimber (H/h), Simulated Annealing (A/a)?\n"
        ).lower()

    options = ['hillclimber', 'h', 'simulated annealing', 'a']

    # Ask user which algorithm to use with hillclimber or simulated annealing
    if algorithm in options:
        route_info = get_create_algorithm()

        if algorithm == "hillclimber" or algorithm == "h":
            algorithm = "hillclimber"

        else:
            algorithm = "simulated_annealing"

            options = ['linear', 'l', 'exponential', 'e']
            while formula not in options:
                formula = input(
                    "Met welke functie wil je de temperatuur generen? Linear (L/l) of Exponentieel (E/e)\n"
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
    options = ['v', 'n', 'q']

    while next_step not in options:
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
