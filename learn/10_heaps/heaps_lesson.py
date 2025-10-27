"""
INTERACTIVE LESSON: Heaps in Python

Heaps are tree-based data structures that maintain a partial ordering property.
Python's heapq module provides an efficient min-heap implementation.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_heaps.py
"""

import heapq

# ============================================================================
# PART 1: WHAT ARE HEAPS?
# ============================================================================
"""
Heaps are complete binary trees where parent nodes are ordered with respect to children.
- Min-heap: parent ≤ children (smallest element at root)
- Max-heap: parent ≥ children (largest element at root)
- Python's heapq implements min-heap
- O(log n) for insert and extract min/max
- O(1) for peek min/max
- O(n) to build heap from list
- Useful for priority queues, finding k largest/smallest elements
"""

# ============================================================================
# PART 2: BASIC HEAP OPERATIONS
# ============================================================================

def heap_basics_demo():
    """Demonstrates basic heap operations."""
    # Creating a heap
    heap = []
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 3)
    # heap is now [1, 5, 3] - min element at index 0

    # Convert list to heap in-place
    numbers = [5, 3, 7, 1, 9, 2]
    heapq.heapify(numbers)  # Now a valid min-heap

    # Extract minimum
    min_val = heapq.heappop(numbers)  # Returns 1

    # Peek minimum (without removing)
    if numbers:
        min_peek = numbers[0]  # First element is always minimum

    # Push and pop in one operation
    replaced = heapq.heapreplace(numbers, 10)  # Pop min, then push 10

    # Push and pop (pushes first)
    result = heapq.heappushpop(numbers, 0)  # Push 0, then pop minimum

    return heap, numbers


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_find_kth_smallest(numbers: list, k: int) -> int:
    """
    Find the kth smallest element in a list.

    Example:
        find_kth_smallest([7, 10, 4, 3, 20, 15], 3) -> 7
        find_kth_smallest([1, 5, 2, 8, 3], 2) -> 2

    Hint: Use heapq.nsmallest()
    """
    # TODO: Implement this function
    pass


def exercise_2_find_k_largest(numbers: list, k: int) -> list:
    """
    Find the k largest elements in a list (any order).

    Example:
        find_k_largest([1, 5, 2, 8, 3], 2) -> [8, 5] or [5, 8]
        find_k_largest([10, 5, 20, 15], 3) -> [20, 15, 10]

    Hint: Use heapq.nlargest()
    """
    # TODO: Implement this function
    pass


def exercise_3_merge_k_sorted_lists(lists: list) -> list:
    """
    Merge k sorted lists into one sorted list.

    Example:
        merge_k_sorted_lists([[1, 4, 7], [2, 5, 8], [3, 6, 9]]) ->
        [1, 2, 3, 4, 5, 6, 7, 8, 9]

    Hint: Use heapq.merge()
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE HEAP OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced heap usage."""
    # Max-heap using negative values
    max_heap = []
    for num in [3, 1, 4, 1, 5]:
        heapq.heappush(max_heap, -num)  # Negate to simulate max-heap

    max_val = -heapq.heappop(max_heap)  # Pop and negate to get max

    # Priority queue with tuples
    pq = []
    heapq.heappush(pq, (2, "task2"))
    heapq.heappush(pq, (1, "task1"))
    heapq.heappush(pq, (3, "task3"))
    priority, task = heapq.heappop(pq)  # Gets (1, "task1")

    # Finding median with two heaps
    # Use max-heap for lower half, min-heap for upper half

    return max_heap, pq


def exercise_4_heap_sort(numbers: list) -> list:
    """
    Sort a list using heap sort (return new list).

    Example:
        heap_sort([3, 1, 4, 1, 5, 9, 2]) -> [1, 1, 2, 3, 4, 5, 9]

    Hint: heapify, then repeatedly pop minimum
    """
    # TODO: Implement this function
    pass


def exercise_5_find_median(numbers: list) -> float:
    """
    Find the median of a list of numbers.

    Example:
        find_median([1, 3, 5]) -> 3
        find_median([1, 2, 3, 4]) -> 2.5

    Hint: Sort or use heaps, then find middle element(s)
    """
    # TODO: Implement this function
    pass


def exercise_6_top_k_frequent(numbers: list, k: int) -> list:
    """
    Find the k most frequent elements.

    Example:
        top_k_frequent([1, 1, 1, 2, 2, 3], 2) -> [1, 2]
        top_k_frequent([1, 2, 2, 3, 3, 3], 2) -> [3, 2]

    Hint: Count frequencies, use heap on counts
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED HEAP TECHNIQUES
# ============================================================================

def exercise_7_running_median(stream: list) -> list:
    """
    Calculate running median as numbers come in a stream.

    Example:
        running_median([1, 2, 3, 4]) -> [1, 1.5, 2, 2.5]
        # After 1: median is 1
        # After 1, 2: median is 1.5
        # After 1, 2, 3: median is 2
        # After 1, 2, 3, 4: median is 2.5

    Hint: Use two heaps (max-heap for lower half, min-heap for upper half)
    """
    # TODO: Implement this function
    pass


def exercise_8_connect_ropes(ropes: list) -> int:
    """
    Connect ropes with minimum cost. Cost to connect two ropes is their sum.
    Classic heap problem!

    Example:
        connect_ropes([4, 3, 2, 6]) -> 29
        # Connect 2+3=5 (cost 5), then 4+5=9 (cost 9), then 6+9=15 (cost 15)
        # Total cost: 5+9+15=29

    Hint: Always connect two shortest ropes. Use min-heap.
    """
    # TODO: Implement this function
    pass


def exercise_9_k_closest_points(points: list, k: int) -> list:
    """
    Find k closest points to origin (0, 0).
    Each point is a tuple (x, y).

    Example:
        k_closest_points([(1, 1), (3, 3), (2, 2)], 2) ->
        [(1, 1), (2, 2)]

    Hint: Calculate distance for each point, use heap
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Heaps:

1. TASK SCHEDULING
   - Priority queues for job scheduling
   - CPU scheduling algorithms
   - Event-driven simulations
   Example: Always process highest priority task first

2. REAL-TIME SYSTEMS
   - Finding top K elements in stream
   - Running statistics (median, percentiles)
   - Sliding window problems
   Example: Finding top 10 trending topics in real-time

3. GRAPH ALGORITHMS
   - Dijkstra's shortest path
   - Prim's minimum spanning tree
   - A* pathfinding
   Example: Finding shortest route in maps

4. DATA COMPRESSION
   - Huffman coding
   - Optimal merge patterns
   - File compression
   Example: Building optimal encoding trees

5. LOAD BALANCING
   - Distributing tasks to servers
   - Resource allocation
   - Rate limiting
   Example: Always assign task to least loaded server

6. RECOMMENDATION SYSTEMS
   - Top K recommendations
   - Nearest neighbors
   - Similarity ranking
   Example: Finding most similar products
"""

def exercise_10_task_scheduler(tasks: list, k: int) -> int:
    """
    Schedule tasks with cooldown period k between same tasks.
    Return minimum time needed.

    Example:
        task_scheduler(['A', 'A', 'A', 'B', 'B', 'B'], 2) -> 8
        # Schedule: A -> B -> idle -> A -> B -> idle -> A -> B
        # Total time: 8

    Hint: Use heap for task frequencies, schedule greedily
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("HEAP LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Find Kth Smallest:")
    try:
        assert exercise_1_find_kth_smallest([7, 10, 4, 3, 20, 15], 3) == 7
        assert exercise_1_find_kth_smallest([1, 5, 2, 8, 3], 2) == 2
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Find K Largest:")
    try:
        result = exercise_2_find_k_largest([1, 5, 2, 8, 3], 2)
        assert set(result) == {8, 5}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Merge K Sorted Lists:")
    try:
        result = exercise_3_merge_k_sorted_lists([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Heap Sort:")
    try:
        assert exercise_4_heap_sort([3, 1, 4, 1, 5, 9, 2]) == [1, 1, 2, 3, 4, 5, 9]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. Find Median:")
    try:
        assert exercise_5_find_median([1, 3, 5]) == 3
        assert exercise_5_find_median([1, 2, 3, 4]) == 2.5
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Top K Frequent:")
    try:
        result = exercise_6_top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        assert set(result) == {1, 2}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Running Median:")
    try:
        result = exercise_7_running_median([1, 2, 3, 4])
        assert result == [1, 1.5, 2, 2.5]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Connect Ropes:")
    try:
        assert exercise_8_connect_ropes([4, 3, 2, 6]) == 29
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. K Closest Points:")
    try:
        result = exercise_9_k_closest_points([(1, 1), (3, 3), (2, 2)], 2)
        assert len(result) == 2
        assert (1, 1) in result
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Task Scheduler:")
    try:
        result = exercise_10_task_scheduler(['A', 'A', 'A', 'B', 'B', 'B'], 2)
        assert result == 8
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
