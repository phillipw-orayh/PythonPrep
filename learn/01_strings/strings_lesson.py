"""
INTERACTIVE LESSON: Strings in Python

Strings are immutable sequences of characters used to store and manipulate text.
They are one of the most fundamental data structures in Python.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_strings.py
"""

# ============================================================================
# PART 1: WHAT ARE STRINGS?
# ============================================================================
"""
Strings are sequences of Unicode characters enclosed in quotes.
- Created with single quotes: 'hello'
- Created with double quotes: "hello"
- Created with triple quotes for multiline: '''hello'''
- Immutable: cannot change characters in place
- Indexed: can access individual characters by position (0-based)
"""

# ============================================================================
# PART 2: BASIC STRING OPERATIONS
# ============================================================================

def string_basics_demo():
    """Demonstrates basic string operations."""
    # Creating strings
    s1 = "Hello"
    s2 = 'World'
    s3 = """Multi
    line
    string"""

    # Concatenation
    combined = s1 + " " + s2  # "Hello World"

    # Repetition
    repeated = "Ha" * 3  # "HaHaHa"

    # Length
    length = len(s1)  # 5

    # Indexing
    first_char = s1[0]    # 'H'
    last_char = s1[-1]    # 'o'

    # Slicing
    substring = s1[1:4]   # 'ell'

    return combined, repeated, length, first_char, last_char, substring


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_reverse_string(s: str) -> str:
    """
    Reverse a string.

    Example:
        reverse_string("hello") -> "olleh"
        reverse_string("Python") -> "nohtyP"

    Hint: Use string slicing with [::-1]
    """
    # TODO: Implement this function
    pass


def exercise_2_count_vowels(s: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in a string (case-insensitive).

    Example:
        count_vowels("hello") -> 2
        count_vowels("Python") -> 1

    Hint: Loop through the string and check if each character is in "aeiouAEIOU"
    """
    # TODO: Implement this function
    pass


def exercise_3_is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    Ignore case and spaces.

    Example:
        is_palindrome("racecar") -> True
        is_palindrome("hello") -> False
        is_palindrome("A man a plan a canal Panama") -> True

    Hint: Remove spaces, convert to lowercase, then compare with its reverse
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE STRING OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced string methods."""
    s = "  Hello, World!  "

    # Case conversion
    upper = s.upper()        # "  HELLO, WORLD!  "
    lower = s.lower()        # "  hello, world!  "
    title = s.title()        # "  Hello, World!  "

    # Stripping whitespace
    stripped = s.strip()     # "Hello, World!"
    left = s.lstrip()        # "Hello, World!  "
    right = s.rstrip()       # "  Hello, World!"

    # Splitting and joining
    words = s.strip().split(", ")  # ["Hello", "World!"]
    joined = "-".join(words)        # "Hello-World!"

    # Searching
    index = s.find("World")    # 9 (position of "World")
    count = s.count("l")       # 3

    # Checking
    starts = s.strip().startswith("Hello")  # True
    ends = s.strip().endswith("!")          # True
    is_alpha = "Hello".isalpha()            # True
    is_digit = "123".isdigit()              # True

    return upper, lower, stripped, words, joined


def exercise_4_title_case(s: str) -> str:
    """
    Convert a string to title case (first letter of each word capitalized).

    Example:
        title_case("hello world") -> "Hello World"
        title_case("python programming") -> "Python Programming"

    Hint: Use the .title() method or split(), capitalize each word, and join()
    """
    # TODO: Implement this function
    pass


def exercise_5_remove_duplicates(s: str) -> str:
    """
    Remove duplicate characters from a string, keeping first occurrence.

    Example:
        remove_duplicates("hello") -> "helo"
        remove_duplicates("aabbcc") -> "abc"

    Hint: Loop through string, keep track of seen characters
    """
    # TODO: Implement this function
    pass


def exercise_6_word_frequency(s: str) -> dict:
    """
    Count the frequency of each word in a string (case-insensitive).

    Example:
        word_frequency("hello world hello") -> {"hello": 2, "world": 1}

    Hint: Convert to lowercase, split into words, use a dictionary to count
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED STRING TECHNIQUES
# ============================================================================

def exercise_7_compress_string(s: str) -> str:
    """
    Compress a string using run-length encoding.
    If compressed string is not shorter, return original.

    Example:
        compress_string("aabcccccaaa") -> "a2b1c5a3"
        compress_string("abc") -> "abc"

    Hint: Count consecutive characters and build result string
    """
    # TODO: Implement this function
    pass


def exercise_8_anagram_check(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams (same letters, different order).
    Ignore case and spaces.

    Example:
        anagram_check("listen", "silent") -> True
        anagram_check("hello", "world") -> False

    Hint: Sort the characters of both strings and compare
    """
    # TODO: Implement this function
    pass


def exercise_9_longest_unique_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.

    Example:
        longest_unique_substring("abcabcbb") -> 3  # "abc"
        longest_unique_substring("bbbbb") -> 1     # "b"
        longest_unique_substring("pwwkew") -> 3    # "wke"

    Hint: Use sliding window technique with a set to track seen characters
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Strings:

1. WEB DEVELOPMENT
   - URL parsing and manipulation
   - HTML/XML processing
   - Input validation and sanitization
   Example: Cleaning user input before storing in database

2. DATA PROCESSING
   - CSV/TSV file parsing
   - Log file analysis
   - Text cleaning and normalization
   Example: Processing log files to extract error messages

3. NATURAL LANGUAGE PROCESSING
   - Tokenization (splitting text into words)
   - Text preprocessing (lowercasing, removing punctuation)
   - Pattern matching with regex
   Example: Analyzing customer reviews for sentiment

4. API DEVELOPMENT
   - JSON string parsing and generation
   - Request/response formatting
   - Authentication tokens
   Example: Parsing JSON API responses

5. SECURITY
   - Password validation
   - Input sanitization to prevent SQL injection
   - Hash generation
   Example: Validating password strength requirements

6. DATA SCIENCE
   - Feature extraction from text
   - String encoding for machine learning
   - Text preprocessing pipelines
   Example: Converting text to numerical features
"""

def exercise_10_validate_email(email: str) -> bool:
    """
    Validate if a string is a properly formatted email address.
    Basic validation: contains @ and . after @, no spaces.

    Example:
        validate_email("user@example.com") -> True
        validate_email("invalid.email") -> False
        validate_email("user @example.com") -> False

    Hint: Check for @ symbol, split by @, validate parts
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("STRING LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Reverse String:")
    try:
        assert exercise_1_reverse_string("hello") == "olleh"
        assert exercise_1_reverse_string("Python") == "nohtyP"
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Count Vowels:")
    try:
        assert exercise_2_count_vowels("hello") == 2
        assert exercise_2_count_vowels("Python") == 1
        assert exercise_2_count_vowels("aeiou") == 5
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Is Palindrome:")
    try:
        assert exercise_3_is_palindrome("racecar") == True
        assert exercise_3_is_palindrome("hello") == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Title Case:")
    try:
        assert exercise_4_title_case("hello world") == "Hello World"
        assert exercise_4_title_case("python programming") == "Python Programming"
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. Remove Duplicates:")
    try:
        assert exercise_5_remove_duplicates("hello") == "helo"
        assert exercise_5_remove_duplicates("aabbcc") == "abc"
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Word Frequency:")
    try:
        result = exercise_6_word_frequency("hello world hello")
        assert result == {"hello": 2, "world": 1}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Compress String:")
    try:
        assert exercise_7_compress_string("aabcccccaaa") == "a2b1c5a3"
        assert exercise_7_compress_string("abc") == "abc"
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Anagram Check:")
    try:
        assert exercise_8_anagram_check("listen", "silent") == True
        assert exercise_8_anagram_check("hello", "world") == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. Longest Unique Substring:")
    try:
        assert exercise_9_longest_unique_substring("abcabcbb") == 3
        assert exercise_9_longest_unique_substring("bbbbb") == 1
        assert exercise_9_longest_unique_substring("pwwkew") == 3
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Validate Email:")
    try:
        assert exercise_10_validate_email("user@example.com") == True
        assert exercise_10_validate_email("invalid.email") == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
