def get_map_info():
    map = ''
    while map != "holland" and map != "h" and map != "nationaal" and map != "n":
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
    algorithm = ''
    while algorithm != "random" and algorithm != "r" and algorithm != "greedy" and algorithm != "g" and algorithm != "depth first" and algorithm != "d" and algorithm != "breadth first" and algorithm != "b":
        algorithm = input("Met welk algoritme wil je een oplossing generen? Random (R/r), Greedy (G/g), Depth First (D/p) of Bread First (B/b)?\n").lower()

        if algorithm == "random" or algorithm == "r":
            algorithm = "random"
            key = None
            depth = None
            ratio = None

        elif algorithm == "greedy" or algorithm == "g":
            algorithm = "greedy"
            key = ''
            depth = None
            ratio = None

            while key != "connecties" and key != "c" and key != "tijd" and key != "t" and key != "score" and key != "s":
                key = input("Op basis waarvan wil je het Greedy algoritme runnen? Connecties (C/c), Tijd (T/t) of Score (S/s)?\n").lower()
                if key == "tijd" or key == "t":
                    key = "time"
                elif key == "score" or key == "s":
                    key = "connections"

        elif algorithm == "depth first" or algorithm == "d":
            algorithm = "depth_first"
            key = None
            depth = get_int("Na hoeveel stations wil je beginnen met prunen?")
            ratio = get_float("Bij welke ratio (score/lengte route) achterstand op de beste score wil je stoppen met zoeken?\n")

        elif algorithm == "breadth first" or algorithm == "b":
            algorithm = "breadth_first"
            key = None
            depth = ''
            ratio = ''
            while isinstance(iterations, int) != True:
                depth = get_int("Na hoeveel stations wil je beginnen met prunen?")
            while isinstance(iterations, float) != True:
                ratio = get_float("Bij welke ratio (score/lengte route) achterstand op de beste score wil je stoppen met zoeken?\n")

    return [algorithm, key, depth, ratio]

def get_improve_algorithm():
    algorithm = tuple()
    while algorithm != "hillclimber" and algorithm != "h" and algorithm != "less is more" and algorithm != "l" and algorithm != "simulated annealing" and algorithm != "s":
        algorithm[0] = input("Met welk algoritme wil je een oplossing generen? Less is More (L/l), Hillclimbee (H/h), Simulated Annealing (S/s)?\n").lower()

    if algorithm == "hillclimber" or algorithm == "h" or algorithm == "simulated annealing" or algorithm == "s":
        route_info = get_create_algorithm()
    else:
        route_info = ["less_is_more", None, None, None]

    return [route_info[0], route_info[1], route_info[2], route_info[3]]

def next_step():
    while next_step != "v" and next_step != "n" and next_step != "q":
        next_step = input("Opties: Gebruik verbeter algoritme (V/v), Nieuwe oplossing genereren (N/n), Stoppen (Q/q)\n").lower()

    if next_step == 'v':
        info = get_improve_algorithm()
        definition = "improve"

    elif next_step == 'n':
        info = get_create_algorithm()
        definition = "create"

    else:
        return "Stoppen"

    return [info[0], info[1], info[2], info[3], definition]

def get_int(text):
    iterations = input(text)
    try:
        iterations = int(iterations)
    except:
        iterations = iterations

    return iterations

def get_float(text):
    iterations = input(text)
    try:
        iterations = float(iterations)
    except:
        iterations = iterations

    return iterations
