def get_map_info():
    map = ''
    while map != "holland" or map != "h" or map != "nationaal" or map != "n":
        map = lowercase(get_string("Voor welke map wil je een oplossing generen? Holland (h/H) of Nationaal (n/N)?"))

    if map = "holland" or map != "h":
        map = "Holland"
        max_routes = 7
        max_time = 120
    else:
        map = "Nationaal"
        max_routes = 20
        max_time = 180

    return map, max_routes, max_time

def get_create_algorithm():
    algorithm = ''
    while algorithm != "random" or algorithm != "r" or algorithm != "greedy" algorithm != "g" or or algorithm != "depth first" algorithm != "d" or or algorithm != "breadth first" algorithm != "b":
        algorithm = lowercase(get_string("Met welk algoritme wil je een oplossing generen? Random (R/r), Greedy (G/g), Depth First (D/p) of Bread First (B/b)?"))

        if algorithm == "random" or algorithm == "r":
            algorithm = "random"
            key = None
            depth = None
            ratio = None

        elif algorithm == "greedy" or "g":
            algorithm = "greedy"
            key = ''
            depth = None
            ratio = None

            while key != "connecties" or key != "c" or key != "tijd" or key != "t" or key != "score" or key != "s":
                key = lowercase(get_string("Op basis waarvan wil je het Greedy algoritme runnen? Connecties (C/c), Tijd (T/t) of Score (S/s)?"))
                if key == "tijd" or key == "t":
                    key = "time"
                elif key == "score" or key == "s":
                    key = "connections"

        elif algorithm == "depth first" or algorithm == "d":
            algorithm = "depth_first"
            depth = get_int("Na hoeveel stations wil je beginnen met prunen?")
            ratio = get_float("Bij welke ratio (score/lengte route) achterstand op de beste score wil je stoppen met zoeken?")

        elif algorithm == "breadth first" or algorithm == "b":
            algorithm = "breadth_first"
            depth = get_int("Na hoeveel stations wil je beginnen met prunen?")
            ratio = get_float("Bij welke ratio (score/lengte route) achterstand op de beste score wil je stoppen met zoeken?")


def get_improve_algorithm():
    pass
