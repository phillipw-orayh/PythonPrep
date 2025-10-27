#!/usr/bin/env python3
"""
Answer Checker for Lists Lesson

This script verifies all exercise implementations in the lists lesson.
Run with: python answers/check_lists.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lists_lesson import (
    exercise_1_sum_list,
    exercise_2_find_max,
    exercise_3_reverse_list,
    exercise_4_remove_duplicates,
    exercise_5_flatten_list,
    exercise_6_find_common_elements,
    exercise_7_rotate_list,
    exercise_8_partition_list,
    exercise_9_merge_sorted_lists,
    exercise_10_find_missing_number
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
    """Check all list exercises."""
    print("="*70)
    print("LISTS LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    # Exercise 1
    def test_1():
        assert exercise_1_sum_list([1, 2, 3, 4, 5]) == 15
        assert exercise_1_sum_list([10, 20, 30]) == 60
        assert exercise_1_sum_list([]) == 0
    results.append(test_exercise(1, test_1))

    # Exercise 2
    def test_2():
        assert exercise_2_find_max([1, 5, 3, 9, 2]) == 9
        assert exercise_2_find_max([10, 20, 15]) == 20
    results.append(test_exercise(2, test_2))

    # Exercise 3
    def test_3():
        assert exercise_3_reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
        assert exercise_3_reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    results.append(test_exercise(3, test_3))

    # Exercise 4
    def test_4():
        assert exercise_4_remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
        assert exercise_4_remove_duplicates(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']
    results.append(test_exercise(4, test_4))

    # Exercise 5
    def test_5():
        assert exercise_5_flatten_list([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
        assert exercise_5_flatten_list([[1], [2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]
    results.append(test_exercise(5, test_5))

    # Exercise 6
    def test_6():
        result = exercise_6_find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
        assert set(result) == {3, 4}
    results.append(test_exercise(6, test_6))

    # Exercise 7
    def test_7():
        assert exercise_7_rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
        assert exercise_7_rotate_list(['a', 'b', 'c'], 1) == ['c', 'a', 'b']
    results.append(test_exercise(7, test_7))

    # Exercise 8
    def test_8():
        result = exercise_8_partition_list([3, 5, 1, 4, 2], 3)
        less_than = [x for x in result if x < 3]
        greater_equal = [x for x in result if x >= 3]
        assert result == less_than + greater_equal
    results.append(test_exercise(8, test_8))

    # Exercise 9
    def test_9():
        assert exercise_9_merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
        assert exercise_9_merge_sorted_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    results.append(test_exercise(9, test_9))

    # Exercise 10
    def test_10():
        assert exercise_10_find_missing_number([1, 2, 4, 5], 5) == 3
        assert exercise_10_find_missing_number([1, 2, 3, 4, 5, 7], 7) == 6
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
