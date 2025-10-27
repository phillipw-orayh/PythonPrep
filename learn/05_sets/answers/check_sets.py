#!/usr/bin/env python3
"""
Answer Checker for Sets Lesson
Run with: python answers/check_sets.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sets_lesson import (
    exercise_1_remove_duplicates,
    exercise_2_common_elements,
    exercise_3_unique_elements,
    exercise_4_is_subset,
    exercise_5_all_unique,
    exercise_6_power_set,
    exercise_7_find_unique_words,
    exercise_8_missing_numbers,
    exercise_9_jaccard_similarity,
    exercise_10_find_duplicates_across_lists
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
    """Check all set exercises."""
    print("="*70)
    print("SETS LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    # Exercise 1
    def test_1():
        result = exercise_1_remove_duplicates([1, 2, 2, 3, 1, 4])
        assert set(result) == {1, 2, 3, 4}
    results.append(test_exercise(1, test_1))

    # Exercise 2
    def test_2():
        assert exercise_2_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == {3, 4}
        assert exercise_2_common_elements(['a', 'b', 'c'], ['b', 'c', 'd']) == {'b', 'c'}
    results.append(test_exercise(2, test_2))

    # Exercise 3
    def test_3():
        assert exercise_3_unique_elements([1, 2, 3], [2, 3, 4]) == {1, 4}
        assert exercise_3_unique_elements(['a', 'b'], ['b', 'c']) == {'a', 'c'}
    results.append(test_exercise(3, test_3))

    # Exercise 4
    def test_4():
        assert exercise_4_is_subset({1, 2}, {1, 2, 3, 4}) == True
        assert exercise_4_is_subset({1, 5}, {1, 2, 3, 4}) == False
    results.append(test_exercise(4, test_4))

    # Exercise 5
    def test_5():
        assert exercise_5_all_unique([1, 2, 3, 4]) == True
        assert exercise_5_all_unique([1, 2, 2, 3]) == False
    results.append(test_exercise(5, test_5))

    # Exercise 6
    def test_6():
        result = exercise_6_power_set({1, 2})
        expected = [frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})]
        assert set(result) == set(expected)
    results.append(test_exercise(6, test_6))

    # Exercise 7
    def test_7():
        result = exercise_7_find_unique_words("Hello world! Hello Python.")
        assert result == {'hello', 'world', 'python'}
    results.append(test_exercise(7, test_7))

    # Exercise 8
    def test_8():
        assert exercise_8_missing_numbers([1, 2, 4, 6], 6) == {3, 5}
        assert exercise_8_missing_numbers([1, 3, 5], 5) == {2, 4}
    results.append(test_exercise(8, test_8))

    # Exercise 9
    def test_9():
        assert abs(exercise_9_jaccard_similarity({1, 2, 3}, {2, 3, 4}) - 0.5) < 0.01
    results.append(test_exercise(9, test_9))

    # Exercise 10
    def test_10():
        result = exercise_10_find_duplicates_across_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
        assert 2 in result and 3 in result and 4 in result
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
