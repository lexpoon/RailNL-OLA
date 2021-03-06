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


def main(map, max_routes, max_time, iterations, algorithm=None, key=None, min_score=None, depth=None, ratio=None):
    """Select the type of visualisation by de-comment a function."""

    # boxplot(map, max_routes, max_time, iterations, algorithm, key, min_score, depth, ratio)
    # iterations(map, max_routes, max_time, iterations, algorithm, key, min_score, depth, ratio)
    # hillclimber_and_simulated(map, max_routes, max_time, iterations, algorithm, key, min_score, depth, ratio)
    srs(map, max_routes, max_time, iterations, algorithm, key, min_score, depth, ratio)


def boxplot(map, max_routes, max_time, iterations, algorithm=None, key=None, min_score=None, depth=None, ratio=None):
    """Visualize a boxplot for all algorithms."""

    random = []
    greedy_connections = []
    greedy_time = []
    greedy_score = []
    depth_first_score = []
    breadth_first_score = []

    # Create dataset based on algorithm scores
    for i in range(iterations):
        random.append(randomize(map, max_routes, max_time).score)
        greedy_connections.append(greedy(map, max_routes, max_time, "connections").score)
        greedy_time.append(greedy(map, max_routes, max_time, "time").score)
        greedy_score.append(greedy(map, max_routes, max_time, "score").score)
        depth_first_score.append(depth_first(map, max_routes, max_time, min_score, depth, ratio).score)
        breadth_first_score.append(breadth_first(map, max_routes, max_time, min_score, depth, ratio).score)

    # Create boxplot based on all scores
    colors = ["steelblue", "tomato", "coral", "lightsalmon", "lightgreen", "lightblue"]
    medianprops = dict(linestyle="solid", linewidth=1, color="black")
    box_plot_data = [random, greedy_connections, greedy_time, greedy_score, depth_first_score, breadth_first_score]
    box = plt.boxplot(box_plot_data, patch_artist=True, medianprops=medianprops, showfliers=False, labels=["random","greedy (connections)","greedy (time)","greedy (score)", "depth first", "breadth first"],
                )

    for patch, color in zip(box["boxes"], colors):
        patch.set_facecolor(color)

    plt.ylabel(f"K Score")
    plt.title("Boxplot Algorithms")
    plt.show()


def iterations(map, max_routes, max_time, iterations, algorithm, key=None, min_score=None, depth=None, ratio=None):
    """Visualize a lineplot of algorithm scores of selected algorithm."""

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

    # Show visualisation
    lineplot(score, algorithm, key=None)


def hillclimber_and_simulated(map, max_routes, max_time, iterations, algorithm, key=None, min_score=None, depth=None, ratio=None):
    """"Visualize the iterative algorithms based on a basic/constructive algorithm."""

    # Get the algorithm solution to apply a iterative algorithm on
    best_score = 0
    for i in range(iterations):
        if algorithm == "random":
            solution = randomize(map, max_routes, max_time)
        elif algorithm == "greedy":
            solution = greedy(map, max_routes, max_time, key)
        elif algorithm == "depth_first":
            solution = depth_first(map, max_routes, max_time, min_score, depth, ratio, "improve")
        elif algorithm == "breadth_first":
            solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio, "improve")
        if solution.score > best_score:
            best_score = solution.score
            best_solution = solution

    # Set variables for running the iterative algorithms
    best_score_hc = best_solution.score
    best_score_sa_linear = best_solution.score
    best_score_sa_exponential = best_solution.score
    score_hc = [best_solution.score]
    score_sa_linear = [best_solution.score]
    score_sa_exponential = [best_solution.score]

    # Apply the hillclimber and simulated annealing on the solution
    for i in range(iterations):
        hc_solution = hillclimber(map, max_routes, max_time, min_score, best_solution, "depth_first", depth, ratio, 3)
        sa_solution_linear = simulated_annealing(map, max_routes, max_time, min_score, best_solution, "depth_first", depth, ratio, 3, i, iterations, "linear")
        sa_solution_exponential = simulated_annealing(map, max_routes, max_time, min_score, best_solution, "depth_first", depth, ratio, 3, i, iterations, "exponential")

        if hc_solution.score > best_score_hc:
            best_score_hc = hc_solution.score
            score_hc.append(hc_solution.score)
        else:
            score_hc.append(score_hc[-1])

        if sa_solution_linear.score > best_score_sa_linear:
            best_score_sa_linear = sa_solution_linear.score
            score_sa_linear.append(sa_solution_linear.score)
        else:
            score_sa_linear.append(score_sa_linear[-1])

        if sa_solution_exponential.score > best_score_sa_exponential:
            best_score_sa_exponential = sa_solution_exponential.score
            score_sa_exponential.append(sa_solution_exponential.score)
        else:
            score_sa_exponential.append(score_sa_exponential[-1])

    # Show the iterative algorithm solutions
    lineplot(score_hc, algorithm, key, "Hill Climber")
    lineplot(score_sa_linear, algorithm, "Simulated Annealing (Linear)")
    lineplot(score_sa_exponential, algorithm, "Simulated Annealing (Exponential)")


def srs(map, max_routes, max_time, iterations, algorithm=None, key=None, min_score=None, depth=None, ratio=None):
    best_score = 0
    no_improvement = 0
    improvement = 0
    difference = []
    for i in range(iterations):
        if algorithm == "random":
            solution = randomize(map, max_routes, max_time)
        elif algorithm == "greedy":
            solution = greedy(map, max_routes, max_time, key)
        elif algorithm == "depth_first":
            solution = depth_first(map, max_routes, max_time, min_score, depth, ratio, "improve")
        elif algorithm == "breadth_first":
            solution = breadth_first(map, max_routes, max_time, min_score, depth, ratio, "improve")

        srs = short_route_swap(map, max_time, min_score, solution)

        if solution.score < srs.score:
            improvement += 1
            difference.append(srs.score - solution.score)
        else:
            no_improvement += 1

    # Create pie chart
    labels = "No improvement", "Improvement"
    sizes = [no_improvement, improvement]
    explode = (0, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")

    plt.title(f"Percentage of 1000 x SRS improvements of {algorithm} ({key})")
    plt.savefig(f"SRS_{algorithm}_{key}_{iterations}_pie_chart")
    plt.clf()

    # Create boxplot based on all scores
    colors = ["steelblue"]
    medianprops = dict(linestyle="solid", linewidth=1, color="black")
    box_plot_data = [difference]
    box = plt.boxplot(box_plot_data, patch_artist=True, medianprops=medianprops, showfliers=False, labels=["SRS difference"])

    for patch, color in zip(box["boxes"], colors):
        patch.set_facecolor(color)

    plt.ylabel(f"Score difference")
    plt.title("Boxplot difference after 1000 x SRS")
    plt.savefig(f"SRS_difference_{algorithm}_{key}_{iterations}_boxplot")
    plt.clf()


def lineplot(score, algorithm, key=None, type=None):
    """Create lineplot of selected algorithm."""

    plt.plot(score)
    plt.xlabel("Number of Iterations")
    plt.ylabel(f"K Score")

    # Create correct title
    name = algorithm.split("_")
    name = [x.capitalize() for x in name]
    name = " ".join(name)

    if key is None:
        plt.title(name)
    if key is not None:
        plt.title(f"{name} {key.capitalize()}")
    if type is not None:
        plt.title(f"{name} {type.capitalize()}")
    # plt.show()
    plt.savefig(f"{name}_{key}_100")
    plt.clf()

if __name__ == "__main__":
    min_score = 10000/89-105

    """boxplot"""
    # main("Nationaal", 20, 180, 100, None, None, min_score, 3, 1.2)

    """iterations or Hillclimber and Simulated Annealing"""
    # main("Nationaal", 20, 180, 2, "random", None, min_score, 3, 1.5)
    main("Nationaal", 20, 180, 1000, "greedy", "connections", min_score, 3, 1.5)
    # main("Nationaal", 20, 180, 100, "greedy", "time", min_score, 3, 1.5)
    # main("Nationaal", 20, 180, 100, "greedy", "score", min_score, 3, 1.5)
    # main("Nationaal", 20, 180, 2, "depth_first", "connections", min_score, 3, 1.5)
    # main("Nationaal", 20, 180, 1000, "breadth_first", None, min_score, 3, 1.5)
