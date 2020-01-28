"""
def main(map, max_routes, max_time, iterations, key=None, min_score=None, depth=None, ratio=None):

if __name__ == "__main__":
    main("Nationaal", 20, 180, 1, "Connections", 100, 3, 1.5)

"""
from depth_first import depth_first
from breadth_first import breadth_first
from functions.calculations import all_connections
from greedy import greedy
from hillclimber import hillclimber
from randomize import randomize
from short_route_swap import short_route_swap
from simulated_annealing import simulated_annealing
from statistics import mean

import numpy as np
import matplotlib.pyplot as plt


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


def boxplot(map, max_routes, max_time, iterations, algorithm, key=None, min_score=None, depth=None, ratio=None):
    # Random test data
    np.random.seed(19680801)
    all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
    labels = ['x1', 'x2', 'x3']

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

    # rectangular box plot
    bplot1 = axes[0].boxplot(all_data,
                             vert=True,  # vertical box alignment
                             patch_artist=True,  # fill with color
                             labels=labels)  # will be used to label x-ticks
    axes[0].set_title('Rectangular box plot')

    # notch shape box plot
    bplot2 = axes[1].boxplot(all_data,
                             notch=True,  # notch shape
                             vert=True,  # vertical box alignment
                             patch_artist=True,  # fill with color
                             labels=labels)  # will be used to label x-ticks
    axes[1].set_title('Notched box plot')

    # fill with colors
    colors = ['pink', 'lightblue', 'lightgreen']
    for bplot in (bplot1, bplot2):
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

    # adding horizontal grid lines
    for ax in axes:
        ax.yaxis.grid(True)
        ax.set_xlabel('Three separate samples')
        ax.set_ylabel('Observed values')

    plt.show()

def lineplot_iterations(map, max_routes, max_time, iterations, algorithm, key=None, min_score=None, depth=None, ratio=None):

    score = []
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
    plt.plot(score)
    plt.xlabel("Number of Iterations")
    plt.ylabel(f"K Score")
    if key is None:
        plt.title(f"{algorithm}")
    if key is not None:
        plt.title(f"{algorithm} {key}")
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
    plt.bar(r1, BASIC, color='red', width=barWidth, edgecolor='white', label='Basic')
    plt.bar(r2, SRS, color='green', width=barWidth, edgecolor='white', label='Short Route Swap')
    plt.bar(r3, HC, color='blue', width=barWidth, edgecolor='white', label='Hill Climber')
    plt.bar(r4, SA, color='green', width=barWidth, edgecolor='white', label='Simulated Annealing')

    # Add xticks on the middle of the group bars
    plt.xlabel('Algorithms', fontweight='bold')
    plt.xticks([r + barWidth * 1.5 for r in r1], ['Random', 'Greedy (connections)', 'Depth First', 'Breadth First'])
    # Create legend & Show graphic
    plt.legend()
    plt.show()

# if __name__ == "__main__":
#     histogram_multiple("Nationaal", 20, 180, 1, "connections", 100, 3, 1.5)
