#!/usr/bin/env python3
"""
Answer Checker for Deques Lesson
Run with: python answers/check_deques.py
"""

import sys
import os
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deques_lesson import *


def test_exercise(num, test_func):
    try:
        test_func()
        print(f"   ✓ Exercise {num} PASSED")
        return True
    except AssertionError as e:
        print(f"   ✗ Exercise {num} FAILED: {str(e)}")
        return False
    except Exception as e:
        print(f"   ✗ Exercise {num} ERROR: {str(e)}")
        return False


def check_all():
    print("="*70)
    print("DEQUES LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    results.append(test_exercise(1, lambda: (
        assert_eq(exercise_1_palindrome_check("racecar"), True),
        assert_eq(exercise_1_palindrome_check("hello"), False)
    )))

    results.append(test_exercise(2, lambda:
        assert_eq(list(exercise_2_reverse_first_k(deque([1, 2, 3, 4, 5]), 3)), [3, 2, 1, 4, 5])
    ))

    results.append(test_exercise(3, lambda:
        assert_eq(exercise_3_max_sliding_window_deque([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
    ))

    results.append(test_exercise(4, lambda:
        assert_eq(exercise_4_min_window_deque([1, 3, -1, -3, 5, 3], 3), [1, -1, -3, -3])
    ))

    results.append(test_exercise(5, lambda:
        assert_eq(exercise_5_first_negative_in_window([12, -1, -7, 8, -15, 30, 16, 28], 3), [-1, -1, -7, -15, -15, 0])
    ))

    results.append(test_exercise(6, lambda:
        assert_eq(exercise_6_rotate_array_deque([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
    ))

    results.append(test_exercise(7, lambda: (
        assert_eq(exercise_7_jump_game_reachable([2, 3, 1, 1, 4]), True),
        assert_eq(exercise_7_jump_game_reachable([3, 2, 1, 0, 4]), False)
    )))

    results.append(test_exercise(8, lambda:
        assert_eq(exercise_8_constrained_subsequence_sum([10, 2, -10, 5, 20], 2), 37)
    ))

    results.append(test_exercise(9, lambda: (
        assert_eq(exercise_9_shortest_subarray_sum([2, -1, 2], 3), 3),
        assert_eq(exercise_9_shortest_subarray_sum([1, 2], 4), -1)
    )))

    results.append(test_exercise(10, lambda:
        assert_eq(exercise_10_gas_station_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
    ))

    passed = sum(results)
    total = len(results)
    print(f"\n{'='*70}")
    print(f"RESULTS: {passed}/{total} exercises passed")
    print("="*70)
    return passed == total


def assert_eq(actual, expected):
    assert actual == expected, f"Expected {expected}, got {actual}"


if __name__ == "__main__":
    sys.exit(0 if check_all() else 1)
