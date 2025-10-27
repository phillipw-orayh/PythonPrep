"""
INTERACTIVE LESSON: Deques in Python

Deques (double-ended queues) allow adding/removing from both ends efficiently.
They combine the flexibility of stacks and queues.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_deques.py
"""

from collections import deque

# ============================================================================
# PART 1: WHAT ARE DEQUES?
# ============================================================================
"""
Deques (pronounced "deck") are double-ended queues.
- Can add/remove from BOTH front and back
- Combines stack and queue operations
- Python's collections.deque is highly optimized
- O(1) time for append/pop from either end
- O(n) time for middle insertions/deletions
- Used in: sliding windows, palindrome checking, work stealing algorithms
"""

# ============================================================================
# PART 2: BASIC DEQUE OPERATIONS
# ============================================================================

def deque_basics_demo():
    """Demonstrates basic deque operations."""
    # Creating a deque
    dq = deque()

    # Add to right (back)
    dq.append(1)  # deque([1])
    dq.append(2)  # deque([1, 2])

    # Add to left (front)
    dq.appendleft(0)  # deque([0, 1, 2])

    # Remove from right
    right_val = dq.pop()  # Returns 2, deque([0, 1])

    # Remove from left
    left_val = dq.popleft()  # Returns 0, deque([1])

    # Peek from either end
    if dq:
        front = dq[0]  # 1
        back = dq[-1]  # 1

    # Rotate (move elements)
    dq.extend([2, 3, 4])  # deque([1, 2, 3, 4])
    dq.rotate(1)  # deque([4, 1, 2, 3]) - rotates right
    dq.rotate(-1)  # deque([1, 2, 3, 4]) - rotates left

    # Max length deque
    bounded = deque(maxlen=3)
    bounded.extend([1, 2, 3, 4])  # deque([2, 3, 4]) - auto-removes from left

    return dq


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_palindrome_check(s: str) -> bool:
    """
    Check if a string is a palindrome using a deque.

    Example:
        palindrome_check("racecar") -> True
        palindrome_check("hello") -> False

    Hint: Add all characters to deque, compare front and back iteratively
    """
    # TODO: Implement this function
    pass


def exercise_2_reverse_first_k(dq: deque, k: int) -> deque:
    """
    Reverse the first k elements of a deque.

    Example:
        reverse_first_k(deque([1, 2, 3, 4, 5]), 3) -> deque([3, 2, 1, 4, 5])

    Hint: Remove first k elements, push to stack, then add back to front
    """
    # TODO: Implement this function
    pass


def exercise_3_max_sliding_window_deque(nums: list, k: int) -> list:
    """
    Find maximum of each sliding window using deque.
    Deque stores indices of potential maximums.

    Example:
        max_sliding_window_deque([1, 3, -1, -3, 5, 3, 6, 7], 3)
        -> [3, 3, 5, 5, 6, 7]

    Hint: Maintain deque of indices in decreasing order of values
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE DEQUE OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced deque usage."""
    # Using deque as a circular buffer
    buffer = deque(maxlen=5)
    for i in range(10):
        buffer.append(i)  # Keeps only last 5

    # Deque for LRU cache
    class LRUCache:
        def __init__(self, capacity):
            self.cache = {}
            self.order = deque()
            self.capacity = capacity

        def get(self, key):
            if key in self.cache:
                self.order.remove(key)
                self.order.append(key)
                return self.cache[key]
            return -1

        def put(self, key, value):
            if key in self.cache:
                self.order.remove(key)
            elif len(self.cache) >= self.capacity:
                lru = self.order.popleft()
                del self.cache[lru]

            self.cache[key] = value
            self.order.append(key)

    return buffer, LRUCache


def exercise_4_min_window_deque(nums: list, k: int) -> list:
    """
    Find minimum of each sliding window of size k.

    Example:
        min_window_deque([1, 3, -1, -3, 5, 3], 3)
        -> [1, -1, -3, -3]

    Hint: Similar to max sliding window, but maintain increasing order
    """
    # TODO: Implement this function
    pass


def exercise_5_first_negative_in_window(nums: list, k: int) -> list:
    """
    Find first negative number in each window of size k.
    Return 0 if no negative number exists.

    Example:
        first_negative_in_window([12, -1, -7, 8, -15, 30, 16, 28], 3)
        -> [-1, -1, -7, -15, -15, 0]

    Hint: Use deque to track indices of negative numbers
    """
    # TODO: Implement this function
    pass


def exercise_6_rotate_array_deque(nums: list, k: int) -> list:
    """
    Rotate array to the right by k positions using deque.

    Example:
        rotate_array_deque([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]

    Hint: Use deque.rotate() method
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED DEQUE TECHNIQUES
# ============================================================================

def exercise_7_jump_game_reachable(nums: list) -> bool:
    """
    Determine if you can reach the last index.
    Each element represents max jump length from that position.

    Example:
        jump_game_reachable([2, 3, 1, 1, 4]) -> True
        # Can jump: 0->1->4 or 0->2->3->4
        jump_game_reachable([3, 2, 1, 0, 4]) -> False

    Hint: Use deque for BFS to explore reachable indices
    """
    # TODO: Implement this function
    pass


def exercise_8_constrained_subsequence_sum(nums: list, k: int) -> int:
    """
    Find maximum sum of non-empty subsequence where adjacent elements
    are at most k indices apart.

    Example:
        constrained_subsequence_sum([10, 2, -10, 5, 20], 2) -> 37
        # Pick 10, 5, 20 (indices 0, 3, 4)

    Hint: Use deque with DP to track maximum sums within window
    """
    # TODO: Implement this function
    pass


def exercise_9_shortest_subarray_sum(nums: list, k: int) -> int:
    """
    Find length of shortest non-empty subarray with sum >= k.
    Return -1 if no such subarray exists.

    Example:
        shortest_subarray_sum([2, -1, 2], 3) -> 3
        shortest_subarray_sum([1, 2], 4) -> -1

    Hint: Use deque with prefix sums to find shortest valid window
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Deques:

1. BROWSER HISTORY
   - Back/forward navigation
   - Recent pages at both ends
   - Bounded history with maxlen
   Example: Chrome's navigation allowing back/forward

2. UNDO/REDO WITH LIMITS
   - Bounded undo/redo stacks
   - Memory-efficient history
   - Auto-remove oldest actions
   Example: Text editors with max undo depth

3. WORK STEALING SCHEDULERS
   - Thread pool task queues
   - Workers steal from both ends
   - Load balancing
   Example: Fork/join framework in Java

4. SLIDING WINDOW ALGORITHMS
   - Stock price analysis
   - Network monitoring
   - Real-time analytics
   Example: Finding peak values in time windows

5. CIRCULAR BUFFERS
   - Audio/video streaming
   - Log rotation
   - Fixed-size caches
   Example: Network packet buffering

6. GAME DEVELOPMENT
   - Entity management
   - Recent player actions
   - Combo systems
   Example: Fighting game move buffers
"""

def exercise_10_gas_station_circuit(gas: list, cost: list) -> int:
    """
    Circular route of gas stations. Can you complete the circuit?
    Return starting station index, or -1 if impossible.

    Example:
        gas_station_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) -> 3
        # Start at index 3: gas=4, cost=1 (net +3)
        # Then index 4: gas=5, cost=2 (net +6)
        # Then index 0: gas=1, cost=3 (net +4)
        # Then index 1: gas=2, cost=4 (net +2)
        # Then index 2: gas=3, cost=5 (net 0) - Success!

    Hint: Track cumulative tank, if negative reset start position
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("DEQUE LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Palindrome Check:")
    try:
        assert exercise_1_palindrome_check("racecar") == True
        assert exercise_1_palindrome_check("hello") == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Reverse First K:")
    try:
        result = exercise_2_reverse_first_k(deque([1, 2, 3, 4, 5]), 3)
        assert list(result) == [3, 2, 1, 4, 5]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Max Sliding Window Deque:")
    try:
        result = exercise_3_max_sliding_window_deque([1, 3, -1, -3, 5, 3, 6, 7], 3)
        assert result == [3, 3, 5, 5, 6, 7]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Min Window Deque:")
    try:
        result = exercise_4_min_window_deque([1, 3, -1, -3, 5, 3], 3)
        assert result == [1, -1, -3, -3]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. First Negative in Window:")
    try:
        result = exercise_5_first_negative_in_window([12, -1, -7, 8, -15, 30, 16, 28], 3)
        assert result == [-1, -1, -7, -15, -15, 0]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Rotate Array Deque:")
    try:
        result = exercise_6_rotate_array_deque([1, 2, 3, 4, 5], 2)
        assert result == [4, 5, 1, 2, 3]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Jump Game Reachable:")
    try:
        assert exercise_7_jump_game_reachable([2, 3, 1, 1, 4]) == True
        assert exercise_7_jump_game_reachable([3, 2, 1, 0, 4]) == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Constrained Subsequence Sum:")
    try:
        result = exercise_8_constrained_subsequence_sum([10, 2, -10, 5, 20], 2)
        assert result == 37
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. Shortest Subarray Sum:")
    try:
        assert exercise_9_shortest_subarray_sum([2, -1, 2], 3) == 3
        assert exercise_9_shortest_subarray_sum([1, 2], 4) == -1
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Gas Station Circuit:")
    try:
        result = exercise_10_gas_station_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
        assert result == 3
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
