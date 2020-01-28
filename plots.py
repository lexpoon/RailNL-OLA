import matplotlib.pyplot as plt
import numpy as np
import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "functions"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

from breadth_first import breadth_first
from depth_first import depth_first
from functions.calculations import all_connections
from greedy import greedy
from hillclimber import hillclimber
from randomize import randomize
from short_route_swap import short_route_swap
from simulated_annealing import simulated_annealing
from statistics import mean


def main(map, max_routes, max_time, iterations, algorithm=None, key=None, min_score=None, depth=None, ratio=None):
    lineplot_iterations(map, max_routes, max_time, iterations, algorithm, key, min_score, depth, ratio)
    # boxplot(map, max_routes, max_time, iterations, algorithm, key, min_score, depth, ratio)


def histogram_bar(randomize, greedy, depth_first, breadth_first):

    # Make a mean dataset
    height = [mean(randomize), mean(greedy), mean(depth_first), mean(breadth_first)]
    bars = ("Randomize", "Greedy (connections)", "Depth first", "Breadth first")
    y_pos = np.arange(len(bars))

    # Create bars
    plt.bar(y_pos, height)

    # Create names on the x-axis
    plt.xticks(y_pos, bars)

    # Show graphic
    plt.show()


def boxplot(map, max_routes, max_time, iterations, algorithm=None, key=None, min_score=None, depth=None, ratio=None):
    """Visualize a boxplot for all algorithms"""

    random = []
    greedy_connections = []
    greedy_time = []
    greedy_score = []
    depth_first_score = []
    breadth_first_score = []

    # iterate x num of times to create dataset based on scores
    for i in range(iterations):
        random.append(randomize(map, max_routes, max_time).score)
        greedy_connections.append(greedy(map, max_routes, max_time, "connections").score)
        greedy_time.append(greedy(map, max_routes, max_time, "time").score)
        greedy_score.append(greedy(map, max_routes, max_time, "score").score)
        depth_first_score.append(depth_first(map, max_routes, max_time, min_score, depth, ratio).score)
        breadth_first_score.append(breadth_first(map, max_routes, max_time, min_score, depth, ratio).score)

    print (f"random, mean: {mean(random)}, minimum: {min(random)}, maximum: {max(random)}")
    print (f"greedy_connections, mean: {mean(greedy_connections)}, minimum: {min(greedy_connections)}, maximum: {max(greedy_connections)}")
    print (f"greedy_time, mean: {mean(greedy_time)}, minimum: {min(greedy_time)}, maximum: {max(greedy_time)}")
    print (f"greedy_score, mean: {mean(greedy_score)}, minimum: {min(greedy_score)}, maximum: {max(greedy_score)}")
    print (f"depth_first_score, mean: {mean(depth_first_score)}, minimum: {min(depth_first_score)}, maximum: {max(depth_first_score)}")
    print (f"breadth_first_score, mean: {mean(breadth_first_score)}, minimum: {min(breadth_first_score)}, maximum: {max(breadth_first_score)}")

    # Create boxplot based on all scores
    colors = ["steelblue", "tomato", "coral", "lightsalmon", "lightgreen", "lightblue"]
    medianprops = dict(linestyle='solid', linewidth=1, color='black')
    box_plot_data = [random, greedy_connections, greedy_time, greedy_score, depth_first_score, breadth_first_score]
    box = plt.boxplot(box_plot_data, patch_artist=True, medianprops=medianprops, showfliers=False, labels=["random","greedy (connections)","greedy (time)","greedy (score)", "depth first", "breadth first"],
                )

    for patch, color in zip(box["boxes"], colors):
        patch.set_facecolor(color)

    plt.ylabel(f"K Score")
    plt.title("Boxplot Algorithms")
    plt.show()

def lineplot_iterations(map, max_routes, max_time, iterations, algorithm, key=None, min_score=None, depth=None, ratio=None):
    """Visualize a lineplot of algorithm scores of selected algorithm"""

    score = []

    # Create dataset based on scores of selected algorithm
    for i in range(iterations):
        if algorithm == "random":
            solution = randomize(map, max_routes, max_time)
        elif algorithm == "greedy":
            solution = greedy(map, max_routes, max_time, key)
        elif algorithm == "depth first":
            solution = depth_first(map, max_routes, max_time, min_score, depth, ratio)
        elif algorithm == "breadth first":
            solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio)
        score.append(solution.score)

    # Create lineplot of selected algorithm
    plt.plot(score)
    plt.xlabel("Number of Iterations")
    plt.ylabel(f"K Score")
    if key is None:
        plt.title(algorithm.capitalize())
    if key is not None:
        plt.title(f"{algorithm.capitalize()} {key.capitalize()}")
    plt.show()


def histogram_multiple(random, greedy, depth_first, breadth_first):

    original_solutions = (random, greedy, depth_first, breadth_first)

    map = "Nationaal"
    max_routes = 20
    max_time = 180
    min_score = 10000/len(all_connections(map)) - 105
    algorithm = "depth_first"
    iterations = 20
    depth = 3
    ratio = 1.5
    remove_routes = 4
    formula = "linear"

    # set width of bar
    barWidth = 0.15

    # set height of bar
    BASIC = []
    SRS = []
    HC = []
    SA = [1,2,3,4]

    for solution in original_solutions:
        BASIC.append(solution.score)

    short_route_swap_solution = [short_route_swap(map, max_routes, 100, solution)
                                for solution in original_solutions]

    for solution in short_route_swap_solution:
        SRS.append(solution.score)

    hillclimber_solution = [hillclimber(map, max_routes, max_time, min_score,
                                        solution, algorithm, iterations,
                                        depth, ratio, remove_routes)
                                        for solution in original_solutions]

    for solution in hillclimber_solution:
        HC.append(solution.score)

    simulated_annealing_solution = [simulated_annealing(map, max_routes, max_time,
                                                        min_score, solution, algorithm,
                                                        iterations, depth, ratio,
                                                        remove_routes, formula)
                                                        for solution in original_solutions]

    for solution in simulated_annealing_solution:
        SA.append(solution.score)

    # Set position of bar on X axis
    r1 = np.arange(len(BASIC))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]

    # Make the plot
    plt.bar(r1, BASIC, color="red", width=barWidth, edgecolor="white", label="Basic")
    plt.bar(r2, SRS, color="green", width=barWidth, edgecolor="white", label="Short Route Swap")
    plt.bar(r3, HC, color="blue", width=barWidth, edgecolor="white", label="Hill Climber")
    plt.bar(r4, SA, color="green", width=barWidth, edgecolor="white", label="Simulated Annealing")

    # Add xticks on the middle of the group bars
    plt.xlabel("Algorithms", fontweight="bold")
    plt.xticks([r + barWidth * 1.5 for r in r1], ["Random", "Greedy (connections)", "Depth First", "Breadth First"])
    # Create legend & Show graphic
    plt.legend()
    plt.show()

if __name__ == "__main__":
    """boxplot"""
    # main("Nationaal", 20, 180, 100, None, None, 100, 3, 1.2)

    """iterations"""
    # main("Nationaal", 20, 180, 100, "random")
    # main("Nationaal", 20, 180, 100, "greedy", "connections")
    # main("Nationaal", 20, 180, 100, "greedy", "time")
    # main("Nationaal", 20, 180, 100, "greedy", "score")
    main("Nationaal", 20, 180, 100, "depth first", None, 100, 3, 1.2)
    # main("Nationaal", 20, 180, 100, "breadth first", None, 100, 3, 1.2)
