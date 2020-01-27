"""
def main(map, max_routes, max_time, iterations, key=None, min_score=None, depth=None, ratio=None):

if __name__ == "__main__":
    main("Nationaal", 20, 180, 1, "Connections", 100, 3, 1.5)

"""

import numpy as np
import matplotlib.pyplot as plt


def histogram_bar(randomize, depth_first, breadth_first):
    # Make a fake dataset:
    height = [randomize, depth_first, breadth_first]
    bars = ("Randomize", "Depth first", "Breadth first")
    y_pos = np.arange(len(bars))

    # Create bars
    plt.bar(y_pos, height)

    # Create names on the x-axis
    plt.xticks(y_pos, bars)

    # Show graphic
    plt.show()

    """
    best_score_random = 0
    for i in range(iterations):
        randomize_solution = randomize(map, max_routes, max_time)
        if randomize_solution.score > best_score_random:
            best_score_random = randomize_solution.score
            best_solution_random = randomize_solution

    best_score_greedy = 0
    for i in range(iterations):
        greedy_solution = greedy(map, max_routes, max_time, key)
        if greedy_solution.score > best_score_greedy:
            best_score_greedy = greedy_solution.score
            best_solution_greedy = greedy_solution

    best_score_depth_first = 0
    for i in range(iterations):
        depth_first_solution = depth_first(map, max_routes, max_time, min_score, depth, ratio)
        if depth_first_solution.score > best_score_depth_first:
            best_score_depth_first = depth_first_solution.score
            best_solution_depth_first = depth_first_solution

    best_score_breadth_first = 0
    for i in range(iterations):
        breadth_first_solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio)
        if breadth_first_solution.score > best_score_breadth_first:
            best_score_breadth_first = breadth_first_solution.score
            best_solution_breadth_first = breadth_first_solution

    histogram(best_solution_random.score, best_solution_depth_first.score, best_solution_breadth_first.score)

    """


def iteration_lineplot(x):
    plt.plot(x)
    plt.ylabel('score')
    plt.show()

    """
    randomize_score = [0]
    for i in range(iterations):
        randomize_solution = randomize(map, max_routes, max_time)
        if randomize_solution.score > randomize_score[-1]:
            randomize_score.append(randomize_solution.score)
        else:
            randomize_score.append(randomize_score[-1])

    depth_first_score = [0]
    for i in range(iterations):
        depth_first_solution = depth_first(map, max_routes, max_time, min_score, depth, ratio)
        if depth_first_solution.score > depth_first_score[-1]:
            depth_first_score.append(depth_first_solution.score)
        else:
            depth_first_score.append(depth_first_score[-1])

    breadth_first_score = [0]
    for i in range(iterations):
        breadth_first_solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio)
        if breadth_first_solution.score > breadth_first_score[-1]:
            breadth_first_score.append(breadth_first_solution.score)
        else:
            breadth_first_score.append(breadth_first_score[-1])

    lineplot(depth_first_score)
    """


def histogram_multiple():
    # set width of bar
    barWidth = 0.25

    # set height of bar
    bars1 = [12, 30, 1, 8, 22]
    bars2 = [28, 6, 16, 5, 10]
    bars3 = [29, 3, 24, 25, 17]

    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    # Make the plot
    plt.bar(r1, bars1, color='grey', width=barWidth, edgecolor='white', label='var1')
    plt.bar(r2, bars2, color='blue', width=barWidth, edgecolor='white', label='var2')
    plt.bar(r3, bars3, color='green', width=barWidth, edgecolor='white', label='var3')

    # Add xticks on the middle of the group bars
    plt.xlabel('group', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])

    # Create legend & Show graphic
    plt.legend()
    plt.show()
