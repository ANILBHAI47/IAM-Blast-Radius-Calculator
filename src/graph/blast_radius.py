def blast_radius(graph, start_node):
    """
    Find all nodes reachable from the given starting node using
    Depth First Search (DFS).

    Args:
        graph (dict): Adjacency list representing the IAM graph.
        start_node (str): The node to start traversal from.

    Returns:
        set: All reachable nodes from the starting node.
    """

    if start_node not in graph:
        raise ValueError(f"{start_node} does not exist in the graph.")

    visited = set()
    stack = [start_node]

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited