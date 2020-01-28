import matplotlib.pyplot as plt
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
    # boxplot(map, max_routes, max_time, iterations, algorithm, key, min_score, depth, ratio)
    # iterations(map, max_routes, max_time, iterations, algorithm, key, min_score, depth, ratio)
    hillclimber_and_simulated(map, max_routes, max_time, iterations, algorithm, key, min_score, depth, ratio)

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

def iterations(map, max_routes, max_time, iterations, algorithm, key=None, min_score=None, depth=None, ratio=None):
    """Visualize a lineplot of algorithm scores of selected algorithm"""

    score = []

    # Create dataset based on scores of selected algorithm
    for i in range(iterations):
        if algorithm == "random":
            solution = randomize(map, max_routes, max_time)
        elif algorithm == "greedy":
            solution = greedy(map, max_routes, max_time, key)
        elif algorithm == "depth_first":
            solution = depth_first(map, max_routes, max_time, min_score, depth, ratio)
        elif algorithm == "breadth_first":
            solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio)
        score.append(solution.score)

    lineplot(score, algorithm, key=None)


def hillclimber_and_simulated(map, max_routes, max_time, iterations, algorithm, key=None, min_score=None, depth=None, ratio=None):

    best_score = 0
    for i in range(iterations):
        if algorithm == "random":
            solution = randomize(map, max_routes, max_time)
        elif algorithm == "greedy":
            solution = greedy(map, max_routes, max_time, key)
        elif algorithm == "depth_first":
            solution = depth_first(map, max_routes, max_time, min_score, depth, ratio)
        elif algorithm == "breadth_first":
            solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio)
        if solution.score > best_score:
            best_score = solution.score
            best_solution = solution

    best_score_hc = best_solution.score
    best_score_sa_linear = best_solution.score
    best_score_sa_exponential = best_solution.score
    score_hc = [best_solution.score]
    score_sa_linear = [best_solution.score]
    score_sa_exponential = [best_solution.score]

    for i in range(iterations):
        hc_solution = hillclimber(map, max_routes, max_time, min_score, best_solution, algorithm, depth, ratio, 3)
        sa_solution_linear = simulated_annealing(map, max_routes, max_time, min_score, best_solution, algorithm, depth, ratio, 3, i, iterations, "linear")
        sa_solution_exponential = simulated_annealing(map, max_routes, max_time, min_score, best_solution, algorithm, depth, ratio, 3, i, iterations, "exponential")

        if hc_solution.score > best_score_hc:
            best_score_hc = hc_solution.score
            score_hc.append(hc_solution.score)
        else:
            score_hc.append(score_hc[-1])

        if sa_solution_linear.score > best_score_sa_linear:
            best_score_sa = sa_solution_linear.score
            score_sa_linear.append(sa_solution_linear.score)
        else:
            score_sa_linear.append(score_hc[-1])

        if sa_solution_exponential.score > best_score_sa_exponential:
            best_score_sa = sa_solution_exponential.score
            score_sa_exponential.append(sa_solution_exponential.score)
        else:
            score_sa_exponential.append(score_hc[-1])

    lineplot(score_hc, algorithm, key, "Hill Climber")
    lineplot(score_sa_linear, algorithm, "Simulated Annealing (Linear)")
    lineplot(score_sa_exponential, algorithm, "Simulated Annealing (Exponential)")

def lineplot(score, algorithm, key=None, type=None):
    """Create lineplot of selected algorithm"""

    plt.plot(score)
    plt.xlabel("Number of Iterations")
    plt.ylabel(f"K Score")

    # Create correct title
    name = algorithm.split("_")
    name = [x.capitalize() for x in name]
    name = ' '.join(name)

    if key is None:
        plt.title(name)
    if key is not None:
        plt.title(f"{name} {key.capitalize()}")
    if type is not None:
        plt.title(f"{name} {type.capitalize()}")
    # plt.show()
    plt.savefig(f"{name}_{key}_100")


if __name__ == "__main__":
    """boxplot"""
    # main("Nationaal", 20, 180, 100, None, None, 100, 3, 1.2)

    """iterations or Hillclimber and Simulated Annealing"""
    main("Nationaal", 20, 180, 10, "random")
    # main("Nationaal", 20, 180, 100, "greedy", "connections")
    # main("Nationaal", 20, 180, 100, "greedy", "time")
    # main("Nationaal", 20, 180, 100, "greedy", "score")
    # main("Nationaal", 20, 180, 100, "depth_first", None, 100, 3, 1.2)
    # main("Nationaal", 20, 180, 100, "breadth_first", None, 100, 3, 1.2)
