"""
def main(map, max_routes, max_time, iterations, key=None, min_score=None, depth=None, ratio=None):

if __name__ == "__main__":
    main("Nationaal", 20, 180, 1, "Connections", 100, 3, 1.5)

"""

import numpy as np
import matplotlib.pyplot as plt

def histogram(randomize, depth_first, breadth_first):
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

def lineplot(x):
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
