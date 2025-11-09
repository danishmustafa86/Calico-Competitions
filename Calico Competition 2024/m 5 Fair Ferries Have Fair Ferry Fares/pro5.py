import heapq
from collections import defaultdict, deque

def solve_fair_ferries():
    T = int(input().strip())
    results = []

    for _ in range(T):
        # Parse initial test case input
        n, fare, start, destination = input().strip().split()
        n = int(n)
        fare = float(fare[1:])  # Remove '$' and convert to float

        # Graph representation
        graph = defaultdict(list)
        docks = set()

        for _ in range(n):
            line = input().strip().split()
            if line[0] == "ROAD":
                _, loc1, loc2 = line
                graph[loc1].append((loc2, 0))  # Roads have cost 0
                graph[loc2].append((loc1, 0))
            elif line[0] == "DOCK":
                _, loc = line
                docks.add(loc)

        # Connect all docks with ferry fares
        dock_list = list(docks)
        for i in range(len(dock_list)):
            for j in range(i + 1, len(dock_list)):
                graph[dock_list[i]].append((dock_list[j], fare))
                graph[dock_list[j]].append((dock_list[i], fare))

        # Dijkstra's algorithm to find the shortest path
        def dijkstra(start, destination):
            pq = [(0, start)]  # Priority queue with (cost, location)
            costs = {start: 0}

            while pq:
                current_cost, current_node = heapq.heappop(pq)

                if current_node == destination:
                    return current_cost

                for neighbor, edge_cost in graph[current_node]:
                    new_cost = current_cost + edge_cost
                    if neighbor not in costs or new_cost < costs[neighbor]:
                        costs[neighbor] = new_cost
                        heapq.heappush(pq, (new_cost, neighbor))

            return float('inf')

        # Run Dijkstra's algorithm
        min_cost = dijkstra(start, destination)

        # Output results based on minimum cost
        if min_cost == float('inf'):
            results.append("Just stay home")
        elif min_cost == 0:
            results.append("The trip's free!")
        else:
            results.append(f"Bring ${min_cost:.2f} for the trip.")

        # Consume the blank line between test cases
        if _ < T - 1:
            input()

    # Print all results
    print("\n".join(results))

# Call the function to solve the problem
solve_fair_ferries()
