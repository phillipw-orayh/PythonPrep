"""
INTERACTIVE LESSON: Dictionaries in Python

Dictionaries are unordered collections of key-value pairs, providing fast O(1) lookups.
They are one of Python's most powerful and frequently used data structures.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_dictionaries.py
"""

# ============================================================================
# PART 1: WHAT ARE DICTIONARIES?
# ============================================================================
"""
Dictionaries (dicts) store key-value pairs for fast lookups.
- Created with curly braces: {"key": "value"}
- Keys must be immutable (strings, numbers, tuples)
- Values can be any type
- Unordered (Python 3.7+ preserves insertion order)
- Mutable: can add, modify, or remove key-value pairs
- O(1) average time for lookups, insertions, deletions
"""

# ============================================================================
# PART 2: BASIC DICTIONARY OPERATIONS
# ============================================================================

def dict_basics_demo():
    """Demonstrates basic dictionary operations."""
    # Creating dictionaries
    person = {"name": "Alice", "age": 30, "city": "NYC"}
    empty = {}
    from_pairs = dict([("a", 1), ("b", 2)])  # From list of tuples

    # Accessing values
    name = person["name"]  # "Alice"
    age = person.get("age")  # 30
    default = person.get("country", "USA")  # "USA" (default)

    # Modifying
    person["age"] = 31  # Update existing
    person["email"] = "alice@example.com"  # Add new

    # Removing
    removed = person.pop("city")  # Remove and return "NYC"
    del person["email"]  # Delete without returning

    # Checking
    has_name = "name" in person  # True
    has_phone = "phone" in person  # False

    # Getting all keys, values, items
    keys = person.keys()  # dict_keys(['name', 'age'])
    values = person.values()  # dict_values(['Alice', 31])
    items = person.items()  # dict_items([('name', 'Alice'), ('age', 31)])

    return person


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_count_characters(s: str) -> dict:
    """
    Count the frequency of each character in a string.

    Example:
        count_characters("hello") -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        count_characters("aabbcc") -> {'a': 2, 'b': 2, 'c': 2}

    Hint: Loop through string, use dict.get() or defaultdict
    """
    # TODO: Implement this function
    pass


def exercise_2_invert_dict(d: dict) -> dict:
    """
    Swap keys and values in a dictionary.

    Example:
        invert_dict({"a": 1, "b": 2, "c": 3}) -> {1: "a", 2: "b", 3: "c"}
        invert_dict({"name": "Alice", "age": 30}) -> {"Alice": "name", 30: "age"}

    Hint: Use dict comprehension {v: k for k, v in d.items()}
    """
    # TODO: Implement this function
    pass


def exercise_3_merge_dicts(d1: dict, d2: dict) -> dict:
    """
    Merge two dictionaries. If keys overlap, d2 values take precedence.

    Example:
        merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) -> {"a": 1, "b": 3, "c": 4}

    Hint: Use {**d1, **d2} or d1.copy() then d1.update(d2)
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE DICTIONARY OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced dictionary operations."""
    # Dictionary comprehension
    squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

    # Filtering
    evens = {k: v for k, v in squares.items() if v % 2 == 0}

    # Nested dictionaries
    users = {
        "user1": {"name": "Alice", "age": 30},
        "user2": {"name": "Bob", "age": 25}
    }

    # DefaultDict (from collections)
    from collections import defaultdict
    counts = defaultdict(int)
    for char in "hello":
        counts[char] += 1

    # Counter (from collections)
    from collections import Counter
    word_counts = Counter("hello world".split())

    # setdefault
    d = {}
    d.setdefault("key", []).append(1)  # Creates list if key doesn't exist

    return squares, users, dict(counts)


def exercise_4_group_by_length(words: list) -> dict:
    """
    Group words by their length.

    Example:
        group_by_length(["a", "bb", "ccc", "dd"]) ->
        {1: ["a"], 2: ["bb", "dd"], 3: ["ccc"]}

    Hint: Use defaultdict(list) or setdefault
    """
    # TODO: Implement this function
    pass


def exercise_5_get_nested_value(d: dict, keys: list) -> any:
    """
    Get a value from a nested dictionary using a list of keys.

    Example:
        get_nested_value({"a": {"b": {"c": 42}}}, ["a", "b", "c"]) -> 42
        get_nested_value({"x": {"y": 10}}, ["x", "y"]) -> 10

    Hint: Loop through keys, accessing each level. Return None if key missing
    """
    # TODO: Implement this function
    pass


def exercise_6_find_duplicates(items: list) -> dict:
    """
    Find all duplicate values and their counts (only include if count > 1).

    Example:
        find_duplicates([1, 2, 2, 3, 3, 3, 4]) -> {2: 2, 3: 3}
        find_duplicates(['a', 'b', 'a', 'c', 'a']) -> {'a': 3}

    Hint: Count all items, then filter where count > 1
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED DICTIONARY TECHNIQUES
# ============================================================================

def exercise_7_dict_diff(d1: dict, d2: dict) -> dict:
    """
    Find keys that have different values in two dictionaries.
    Return dict with keys and (value_from_d1, value_from_d2).

    Example:
        dict_diff({"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 5, "c": 3}) ->
        {"b": (2, 5)}

    Hint: Loop through keys present in both, compare values
    """
    # TODO: Implement this function
    pass


def exercise_8_flatten_nested_dict(d: dict, sep: str = ".") -> dict:
    """
    Flatten a nested dictionary using separator for nested keys.

    Example:
        flatten_nested_dict({"a": {"b": 1, "c": 2}, "d": 3}) ->
        {"a.b": 1, "a.c": 2, "d": 3}

    Hint: Use recursion, build keys with separator
    """
    # TODO: Implement this function
    pass


def exercise_9_most_common_value(d: dict) -> any:
    """
    Find the most common value in a dictionary.

    Example:
        most_common_value({"a": 1, "b": 2, "c": 1, "d": 1}) -> 1
        most_common_value({"x": "apple", "y": "banana", "z": "apple"}) -> "apple"

    Hint: Count values using Counter or manual counting
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Dictionaries:

1. CACHING AND MEMOIZATION
   - Store computed results for fast retrieval
   - LRU cache implementations
   - Database query caching
   Example: Caching API responses by endpoint URL

2. CONFIGURATION MANAGEMENT
   - Application settings
   - Feature flags
   - Environment variables
   Example: config = {"debug": True, "max_connections": 100}

3. DATA INDEXING
   - Building indexes for fast lookups
   - Hash tables for O(1) access
   - Inverted indexes for search engines
   Example: user_index = {user_id: user_object}

4. JSON AND API RESPONSES
   - Parsing JSON data
   - Building API responses
   - Data serialization
   Example: {"status": "success", "data": {...}, "error": None}

5. COUNTING AND AGGREGATION
   - Word frequency analysis
   - Event tracking
   - Analytics and metrics
   Example: Counting page views per URL

6. GRAPH REPRESENTATIONS
   - Adjacency lists for graphs
   - Node relationships
   - Network analysis
   Example: graph = {node: [neighbors]} for social networks
"""

def exercise_10_build_index(records: list, key: str) -> dict:
    """
    Build an index from a list of dictionaries using specified key.
    Common in database-like operations!

    Example:
        records = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
        build_index(records, "id") ->
        {1: {"id": 1, "name": "Alice"}, 2: {"id": 2, "name": "Bob"}}

    Hint: Loop through records, use record[key] as index key
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("DICTIONARY LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Count Characters:")
    try:
        assert exercise_1_count_characters("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        assert exercise_1_count_characters("aabbcc") == {'a': 2, 'b': 2, 'c': 2}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Invert Dict:")
    try:
        assert exercise_2_invert_dict({"a": 1, "b": 2, "c": 3}) == {1: "a", 2: "b", 3: "c"}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Merge Dicts:")
    try:
        assert exercise_3_merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Group By Length:")
    try:
        result = exercise_4_group_by_length(["a", "bb", "ccc", "dd"])
        assert result == {1: ["a"], 2: ["bb", "dd"], 3: ["ccc"]}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. Get Nested Value:")
    try:
        assert exercise_5_get_nested_value({"a": {"b": {"c": 42}}}, ["a", "b", "c"]) == 42
        assert exercise_5_get_nested_value({"x": {"y": 10}}, ["x", "y"]) == 10
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Find Duplicates:")
    try:
        assert exercise_6_find_duplicates([1, 2, 2, 3, 3, 3, 4]) == {2: 2, 3: 3}
        assert exercise_6_find_duplicates(['a', 'b', 'a', 'c', 'a']) == {'a': 3}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Dict Diff:")
    try:
        result = exercise_7_dict_diff({"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 5, "c": 3})
        assert result == {"b": (2, 5)}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Flatten Nested Dict:")
    try:
        result = exercise_8_flatten_nested_dict({"a": {"b": 1, "c": 2}, "d": 3})
        assert result == {"a.b": 1, "a.c": 2, "d": 3}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. Most Common Value:")
    try:
        assert exercise_9_most_common_value({"a": 1, "b": 2, "c": 1, "d": 1}) == 1
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Build Index:")
    try:
        records = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        result = exercise_10_build_index(records, "id")
        assert result == {1: {"id": 1, "name": "Alice"}, 2: {"id": 2, "name": "Bob"}}
        print("   ✓ PASSED")
    except (AssertionError, TypeError, KeyError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
