#!/usr/bin/env python3
"""
Answer Checker for Trees Lesson
Run with: python answers/check_trees.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from trees_lesson import *


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
    print("TREES LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    results.append(test_exercise(1, lambda: (
        root := create_tree([3, 9, 20, None, None, 15, 7]),
        assert_eq(exercise_1_max_depth(root), 3)
    )))

    results.append(test_exercise(2, lambda: (
        root := create_tree([4, 2, 7, 1, 3, 6, 9]),
        result := exercise_2_invert_tree(root),
        assert_eq(result.left.val, 7),
        assert_eq(result.right.val, 2)
    )))

    results.append(test_exercise(3, lambda: (
        p := create_tree([1, 2, 3]),
        q := create_tree([1, 2, 3]),
        assert_eq(exercise_3_same_tree(p, q), True),
        p2 := create_tree([1, 2]),
        q2 := create_tree([1, None, 2]),
        assert_eq(exercise_3_same_tree(p2, q2), False)
    )))

    results.append(test_exercise(4, lambda: (
        root := create_tree([3, 9, 20, None, None, 15, 7]),
        assert_eq(exercise_4_level_order_traversal(root), [[3], [9, 20], [15, 7]])
    )))

    results.append(test_exercise(5, lambda: (
        root1 := create_tree([2, 1, 3]),
        assert_eq(exercise_5_is_valid_bst(root1), True),
        root2 := create_tree([5, 1, 4, None, None, 3, 6]),
        assert_eq(exercise_5_is_valid_bst(root2), False)
    )))

    results.append(test_exercise(6, lambda: (
        root := create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),
        assert_eq(exercise_6_path_sum(root, 22), True),
        assert_eq(exercise_6_path_sum(root, 100), False)
    )))

    results.append(test_exercise(7, lambda: (
        root := create_tree([3, 5, 1, 6, 2, 0, 8]),
        p := root.left,
        q := root.left.right,
        result := exercise_7_lowest_common_ancestor(root, p, q),
        assert_eq(result.val, 5)
    )))

    results.append(test_exercise(8, lambda: (
        root := create_tree([1, 2, 3, None, None, 4, 5]),
        serialized := exercise_8_serialize_deserialize(root),
        assert_eq(isinstance(serialized, str) and len(serialized) > 0, True)
    )))

    results.append(test_exercise(9, lambda: (
        root := create_tree([-10, 9, 20, None, None, 15, 7]),
        assert_eq(exercise_9_max_path_sum(root), 42)
    )))

    results.append(test_exercise(10, lambda: (
        root := create_tree([0, 0, None, 0, 0]),
        assert_eq(exercise_10_binary_tree_cameras(root), 1)
    )))

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
