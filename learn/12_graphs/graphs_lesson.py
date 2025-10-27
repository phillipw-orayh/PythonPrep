"""
INTERACTIVE LESSON: Graphs in Python

Graphs are networks of nodes (vertices) connected by edges.
They model relationships and connections between entities.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_graphs.py
"""

from collections import deque, defaultdict
import heapq

# ============================================================================
# PART 1: WHAT ARE GRAPHS?
# ============================================================================
"""
Graphs consist of vertices (nodes) and edges (connections).
- Directed vs Undirected edges
- Weighted vs Unweighted edges
- Cyclic vs Acyclic (DAG - Directed Acyclic Graph)
- Representations: Adjacency List, Adjacency Matrix, Edge List
- Used in: social networks, maps, dependencies, web links, networks
"""

# ============================================================================
# PART 2: BASIC GRAPH OPERATIONS
# ============================================================================

def graph_basics_demo():
    """Demonstrates basic graph operations."""
    # Adjacency List (most common)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Adjacency Matrix
    # For graph with n vertices (0 to n-1)
    n = 4
    adj_matrix = [[0] * n for _ in range(n)]
    # Add edge between 0 and 1
    adj_matrix[0][1] = 1
    adj_matrix[1][0] = 1  # For undirected

    # Weighted graph (adjacency list)
    weighted_graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('D', 5)],
        'C': [('A', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    # DFS (Depth-First Search)
    def dfs(graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start)

        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

        return visited

    # BFS (Breadth-First Search)
    def bfs(graph, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return visited

    return graph


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_num_islands(grid: list) -> int:
    """
    Count number of islands in a 2D grid.
    1 = land, 0 = water. Islands are connected horizontally/vertically.
    Classic interview question!

    Example:
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        Output: 3

    Hint: Use DFS/BFS from each unvisited land cell
    """
    # TODO: Implement this function
    pass


def exercise_2_has_path(graph: dict, start: str, end: str) -> bool:
    """
    Check if there's a path from start to end in a directed graph.

    Example:
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        has_path(graph, 'A', 'D') -> True
        has_path(graph, 'D', 'A') -> False

    Hint: Use DFS or BFS
    """
    # TODO: Implement this function
    pass


def exercise_3_clone_graph(node: 'Node') -> 'Node':
    """
    Clone (deep copy) an undirected graph.
    Node class has val and neighbors list.

    Example:
        Input: Graph with nodes 1-2-3-4 (fully connected)
        Output: Deep copy of the graph

    Hint: Use DFS/BFS with a hash map to track cloned nodes
    """
    # TODO: Implement this function
    # Note: Assume Node class has val and neighbors attributes
    pass


# ============================================================================
# PART 4: INTERMEDIATE GRAPH OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced graph operations."""
    # Detecting cycle in directed graph
    def has_cycle_directed(graph):
        def dfs(node, visited, rec_stack):
            visited.add(node)
            rec_stack.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor, visited, rec_stack):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(node)
            return False

        visited = set()
        for node in graph:
            if node not in visited:
                if dfs(node, visited, set()):
                    return True
        return False

    # Topological Sort (DAG only)
    def topological_sort(graph):
        def dfs(node, visited, stack):
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, visited, stack)
            stack.append(node)

        visited = set()
        stack = []

        for node in graph:
            if node not in visited:
                dfs(node, visited, stack)

        return stack[::-1]

    return has_cycle_directed, topological_sort


def exercise_4_course_schedule(num_courses: int, prerequisites: list) -> bool:
    """
    Check if you can finish all courses given prerequisites.
    prerequisites[i] = [a, b] means must take b before a.
    This is cycle detection in directed graph!

    Example:
        num_courses = 2, prerequisites = [[1,0]]
        Output: True (can take 0 then 1)

        num_courses = 2, prerequisites = [[1,0],[0,1]]
        Output: False (circular dependency)

    Hint: Build graph and detect cycle using DFS
    """
    # TODO: Implement this function
    pass


def exercise_5_shortest_path_unweighted(graph: dict, start: str, end: str) -> int:
    """
    Find shortest path length between start and end in unweighted graph.
    Return -1 if no path exists.

    Example:
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        shortest_path_unweighted(graph, 'A', 'D') -> 2

    Hint: Use BFS, track distance
    """
    # TODO: Implement this function
    pass


def exercise_6_all_paths(graph: dict, start: str, end: str) -> list:
    """
    Find all paths from start to end in a directed graph.

    Example:
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        all_paths(graph, 'A', 'D') -> [['A','B','D'], ['A','C','D']]

    Hint: Use DFS with backtracking, track current path
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED GRAPH TECHNIQUES
# ============================================================================

def exercise_7_dijkstra_shortest_path(graph: dict, start: str, end: str) -> int:
    """
    Find shortest path in a weighted graph using Dijkstra's algorithm.
    graph[node] = [(neighbor, weight), ...]

    Example:
        graph = {
            'A': [('B', 4), ('C', 2)],
            'B': [('D', 5)],
            'C': [('D', 1)],
            'D': []
        }
        dijkstra_shortest_path(graph, 'A', 'D') -> 3 (A->C->D)

    Hint: Use min-heap (priority queue) with distances
    """
    # TODO: Implement this function
    pass


def exercise_8_network_delay_time(times: list, n: int, k: int) -> int:
    """
    Network delay time problem (Dijkstra application).
    times[i] = [source, target, time]. Find time for signal to reach all nodes from k.
    Return -1 if impossible.

    Example:
        times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        Output: 2 (all nodes reachable in 2 units)

    Hint: Dijkstra's algorithm, return max distance
    """
    # TODO: Implement this function
    pass


def exercise_9_min_spanning_tree(edges: list, n: int) -> int:
    """
    Find minimum spanning tree cost using Union-Find (Kruskal's algorithm).
    edges[i] = [u, v, weight]

    Example:
        edges = [[0,1,10],[0,2,6],[0,3,5],[1,3,15],[2,3,4]]
        n = 4
        Output: 19 (edges: 2-3:4, 0-3:5, 0-1:10)

    Hint: Sort edges by weight, use Union-Find to detect cycles
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Graphs:

1. SOCIAL NETWORKS
   - Friend connections
   - Recommendation algorithms
   - Influence propagation
   Example: Facebook friend suggestions, LinkedIn connections

2. MAPS AND NAVIGATION
   - Road networks
   - Shortest path (GPS)
   - Traffic optimization
   Example: Google Maps, Uber routing

3. WEB AND SEO
   - PageRank algorithm
   - Web crawler
   - Link analysis
   Example: Google Search ranking

4. NETWORKS
   - Computer networks
   - Internet routing
   - Load balancing
   Example: BGP routing protocol

5. DEPENDENCIES
   - Package managers
   - Build systems
   - Task scheduling
   Example: npm, Maven, Make

6. BIOLOGY
   - Protein interaction networks
   - Disease spread modeling
   - Gene regulatory networks
   Example: COVID-19 contact tracing
"""

def exercise_10_word_ladder(begin_word: str, end_word: str, word_list: list) -> int:
    """
    Find shortest transformation sequence from begin_word to end_word.
    Each step can only change one letter, and must be in word_list.
    Classic BFS problem!

    Example:
        begin_word = "hit", end_word = "cog"
        word_list = ["hot","dot","dog","lot","log","cog"]
        Output: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")

    Hint: Build graph where words differ by one letter are connected, use BFS
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("GRAPH LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Number of Islands:")
    try:
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        assert exercise_1_num_islands(grid) == 3
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Has Path:")
    try:
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        assert exercise_2_has_path(graph, 'A', 'D') == True
        assert exercise_2_has_path(graph, 'D', 'A') == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3 (skipped - requires special Node class)
    print("\n3. Clone Graph:")
    print("   ⚠ SKIPPED - Requires special Node class with neighbors")

    # Test exercise 4
    print("\n4. Course Schedule:")
    try:
        assert exercise_4_course_schedule(2, [[1,0]]) == True
        assert exercise_4_course_schedule(2, [[1,0],[0,1]]) == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. Shortest Path Unweighted:")
    try:
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        assert exercise_5_shortest_path_unweighted(graph, 'A', 'D') == 2
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. All Paths:")
    try:
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        result = exercise_6_all_paths(graph, 'A', 'D')
        assert len(result) == 2
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Dijkstra Shortest Path:")
    try:
        graph = {
            'A': [('B', 4), ('C', 2)],
            'B': [('D', 5)],
            'C': [('D', 1)],
            'D': []
        }
        assert exercise_7_dijkstra_shortest_path(graph, 'A', 'D') == 3
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Network Delay Time:")
    try:
        assert exercise_8_network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. Min Spanning Tree:")
    try:
        edges = [[0,1,10],[0,2,6],[0,3,5],[1,3,15],[2,3,4]]
        assert exercise_9_min_spanning_tree(edges, 4) == 19
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Word Ladder:")
    try:
        result = exercise_10_word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"])
        assert result == 5
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
