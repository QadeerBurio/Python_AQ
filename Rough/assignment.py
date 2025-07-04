import heapq

def dijkstra(graph, start):
    # Step 1: Set initial distances
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    visited = set()
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return shortest_distances

# Graph for warehouse problem
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('E', 3)],
    'D': [('E', 2)],
    'E': [('F', 1)],
    'F': []
}

# Run the algorithm from node 'A'
start_node = 'A'
distances = dijkstra(graph, start_node)

# Print the result
print("Shortest distances from node A:")
for node, distance in distances.items():
    print(f"Distance to {node}: {distance}")
