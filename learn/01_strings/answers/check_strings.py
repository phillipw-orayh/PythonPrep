#!/usr/bin/env python3
"""
Answer Checker for Strings Lesson

This script verifies all exercise implementations in the strings lesson.
Run with: python answers/check_strings.py
"""

import sys
import os

# Add parent directory to path to import lesson
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strings_lesson import (
    exercise_1_reverse_string,
    exercise_2_count_vowels,
    exercise_3_is_palindrome,
    exercise_4_title_case,
    exercise_5_remove_duplicates,
    exercise_6_word_frequency,
    exercise_7_compress_string,
    exercise_8_anagram_check,
    exercise_9_longest_unique_substring,
    exercise_10_validate_email
)


def test_exercise(exercise_num, test_func):
    """Helper to run a test and report results."""
    try:
        test_func()
        print(f"   ✓ Exercise {exercise_num} PASSED")
        return True
    except AssertionError as e:
        print(f"   ✗ Exercise {exercise_num} FAILED: {str(e)}")
        return False
    except Exception as e:
        print(f"   ✗ Exercise {exercise_num} ERROR: {str(e)}")
        return False


def check_all():
    """Check all string exercises."""
    print("="*70)
    print("STRINGS LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    # Exercise 1
    def test_1():
        assert exercise_1_reverse_string("hello") == "olleh", "Failed basic reverse"
        assert exercise_1_reverse_string("Python") == "nohtyP", "Failed Python reverse"
        assert exercise_1_reverse_string("") == "", "Failed empty string"
    results.append(test_exercise(1, test_1))

    # Exercise 2
    def test_2():
        assert exercise_2_count_vowels("hello") == 2, "Failed hello count"
        assert exercise_2_count_vowels("Python") == 1, "Failed Python count"
        assert exercise_2_count_vowels("aeiou") == 5, "Failed aeiou count"
        assert exercise_2_count_vowels("xyz") == 0, "Failed no vowels"
    results.append(test_exercise(2, test_2))

    # Exercise 3
    def test_3():
        assert exercise_3_is_palindrome("racecar") == True, "Failed racecar"
        assert exercise_3_is_palindrome("hello") == False, "Failed hello"
        assert exercise_3_is_palindrome("A man a plan a canal Panama") == True, "Failed phrase"
    results.append(test_exercise(3, test_3))

    # Exercise 4
    def test_4():
        assert exercise_4_title_case("hello world") == "Hello World"
        assert exercise_4_title_case("python programming") == "Python Programming"
    results.append(test_exercise(4, test_4))

    # Exercise 5
    def test_5():
        assert exercise_5_remove_duplicates("hello") == "helo"
        assert exercise_5_remove_duplicates("aabbcc") == "abc"
    results.append(test_exercise(5, test_5))

    # Exercise 6
    def test_6():
        result = exercise_6_word_frequency("hello world hello")
        assert result == {"hello": 2, "world": 1}
    results.append(test_exercise(6, test_6))

    # Exercise 7
    def test_7():
        assert exercise_7_compress_string("aabcccccaaa") == "a2b1c5a3"
        assert exercise_7_compress_string("abc") == "abc"
    results.append(test_exercise(7, test_7))

    # Exercise 8
    def test_8():
        assert exercise_8_anagram_check("listen", "silent") == True
        assert exercise_8_anagram_check("hello", "world") == False
    results.append(test_exercise(8, test_8))

    # Exercise 9
    def test_9():
        assert exercise_9_longest_unique_substring("abcabcbb") == 3
        assert exercise_9_longest_unique_substring("bbbbb") == 1
        assert exercise_9_longest_unique_substring("pwwkew") == 3
    results.append(test_exercise(9, test_9))

    # Exercise 10
    def test_10():
        assert exercise_10_validate_email("user@example.com") == True
        assert exercise_10_validate_email("invalid.email") == False
        assert exercise_10_validate_email("user @example.com") == False
    results.append(test_exercise(10, test_10))

    # Summary
    passed = sum(results)
    total = len(results)
    print("\n" + "="*70)
    print(f"RESULTS: {passed}/{total} exercises passed")
    if passed == total:
        print("🎉 CONGRATULATIONS! All exercises completed correctly!")
    else:
        print(f"Keep going! {total - passed} exercise(s) remaining.")
    print("="*70)

    return passed == total


if __name__ == "__main__":
    success = check_all()
    sys.exit(0 if success else 1)
