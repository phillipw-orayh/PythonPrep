"""
INTERACTIVE LESSON: Queues in Python

Queues are FIFO (First In, First Out) data structures - like a line at a store.
The first item added is the first one removed.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_queues.py
"""

from collections import deque

# ============================================================================
# PART 1: WHAT ARE QUEUES?
# ============================================================================
"""
Queues follow the First In, First Out (FIFO) principle.
- Think of people in line: first person in is first served
- Main operations: enqueue (add to back), dequeue (remove from front)
- Python's collections.deque is optimized for queues
- O(1) time complexity for enqueue and dequeue (with deque)
- Used in: breadth-first search, task scheduling, message queues, buffering
"""

# ============================================================================
# PART 2: BASIC QUEUE OPERATIONS
# ============================================================================

def queue_basics_demo():
    """Demonstrates basic queue operations using deque."""
    # Creating a queue (using deque)
    queue = deque()

    # Enqueue (add to back)
    queue.append(1)  # Queue: [1]
    queue.append(2)  # Queue: [1, 2]
    queue.append(3)  # Queue: [1, 2, 3]

    # Peek front
    if queue:
        front = queue[0]  # 1

    # Dequeue (remove from front)
    removed = queue.popleft()  # Returns 1, Queue: [2, 3]

    # Check if empty
    is_empty = len(queue) == 0  # False

    # Size
    size = len(queue)  # 2

    return queue


class Queue:
    """Simple queue implementation using deque."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Add item to back of queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return front item."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        """Return front item without removing."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        """Check if queue is empty."""
        return len(self._items) == 0

    def size(self):
        """Return number of items in queue."""
        return len(self._items)


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_reverse_queue(queue: deque) -> deque:
    """
    Reverse a queue (return new queue with reversed elements).

    Example:
        reverse_queue(deque([1, 2, 3, 4])) -> deque([4, 3, 2, 1])

    Hint: Use a stack (list) to reverse, then rebuild queue
    """
    # TODO: Implement this function
    pass


def exercise_2_first_unique_character(s: str) -> int:
    """
    Find the index of the first non-repeating character.
    Return -1 if none exists.

    Example:
        first_unique_character("leetcode") -> 0  # 'l' appears once
        first_unique_character("loveleetcode") -> 2  # 'v' appears once
        first_unique_character("aabb") -> -1

    Hint: Count frequencies, then iterate to find first with count 1
    """
    # TODO: Implement this function
    pass


def exercise_3_queue_using_stacks(operations: list) -> list:
    """
    Implement a queue using two stacks.
    Operations: ("enqueue", value), ("dequeue",), ("peek",)
    Return results of dequeue and peek operations.

    Example:
        queue_using_stacks([("enqueue", 1), ("enqueue", 2), ("dequeue",)])
        -> [1]

    Hint: Use one stack for enqueue, transfer to other stack for dequeue
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE QUEUE OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced queue usage."""
    # Priority queue (using heap)
    import heapq
    pq = []
    heapq.heappush(pq, (2, "task2"))  # (priority, task)
    heapq.heappush(pq, (1, "task1"))
    heapq.heappush(pq, (3, "task3"))
    priority, task = heapq.heappop(pq)  # Gets (1, "task1")

    # Circular queue (bounded)
    class CircularQueue:
        def __init__(self, k):
            self.queue = [None] * k
            self.front = 0
            self.rear = -1
            self.size = 0
            self.capacity = k

        def enqueue(self, value):
            if self.size == self.capacity:
                return False
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = value
            self.size += 1
            return True

        def dequeue(self):
            if self.size == 0:
                return None
            value = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return value

    return pq, CircularQueue


def exercise_4_sliding_window_maximum(nums: list, k: int) -> list:
    """
    Find the maximum in each sliding window of size k.

    Example:
        sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
        -> [3, 3, 5, 5, 6, 7]
        # Windows: [1,3,-1], [3,-1,-3], [-1,-3,5], [-3,5,3], [5,3,6], [3,6,7]

    Hint: Use deque to maintain indices of potential maximums
    """
    # TODO: Implement this function
    pass


def exercise_5_moving_average(stream: list, size: int) -> list:
    """
    Calculate moving average of last 'size' elements in a stream.

    Example:
        moving_average([1, 10, 3, 5], 3) -> [1.0, 5.5, 4.666..., 6.0]
        # After 1: [1] -> avg 1.0
        # After 10: [1, 10] -> avg 5.5
        # After 3: [1, 10, 3] -> avg 4.666...
        # After 5: [10, 3, 5] -> avg 6.0

    Hint: Use deque with maxlen=size, maintain running sum
    """
    # TODO: Implement this function
    pass


def exercise_6_recent_counter(timestamps: list, window: int) -> list:
    """
    Count requests in the last 'window' milliseconds for each timestamp.

    Example:
        recent_counter([1, 100, 3001, 3002], 3000)
        -> [1, 2, 3, 3]
        # At 1: [1] (1 request)
        # At 100: [1, 100] (2 requests)
        # At 3001: [1, 100, 3001] all within 3000ms (3 requests)
        # At 3002: [100, 3001, 3002] (1 expired, 3 remain)

    Hint: Use queue, dequeue timestamps older than current - window
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED QUEUE TECHNIQUES
# ============================================================================

def exercise_7_shortest_path_bfs(grid: list, start: tuple, end: tuple) -> int:
    """
    Find shortest path length in a grid using BFS (Breadth-First Search).
    0 = walkable, 1 = wall. Return -1 if no path exists.

    Example:
        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        shortest_path_bfs(grid, (0, 0), (2, 2)) -> 4
        # Path: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)

    Hint: Use queue for BFS, track visited cells, count steps
    """
    # TODO: Implement this function
    pass


def exercise_8_perfect_squares(n: int) -> int:
    """
    Find minimum number of perfect squares that sum to n.
    Use BFS approach.

    Example:
        perfect_squares(12) -> 3  # 12 = 4 + 4 + 4
        perfect_squares(13) -> 2  # 13 = 4 + 9

    Hint: BFS where each state is a remaining sum, edges are subtracting squares
    """
    # TODO: Implement this function
    pass


def exercise_9_rotting_oranges(grid: list) -> int:
    """
    Grid with 0=empty, 1=fresh orange, 2=rotten orange.
    Each minute, rotten oranges rot adjacent fresh oranges.
    Return minutes until all oranges rot, or -1 if impossible.

    Example:
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
        rotting_oranges(grid) -> 4

    Hint: Multi-source BFS starting from all rotten oranges
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Queues:

1. TASK SCHEDULING
   - Operating system process scheduling
   - Print job queues
   - Background job processing
   Example: CPU scheduler managing processes

2. MESSAGE QUEUES
   - Microservices communication
   - Event-driven architectures
   - Asynchronous processing
   Example: RabbitMQ, Apache Kafka, AWS SQS

3. BREADTH-FIRST SEARCH
   - Shortest path algorithms
   - Level-order tree traversal
   - Web crawlers
   Example: Finding friends within N degrees on social networks

4. BUFFERING
   - IO buffers (keyboard, printer)
   - Video streaming
   - Network packet handling
   Example: YouTube video buffering

5. REQUEST HANDLING
   - Web server request queues
   - API rate limiting
   - Load balancing
   Example: Handling HTTP requests in order received

6. REAL-TIME SYSTEMS
   - Call center queues
   - Customer service ticketing
   - Order processing
   Example: Support ticket systems (first come, first served)
"""

def exercise_10_design_circular_queue(operations: list, capacity: int) -> list:
    """
    Implement a circular queue with fixed capacity.
    Operations: ("enqueue", value), ("dequeue",), ("front",), ("rear",), ("is_empty",), ("is_full",)
    Return results for operations that return values.
    Common interview question!

    Example:
        operations = [
            ("enqueue", 1),
            ("enqueue", 2),
            ("dequeue",),
            ("enqueue", 3),
            ("front",)
        ]
        design_circular_queue(operations, 3) -> [1, 3]

    Hint: Use array with front/rear pointers that wrap around
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("QUEUE LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Reverse Queue:")
    try:
        result = exercise_1_reverse_queue(deque([1, 2, 3, 4]))
        assert list(result) == [4, 3, 2, 1]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. First Unique Character:")
    try:
        assert exercise_2_first_unique_character("leetcode") == 0
        assert exercise_2_first_unique_character("loveleetcode") == 2
        assert exercise_2_first_unique_character("aabb") == -1
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Queue Using Stacks:")
    try:
        result = exercise_3_queue_using_stacks([("enqueue", 1), ("enqueue", 2), ("dequeue",)])
        assert result == [1]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Sliding Window Maximum:")
    try:
        result = exercise_4_sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
        assert result == [3, 3, 5, 5, 6, 7]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. Moving Average:")
    try:
        result = exercise_5_moving_average([1, 10, 3, 5], 3)
        assert abs(result[0] - 1.0) < 0.01
        assert abs(result[1] - 5.5) < 0.01
        assert abs(result[2] - 4.666) < 0.01
        assert abs(result[3] - 6.0) < 0.01
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Recent Counter:")
    try:
        result = exercise_6_recent_counter([1, 100, 3001, 3002], 3000)
        assert result == [1, 2, 3, 3]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Shortest Path BFS:")
    try:
        grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
        result = exercise_7_shortest_path_bfs(grid, (0, 0), (2, 2))
        assert result == 4
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Perfect Squares:")
    try:
        assert exercise_8_perfect_squares(12) == 3
        assert exercise_8_perfect_squares(13) == 2
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. Rotting Oranges:")
    try:
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        result = exercise_9_rotting_oranges(grid)
        assert result == 4
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Design Circular Queue:")
    try:
        ops = [("enqueue", 1), ("enqueue", 2), ("dequeue",), ("enqueue", 3), ("front",)]
        result = exercise_10_design_circular_queue(ops, 3)
        assert result == [1, 3]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
