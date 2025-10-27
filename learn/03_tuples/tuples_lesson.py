"""
INTERACTIVE LESSON: Tuples in Python

Tuples are immutable, ordered sequences similar to lists but cannot be changed after creation.
They are used when you need a collection that shouldn't be modified.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_tuples.py
"""

# ============================================================================
# PART 1: WHAT ARE TUPLES?
# ============================================================================
"""
Tuples are ordered, immutable collections.
- Created with parentheses: (1, 2, 3)
- Can also create without parentheses: 1, 2, 3
- Immutable: cannot change, add, or remove elements after creation
- Indexed: access elements by position (0-based)
- Can contain mixed types: (1, "hello", 3.14)
- Often used for function return values and fixed collections
"""

# ============================================================================
# PART 2: BASIC TUPLE OPERATIONS
# ============================================================================

def tuple_basics_demo():
    """Demonstrates basic tuple operations."""
    # Creating tuples
    numbers = (1, 2, 3, 4, 5)
    mixed = (1, "hello", 3.14, True)
    single = (42,)  # Note the comma! (42) is just 42, not a tuple
    empty = ()
    no_parens = 1, 2, 3  # Also creates a tuple

    # Accessing elements
    first = numbers[0]      # 1
    last = numbers[-1]      # 5
    slice_result = numbers[1:4]  # (2, 3, 4)

    # Tuple unpacking
    x, y, z = (1, 2, 3)  # x=1, y=2, z=3
    a, *rest, b = (1, 2, 3, 4, 5)  # a=1, rest=[2,3,4], b=5

    # Operations (that don't modify)
    length = len(numbers)
    contains = 3 in numbers
    index = numbers.index(3)
    count = (1, 2, 2, 3).count(2)  # 2

    # Concatenation (creates new tuple)
    combined = numbers + (6, 7)  # (1, 2, 3, 4, 5, 6, 7)
    repeated = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)

    return numbers, combined


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_tuple_to_list(t: tuple) -> list:
    """
    Convert a tuple to a list.

    Example:
        tuple_to_list((1, 2, 3)) -> [1, 2, 3]
        tuple_to_list(('a', 'b', 'c')) -> ['a', 'b', 'c']

    Hint: Use list() constructor
    """
    # TODO: Implement this function
    pass


def exercise_2_swap_elements(a, b):
    """
    Swap two values and return as a tuple.

    Example:
        swap_elements(1, 2) -> (2, 1)
        swap_elements('hello', 'world') -> ('world', 'hello')

    Hint: Return a tuple with swapped order
    """
    # TODO: Implement this function
    pass


def exercise_3_find_min_max(numbers: tuple) -> tuple:
    """
    Find both minimum and maximum values in a tuple of numbers.
    Return as a tuple: (min, max)

    Example:
        find_min_max((3, 1, 4, 1, 5, 9, 2)) -> (1, 9)
        find_min_max((10, 5, 20, 15)) -> (5, 20)

    Hint: Use min() and max() functions
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE TUPLE OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced tuple usage."""
    # Named tuples (from collections module)
    from collections import namedtuple

    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print(f"Point: x={p.x}, y={p.y}")  # Access by name

    # Tuples as dictionary keys (lists can't be keys!)
    locations = {
        (0, 0): "origin",
        (1, 0): "east",
        (0, 1): "north"
    }

    # Multiple return values
    def get_stats(numbers):
        return min(numbers), max(numbers), sum(numbers)

    min_val, max_val, total = get_stats([1, 2, 3, 4, 5])

    # Tuple comprehension (actually creates a generator)
    squares_gen = (x**2 for x in range(5))
    squares_tuple = tuple(squares_gen)  # Convert to tuple

    return Point, locations


def exercise_4_count_occurrences(t: tuple, value) -> int:
    """
    Count how many times a value appears in a tuple.

    Example:
        count_occurrences((1, 2, 2, 3, 2, 4), 2) -> 3
        count_occurrences(('a', 'b', 'a', 'c'), 'a') -> 2

    Hint: Use the .count() method
    """
    # TODO: Implement this function
    pass


def exercise_5_merge_tuples(*tuples: tuple) -> tuple:
    """
    Merge multiple tuples into one.

    Example:
        merge_tuples((1, 2), (3, 4), (5, 6)) -> (1, 2, 3, 4, 5, 6)
        merge_tuples(('a',), ('b',), ('c',)) -> ('a', 'b', 'c')

    Hint: Use sum() with an empty tuple, or concatenate with +
    """
    # TODO: Implement this function
    pass


def exercise_6_tuple_intersection(t1: tuple, t2: tuple) -> tuple:
    """
    Find common elements between two tuples (preserve order from t1, no duplicates).

    Example:
        tuple_intersection((1, 2, 3, 4), (3, 4, 5, 6)) -> (3, 4)
        tuple_intersection(('a', 'b', 'c'), ('b', 'c', 'd')) -> ('b', 'c')

    Hint: Convert to sets for intersection, then filter t1 to preserve order
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED TUPLE TECHNIQUES
# ============================================================================

def exercise_7_nested_tuple_access(nested: tuple, indices: tuple) -> any:
    """
    Access an element in a nested tuple using a tuple of indices.

    Example:
        nested_tuple_access(((1, 2), (3, 4), (5, 6)), (1, 0)) -> 3
        # First index 1 gives (3, 4), second index 0 gives 3

    Hint: Loop through indices and access each level
    """
    # TODO: Implement this function
    pass


def exercise_8_flatten_tuple(nested: tuple) -> tuple:
    """
    Flatten a nested tuple (one level deep).

    Example:
        flatten_tuple(((1, 2), (3, 4), (5,))) -> (1, 2, 3, 4, 5)
        flatten_tuple((('a',), ('b', 'c'), ('d',))) -> ('a', 'b', 'c', 'd')

    Hint: Use tuple comprehension or sum with empty tuple
    """
    # TODO: Implement this function
    pass


def exercise_9_create_coordinate_map(points: list) -> dict:
    """
    Create a dictionary mapping tuples (x, y coordinates) to their index.

    Example:
        create_coordinate_map([(1, 2), (3, 4), (5, 6)]) ->
        {(1, 2): 0, (3, 4): 1, (5, 6): 2}

    Hint: Use enumerate() and dict comprehension
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Tuples:

1. DATABASE RECORDS
   - Representing fixed-structure database rows
   - Query results (each row as a tuple)
   - Immutable data guarantees
   Example: [(1, 'Alice', 30), (2, 'Bob', 25)] for user records

2. COORDINATES AND POINTS
   - 2D/3D coordinate systems
   - Geographic locations (latitude, longitude)
   - Graph nodes
   Example: Storing (x, y) positions in games or maps

3. FUNCTION RETURN VALUES
   - Returning multiple values from functions
   - Unpacking results
   - Error handling (value, error_code)
   Example: return (result, success, message)

4. DICTIONARY KEYS
   - Multi-dimensional keys
   - Composite keys
   - Immutable requirements
   Example: Cache keys like (user_id, resource_type, timestamp)

5. DATA INTEGRITY
   - Constants and configuration
   - Immutable collections
   - Preventing accidental modifications
   Example: COLOR_PALETTE = ((255, 0, 0), (0, 255, 0), (0, 0, 255))

6. NETWORK PROGRAMMING
   - IP addresses and ports
   - Socket addresses
   - Connection endpoints
   Example: server_address = ('localhost', 8000)
"""

def exercise_10_parse_csv_row(row: str) -> tuple:
    """
    Parse a CSV row string into a tuple of values.
    Common in data processing!

    Example:
        parse_csv_row("John,Doe,30,USA") -> ('John', 'Doe', '30', 'USA')
        parse_csv_row("apple,red,5") -> ('apple', 'red', '5')

    Hint: Use .split(',') and convert to tuple
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("TUPLE LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Tuple to List:")
    try:
        assert exercise_1_tuple_to_list((1, 2, 3)) == [1, 2, 3]
        assert exercise_1_tuple_to_list(('a', 'b', 'c')) == ['a', 'b', 'c']
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Swap Elements:")
    try:
        assert exercise_2_swap_elements(1, 2) == (2, 1)
        assert exercise_2_swap_elements('hello', 'world') == ('world', 'hello')
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Find Min Max:")
    try:
        assert exercise_3_find_min_max((3, 1, 4, 1, 5, 9, 2)) == (1, 9)
        assert exercise_3_find_min_max((10, 5, 20, 15)) == (5, 20)
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Count Occurrences:")
    try:
        assert exercise_4_count_occurrences((1, 2, 2, 3, 2, 4), 2) == 3
        assert exercise_4_count_occurrences(('a', 'b', 'a', 'c'), 'a') == 2
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. Merge Tuples:")
    try:
        assert exercise_5_merge_tuples((1, 2), (3, 4), (5, 6)) == (1, 2, 3, 4, 5, 6)
        assert exercise_5_merge_tuples(('a',), ('b',), ('c',)) == ('a', 'b', 'c')
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Tuple Intersection:")
    try:
        assert exercise_6_tuple_intersection((1, 2, 3, 4), (3, 4, 5, 6)) == (3, 4)
        assert exercise_6_tuple_intersection(('a', 'b', 'c'), ('b', 'c', 'd')) == ('b', 'c')
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Nested Tuple Access:")
    try:
        assert exercise_7_nested_tuple_access(((1, 2), (3, 4), (5, 6)), (1, 0)) == 3
        print("   ✓ PASSED")
    except (AssertionError, TypeError, IndexError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Flatten Tuple:")
    try:
        assert exercise_8_flatten_tuple(((1, 2), (3, 4), (5,))) == (1, 2, 3, 4, 5)
        assert exercise_8_flatten_tuple((('a',), ('b', 'c'), ('d',))) == ('a', 'b', 'c', 'd')
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. Create Coordinate Map:")
    try:
        result = exercise_9_create_coordinate_map([(1, 2), (3, 4), (5, 6)])
        assert result == {(1, 2): 0, (3, 4): 1, (5, 6): 2}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Parse CSV Row:")
    try:
        assert exercise_10_parse_csv_row("John,Doe,30,USA") == ('John', 'Doe', '30', 'USA')
        assert exercise_10_parse_csv_row("apple,red,5") == ('apple', 'red', '5')
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
