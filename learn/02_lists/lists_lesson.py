"""
INTERACTIVE LESSON: Lists in Python

Lists are mutable, ordered sequences that can contain elements of any type.
They are one of the most versatile and commonly used data structures in Python.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_lists.py
"""

# ============================================================================
# PART 1: WHAT ARE LISTS?
# ============================================================================
"""
Lists are ordered, mutable collections that can hold items of different types.
- Created with square brackets: [1, 2, 3]
- Mutable: can modify, add, or remove elements
- Indexed: access elements by position (0-based)
- Dynamic: can grow or shrink in size
- Can contain mixed types: [1, "hello", 3.14, True]
"""

# ============================================================================
# PART 2: BASIC LIST OPERATIONS
# ============================================================================

def list_basics_demo():
    """Demonstrates basic list operations."""
    # Creating lists
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    empty = []

    # Accessing elements
    first = numbers[0]      # 1
    last = numbers[-1]      # 5
    slice_result = numbers[1:4]  # [2, 3, 4]

    # Modifying elements
    numbers[0] = 10         # [10, 2, 3, 4, 5]

    # Adding elements
    numbers.append(6)       # [10, 2, 3, 4, 5, 6]
    numbers.insert(0, 0)    # [0, 10, 2, 3, 4, 5, 6]
    numbers.extend([7, 8])  # [0, 10, 2, 3, 4, 5, 6, 7, 8]

    # Removing elements
    numbers.pop()           # Removes and returns 8
    numbers.remove(10)      # Removes first occurrence of 10
    del numbers[0]          # Removes element at index 0

    # Other operations
    length = len(numbers)
    contains = 5 in numbers
    index = numbers.index(5)  # Position of 5

    return numbers


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_sum_list(numbers: list) -> int:
    """
    Calculate the sum of all numbers in a list.

    Example:
        sum_list([1, 2, 3, 4, 5]) -> 15
        sum_list([10, 20, 30]) -> 60

    Hint: Use a loop or the built-in sum() function
    """
    # TODO: Implement this function
    pass


def exercise_2_find_max(numbers: list) -> int:
    """
    Find the maximum value in a list of numbers.

    Example:
        find_max([1, 5, 3, 9, 2]) -> 9
        find_max([10, 20, 15]) -> 20

    Hint: Use max() function or loop through comparing values
    """
    # TODO: Implement this function
    pass


def exercise_3_reverse_list(items: list) -> list:
    """
    Reverse a list (return a new list, don't modify original).

    Example:
        reverse_list([1, 2, 3, 4]) -> [4, 3, 2, 1]
        reverse_list(['a', 'b', 'c']) -> ['c', 'b', 'a']

    Hint: Use slicing [::-1] or reversed() function
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE LIST OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced list operations."""
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]

    # Sorting
    sorted_asc = sorted(numbers)          # [1, 1, 2, 3, 4, 5, 6, 9]
    sorted_desc = sorted(numbers, reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]
    numbers.sort()  # Modifies in place

    # List comprehensions
    squares = [x**2 for x in range(5)]    # [0, 1, 4, 9, 16]
    evens = [x for x in numbers if x % 2 == 0]  # [2, 4, 6]

    # Filtering
    greater_than_3 = list(filter(lambda x: x > 3, numbers))

    # Mapping
    doubled = list(map(lambda x: x * 2, numbers))

    # Counting
    count_ones = numbers.count(1)  # 2

    # Copying
    shallow_copy = numbers.copy()
    deep_copy = numbers[:]

    return squares, evens, doubled


def exercise_4_remove_duplicates(items: list) -> list:
    """
    Remove duplicates from a list while preserving order.

    Example:
        remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
        remove_duplicates(['a', 'b', 'a', 'c']) -> ['a', 'b', 'c']

    Hint: Use a set to track seen items, or use dict.fromkeys()
    """
    # TODO: Implement this function
    pass


def exercise_5_flatten_list(nested: list) -> list:
    """
    Flatten a nested list (one level deep only).

    Example:
        flatten_list([[1, 2], [3, 4], [5]]) -> [1, 2, 3, 4, 5]
        flatten_list([[1], [2, 3], [4, 5, 6]]) -> [1, 2, 3, 4, 5, 6]

    Hint: Use nested loop or list comprehension
    """
    # TODO: Implement this function
    pass


def exercise_6_find_common_elements(list1: list, list2: list) -> list:
    """
    Find common elements between two lists (no duplicates in result).

    Example:
        find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) -> [3, 4]
        find_common_elements(['a', 'b', 'c'], ['b', 'c', 'd']) -> ['b', 'c']

    Hint: Convert to sets and use intersection, then convert back to list
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED LIST TECHNIQUES
# ============================================================================

def exercise_7_rotate_list(items: list, k: int) -> list:
    """
    Rotate a list to the right by k positions.

    Example:
        rotate_list([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
        rotate_list(['a', 'b', 'c'], 1) -> ['c', 'a', 'b']

    Hint: Use list slicing. Handle k larger than list length with modulo
    """
    # TODO: Implement this function
    pass


def exercise_8_partition_list(numbers: list, pivot: int) -> list:
    """
    Partition a list so all elements less than pivot come before elements >= pivot.
    Preserve relative order within each partition.

    Example:
        partition_list([3, 5, 1, 4, 2], 3) -> [1, 2, 3, 5, 4]
        partition_list([7, 2, 9, 4, 5], 5) -> [2, 4, 7, 9, 5]

    Hint: Create two lists (less than and greater/equal), then combine
    """
    # TODO: Implement this function
    pass


def exercise_9_merge_sorted_lists(list1: list, list2: list) -> list:
    """
    Merge two sorted lists into one sorted list.

    Example:
        merge_sorted_lists([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
        merge_sorted_lists([1, 2, 3], [4, 5, 6]) -> [1, 2, 3, 4, 5, 6]

    Hint: Use two pointers to compare elements from both lists
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Lists:

1. DATA PROCESSING
   - Storing and processing collections of records
   - Batch processing operations
   - ETL pipelines (Extract, Transform, Load)
   Example: Processing thousands of user records from a database

2. ALGORITHM IMPLEMENTATION
   - Implementing stacks, queues, heaps
   - Graph algorithms (adjacency lists)
   - Dynamic programming solutions
   Example: Implementing Dijkstra's shortest path algorithm

3. WEB DEVELOPMENT
   - Managing collections of users, posts, comments
   - Request/response data
   - Form data processing
   Example: Storing list of products in a shopping cart

4. DATA SCIENCE
   - Feature vectors for machine learning
   - Time series data
   - Dataset management
   Example: Storing features for training ML models

5. GAME DEVELOPMENT
   - Managing game entities (players, enemies, items)
   - Event queues
   - Path finding
   Example: Tracking all active enemies in a game level

6. SYSTEM ADMINISTRATION
   - Managing file lists
   - Process monitoring
   - Log aggregation
   Example: Listing all files in a directory for backup
"""

def exercise_10_find_missing_number(numbers: list, n: int) -> int:
    """
    Given a list containing n-1 numbers from 1 to n, find the missing number.
    Common interview question!

    Example:
        find_missing_number([1, 2, 4, 5], 5) -> 3
        find_missing_number([1, 2, 3, 4, 5, 7], 7) -> 6

    Hint: Sum of 1 to n is n*(n+1)/2. Subtract sum of list from this
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("LIST LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Sum List:")
    try:
        assert exercise_1_sum_list([1, 2, 3, 4, 5]) == 15
        assert exercise_1_sum_list([10, 20, 30]) == 60
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Find Max:")
    try:
        assert exercise_2_find_max([1, 5, 3, 9, 2]) == 9
        assert exercise_2_find_max([10, 20, 15]) == 20
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Reverse List:")
    try:
        assert exercise_3_reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
        assert exercise_3_reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Remove Duplicates:")
    try:
        assert exercise_4_remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
        assert exercise_4_remove_duplicates(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. Flatten List:")
    try:
        assert exercise_5_flatten_list([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
        assert exercise_5_flatten_list([[1], [2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Find Common Elements:")
    try:
        result = exercise_6_find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
        assert set(result) == {3, 4}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Rotate List:")
    try:
        assert exercise_7_rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
        assert exercise_7_rotate_list(['a', 'b', 'c'], 1) == ['c', 'a', 'b']
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Partition List:")
    try:
        result = exercise_8_partition_list([3, 5, 1, 4, 2], 3)
        # Check that elements < 3 come before elements >= 3
        less_than = [x for x in result if x < 3]
        greater_equal = [x for x in result if x >= 3]
        assert result == less_than + greater_equal
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. Merge Sorted Lists:")
    try:
        assert exercise_9_merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
        assert exercise_9_merge_sorted_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Find Missing Number:")
    try:
        assert exercise_10_find_missing_number([1, 2, 4, 5], 5) == 3
        assert exercise_10_find_missing_number([1, 2, 3, 4, 5, 7], 7) == 6
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
