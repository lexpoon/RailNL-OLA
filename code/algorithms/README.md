# Algorithms
Each file in this folder contains an algorithm that finds a solution in the form of a set of routes. This guide will explain each algorithm.

## Randomize
The randomize algorithm starts by picking a random station and then connects with a new randomly chosen station. It stops when the time constraint is met or when a station has no connections left. It then starts with a new route. A connection is only allowed to be used once.

## Greedy
The greedy algorithm starts with the station with the least amount of connections. It then chooses the station to connect with based on either the least amount of connections, the lowest amount of minutes or the highest K score. The user can choose which method the algorithm uses.

## Breadth-first
The breadth first algorithm creates a tree of solutions. It starts by picking the station with the fewest connections. Then, for each possible connection of that station, a new route is created, adding each connection to the currently existing route. The adding of a new connection to all existing routes happens simultaneously. Therefore, every route will have the same length. This is done until the time constraint of a route is met. If the score of a route remains behind compared to the best score, no more stations will be added to this route.

## Depth-first
The depth first algorithm creates a tree of solutions. It starts by picking the station with the fewest connections. Then, it selects a possible connection of that station and searches its further connections as far as possible, without going back to previous steps. This is done until the time constraint is met for this particular route. Next, the last station is removed from the route and from this station, all other possibilities are searched. This goes on until all possible routes are detected.

## Short Route Swap
The short route swap algorithm finds the routes with the lowest K score, which mostly are routes existing of just 1 connection. It deletes them from the solution and tries to add the deleted connections again to another existing routes.

## Hillclimber
The hillclimber algorithm starts with deleting a random route from a solution. It then deletes an x amount of routes that are connected to the first deleted route. After that, the algorithm creates new routes for the now unused connections, trying to improve the K score. If it improves the solution, this will be the best solution and continues improving with this solution. The new routes can be created with either the random, greedy, breadth-first or depth-first algorithm. The user can choose how many routes will be deleted.

## Simulated Annealing
The simulated annealing algorithm is works the same as hillclimber. The only difference with this algorithm, is the probability of acceptance. Here, a lower score is also accepted with a certain probability. This chance decreases as more iterations are performed.
