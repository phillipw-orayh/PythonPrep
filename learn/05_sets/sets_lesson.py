"""
INTERACTIVE LESSON: Sets in Python

Sets are unordered collections of unique elements with fast membership testing.
They are perfect for removing duplicates and mathematical set operations.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_sets.py
"""

# ============================================================================
# PART 1: WHAT ARE SETS?
# ============================================================================
"""
Sets are unordered collections of unique elements.
- Created with curly braces: {1, 2, 3}
- No duplicate values allowed
- Unordered: no indexing or slicing
- Mutable: can add or remove elements
- Elements must be immutable (hashable)
- O(1) average time for membership testing
- Support mathematical set operations (union, intersection, etc.)
"""

# ============================================================================
# PART 2: BASIC SET OPERATIONS
# ============================================================================

def set_basics_demo():
    """Demonstrates basic set operations."""
    # Creating sets
    numbers = {1, 2, 3, 4, 5}
    from_list = set([1, 2, 2, 3, 3])  # {1, 2, 3} - duplicates removed
    empty = set()  # Note: {} creates empty dict, not set!

    # Adding elements
    numbers.add(6)  # {1, 2, 3, 4, 5, 6}
    numbers.update([7, 8, 9])  # Add multiple

    # Removing elements
    numbers.remove(6)  # Raises KeyError if not found
    numbers.discard(10)  # No error if not found
    popped = numbers.pop()  # Remove and return arbitrary element

    # Membership testing (fast!)
    has_three = 3 in numbers  # True
    has_ten = 10 in numbers  # False

    # Set operations
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    union = a | b  # {1, 2, 3, 4, 5, 6}
    intersection = a & b  # {3, 4}
    difference = a - b  # {1, 2}
    symmetric_diff = a ^ b  # {1, 2, 5, 6}

    # Subset and superset
    is_subset = {1, 2}.issubset(a)  # True
    is_superset = a.issuperset({1, 2})  # True

    return numbers, union, intersection


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_remove_duplicates(items: list) -> list:
    """
    Remove duplicates from a list (order doesn't matter).

    Example:
        remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4] (any order)
        remove_duplicates(['a', 'b', 'a', 'c']) -> ['a', 'b', 'c'] (any order)

    Hint: Convert to set, then back to list
    """
    # TODO: Implement this function
    pass


def exercise_2_common_elements(list1: list, list2: list) -> set:
    """
    Find common elements between two lists.

    Example:
        common_elements([1, 2, 3, 4], [3, 4, 5, 6]) -> {3, 4}
        common_elements(['a', 'b', 'c'], ['b', 'c', 'd']) -> {'b', 'c'}

    Hint: Convert to sets and use & operator
    """
    # TODO: Implement this function
    pass


def exercise_3_unique_elements(list1: list, list2: list) -> set:
    """
    Find elements that are in either list but not both (symmetric difference).

    Example:
        unique_elements([1, 2, 3], [2, 3, 4]) -> {1, 4}
        unique_elements(['a', 'b'], ['b', 'c']) -> {'a', 'c'}

    Hint: Convert to sets and use ^ operator
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE SET OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced set operations."""
    # Set comprehension
    squares = {x**2 for x in range(10)}  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

    # Frozen sets (immutable sets)
    fs = frozenset([1, 2, 3])  # Can be used as dict keys or in other sets

    # Multiple set operations
    a = {1, 2, 3}
    b = {2, 3, 4}
    c = {3, 4, 5}

    # Union of multiple sets
    all_together = a | b | c  # {1, 2, 3, 4, 5}

    # Intersection of multiple sets
    common_to_all = a & b & c  # {3}

    # Disjoint (no common elements)
    are_disjoint = a.isdisjoint({10, 11, 12})  # True

    return squares, all_together


def exercise_4_is_subset(set1: set, set2: set) -> bool:
    """
    Check if set1 is a subset of set2 (all elements of set1 are in set2).

    Example:
        is_subset({1, 2}, {1, 2, 3, 4}) -> True
        is_subset({1, 5}, {1, 2, 3, 4}) -> False

    Hint: Use <= operator or .issubset() method
    """
    # TODO: Implement this function
    pass


def exercise_5_all_unique(items: list) -> bool:
    """
    Check if all elements in a list are unique.

    Example:
        all_unique([1, 2, 3, 4]) -> True
        all_unique([1, 2, 2, 3]) -> False

    Hint: Compare length of list with length of set
    """
    # TODO: Implement this function
    pass


def exercise_6_power_set(s: set) -> list:
    """
    Generate the power set (all subsets) of a set.
    Return as list of frozensets.

    Example:
        power_set({1, 2}) ->
        [frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})]

    Hint: Use itertools.combinations for each size from 0 to len(s)
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED SET TECHNIQUES
# ============================================================================

def exercise_7_find_unique_words(text: str) -> set:
    """
    Find all unique words in a text (case-insensitive, ignore punctuation).

    Example:
        find_unique_words("Hello world! Hello Python.") ->
        {'hello', 'world', 'python'}

    Hint: Convert to lowercase, remove punctuation, split, convert to set
    """
    # TODO: Implement this function
    pass


def exercise_8_missing_numbers(numbers: list, n: int) -> set:
    """
    Find all missing numbers in a range from 1 to n.

    Example:
        missing_numbers([1, 2, 4, 6], 6) -> {3, 5}
        missing_numbers([1, 3, 5], 5) -> {2, 4}

    Hint: Create set of range(1, n+1) and subtract set of numbers
    """
    # TODO: Implement this function
    pass


def exercise_9_jaccard_similarity(set1: set, set2: set) -> float:
    """
    Calculate Jaccard similarity coefficient between two sets.
    Formula: |intersection| / |union|

    Example:
        jaccard_similarity({1, 2, 3}, {2, 3, 4}) -> 0.5
        # intersection = {2, 3}, union = {1, 2, 3, 4}
        # similarity = 2/4 = 0.5

    Hint: Use set operations, handle empty case
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Sets:

1. DATA DEDUPLICATION
   - Removing duplicate records
   - Unique user tracking
   - Event deduplication
   Example: unique_visitors = set([user_id for visit in visits])

2. MEMBERSHIP TESTING
   - Checking if user has permission
   - Validating against whitelist/blacklist
   - Fast lookups in large collections
   Example: if user_id in banned_users: block_access()

3. RECOMMENDATION SYSTEMS
   - Finding common interests
   - Collaborative filtering
   - Content similarity
   Example: common_interests = user1_interests & user2_interests

4. DATA ANALYSIS
   - Finding unique values
   - Set operations on data
   - Venn diagram calculations
   Example: Finding customers who bought A but not B

5. GRAPH ALGORITHMS
   - Visited node tracking
   - Finding connected components
   - Cycle detection
   Example: visited = set() for BFS/DFS traversal

6. TEXT PROCESSING
   - Unique word extraction
   - Stop word removal
   - Vocabulary building
   Example: vocabulary = set(word for doc in docs for word in doc)
"""

def exercise_10_find_duplicates_across_lists(lists: list) -> set:
    """
    Find elements that appear in more than one list.
    Common in data reconciliation!

    Example:
        find_duplicates_across_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) -> {2, 3, 4}
        # 2 appears in lists 0 and 1
        # 3 appears in all lists
        # 4 appears in lists 1 and 2

    Hint: Check each unique element to see if it appears in multiple lists
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("SET LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Remove Duplicates:")
    try:
        result = exercise_1_remove_duplicates([1, 2, 2, 3, 1, 4])
        assert set(result) == {1, 2, 3, 4}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Common Elements:")
    try:
        assert exercise_2_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == {3, 4}
        assert exercise_2_common_elements(['a', 'b', 'c'], ['b', 'c', 'd']) == {'b', 'c'}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Unique Elements:")
    try:
        assert exercise_3_unique_elements([1, 2, 3], [2, 3, 4]) == {1, 4}
        assert exercise_3_unique_elements(['a', 'b'], ['b', 'c']) == {'a', 'c'}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Is Subset:")
    try:
        assert exercise_4_is_subset({1, 2}, {1, 2, 3, 4}) == True
        assert exercise_4_is_subset({1, 5}, {1, 2, 3, 4}) == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. All Unique:")
    try:
        assert exercise_5_all_unique([1, 2, 3, 4]) == True
        assert exercise_5_all_unique([1, 2, 2, 3]) == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Power Set:")
    try:
        result = exercise_6_power_set({1, 2})
        expected = [frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})]
        assert set(result) == set(expected)
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Find Unique Words:")
    try:
        result = exercise_7_find_unique_words("Hello world! Hello Python.")
        assert result == {'hello', 'world', 'python'}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Missing Numbers:")
    try:
        assert exercise_8_missing_numbers([1, 2, 4, 6], 6) == {3, 5}
        assert exercise_8_missing_numbers([1, 3, 5], 5) == {2, 4}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. Jaccard Similarity:")
    try:
        assert abs(exercise_9_jaccard_similarity({1, 2, 3}, {2, 3, 4}) - 0.5) < 0.01
        print("   ✓ PASSED")
    except (AssertionError, TypeError, ZeroDivisionError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Find Duplicates Across Lists:")
    try:
        result = exercise_10_find_duplicates_across_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
        # Elements in multiple lists: 2 (in 2 lists), 3 (in 3 lists), 4 (in 2 lists)
        assert 2 in result and 3 in result and 4 in result
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
