#!/usr/bin/env python3
"""
Answer Checker for Queues Lesson
Run with: python answers/check_queues.py
"""

import sys
import os
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from queues_lesson import *


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
    print("QUEUES LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    results.append(test_exercise(1, lambda:
        assert_eq(list(exercise_1_reverse_queue(deque([1, 2, 3, 4]))), [4, 3, 2, 1])
    ))

    results.append(test_exercise(2, lambda: (
        assert_eq(exercise_2_first_unique_character("leetcode"), 0),
        assert_eq(exercise_2_first_unique_character("loveleetcode"), 2),
        assert_eq(exercise_2_first_unique_character("aabb"), -1)
    )))

    results.append(test_exercise(3, lambda:
        assert_eq(exercise_3_queue_using_stacks([("enqueue", 1), ("enqueue", 2), ("dequeue",)]), [1])
    ))

    results.append(test_exercise(4, lambda:
        assert_eq(exercise_4_sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
    ))

    results.append(test_exercise(5, lambda: (
        check_floats_close(exercise_5_moving_average([1, 10, 3, 5], 3), [1.0, 5.5, 4.666, 6.0])
    )))

    results.append(test_exercise(6, lambda:
        assert_eq(exercise_6_recent_counter([1, 100, 3001, 3002], 3000), [1, 2, 3, 3])
    ))

    results.append(test_exercise(7, lambda:
        assert_eq(exercise_7_shortest_path_bfs([[0, 0, 0], [1, 1, 0], [0, 0, 0]], (0, 0), (2, 2)), 4)
    ))

    results.append(test_exercise(8, lambda: (
        assert_eq(exercise_8_perfect_squares(12), 3),
        assert_eq(exercise_8_perfect_squares(13), 2)
    )))

    results.append(test_exercise(9, lambda:
        assert_eq(exercise_9_rotting_oranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)
    ))

    results.append(test_exercise(10, lambda:
        assert_eq(exercise_10_design_circular_queue([("enqueue", 1), ("enqueue", 2), ("dequeue",), ("enqueue", 3), ("front",)], 3), [1, 3])
    ))

    passed = sum(results)
    total = len(results)
    print(f"\n{'='*70}")
    print(f"RESULTS: {passed}/{total} exercises passed")
    print("="*70)
    return passed == total


def assert_eq(actual, expected):
    assert actual == expected, f"Expected {expected}, got {actual}"


def check_floats_close(actual, expected, tol=0.01):
    for a, e in zip(actual, expected):
        assert abs(a - e) < tol, f"Expected {expected}, got {actual}"


if __name__ == "__main__":
    sys.exit(0 if check_all() else 1)
