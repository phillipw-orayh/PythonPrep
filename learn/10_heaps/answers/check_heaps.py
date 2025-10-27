#!/usr/bin/env python3
"""
Answer Checker for Heaps Lesson
Run with: python answers/check_heaps.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from heaps_lesson import (
    exercise_1_find_kth_smallest,
    exercise_2_find_k_largest,
    exercise_3_merge_k_sorted_lists,
    exercise_4_heap_sort,
    exercise_5_find_median,
    exercise_6_top_k_frequent,
    exercise_7_running_median,
    exercise_8_connect_ropes,
    exercise_9_k_closest_points,
    exercise_10_task_scheduler
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
    """Check all heap exercises."""
    print("="*70)
    print("HEAPS LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    # Exercise 1
    def test_1():
        assert exercise_1_find_kth_smallest([7, 10, 4, 3, 20, 15], 3) == 7
        assert exercise_1_find_kth_smallest([1, 5, 2, 8, 3], 2) == 2
    results.append(test_exercise(1, test_1))

    # Exercise 2
    def test_2():
        result = exercise_2_find_k_largest([1, 5, 2, 8, 3], 2)
        assert set(result) == {8, 5}
    results.append(test_exercise(2, test_2))

    # Exercise 3
    def test_3():
        result = exercise_3_merge_k_sorted_lists([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    results.append(test_exercise(3, test_3))

    # Exercise 4
    def test_4():
        assert exercise_4_heap_sort([3, 1, 4, 1, 5, 9, 2]) == [1, 1, 2, 3, 4, 5, 9]
    results.append(test_exercise(4, test_4))

    # Exercise 5
    def test_5():
        assert exercise_5_find_median([1, 3, 5]) == 3
        assert exercise_5_find_median([1, 2, 3, 4]) == 2.5
    results.append(test_exercise(5, test_5))

    # Exercise 6
    def test_6():
        result = exercise_6_top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        assert set(result) == {1, 2}
    results.append(test_exercise(6, test_6))

    # Exercise 7
    def test_7():
        result = exercise_7_running_median([1, 2, 3, 4])
        assert result == [1, 1.5, 2, 2.5]
    results.append(test_exercise(7, test_7))

    # Exercise 8
    def test_8():
        assert exercise_8_connect_ropes([4, 3, 2, 6]) == 29
    results.append(test_exercise(8, test_8))

    # Exercise 9
    def test_9():
        result = exercise_9_k_closest_points([(1, 1), (3, 3), (2, 2)], 2)
        assert len(result) == 2
        assert (1, 1) in result
    results.append(test_exercise(9, test_9))

    # Exercise 10
    def test_10():
        result = exercise_10_task_scheduler(['A', 'A', 'A', 'B', 'B', 'B'], 2)
        assert result == 8
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
