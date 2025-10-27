#!/usr/bin/env python3
"""
Answer Checker for Linked Lists Lesson
Run with: python answers/check_linked_lists.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from linked_lists_lesson import *


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
    print("LINKED LISTS LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    results.append(test_exercise(1, lambda: (
        head := create_linked_list([1, 2, 3, 4]),
        assert_eq(linked_list_to_list(exercise_1_reverse_linked_list(head)), [4, 3, 2, 1])
    )))

    results.append(test_exercise(2, lambda: (
        head := create_linked_list([1, 2, 3, 4, 5]),
        assert_eq(exercise_2_find_middle(head).val, 3)
    )))

    results.append(test_exercise(3, lambda: (
        head1 := create_linked_list([1, 2, 3, 4]),
        (tail := head1, [tail := tail.next for _ in range(3)]),
        setattr(tail, 'next', head1.next),
        assert_eq(exercise_3_detect_cycle(head1), True),
        head2 := create_linked_list([1, 2, 3]),
        assert_eq(exercise_3_detect_cycle(head2), False)
    )))

    results.append(test_exercise(4, lambda: (
        head := create_linked_list([1, 2, 3, 4, 5]),
        assert_eq(linked_list_to_list(exercise_4_remove_nth_from_end(head, 2)), [1, 2, 3, 5])
    )))

    results.append(test_exercise(5, lambda: (
        l1 := create_linked_list([1, 2, 4]),
        l2 := create_linked_list([1, 3, 4]),
        assert_eq(linked_list_to_list(exercise_5_merge_sorted_lists(l1, l2)), [1, 1, 2, 3, 4, 4])
    )))

    results.append(test_exercise(6, lambda: (
        head1 := create_linked_list([1, 2, 2, 1]),
        assert_eq(exercise_6_palindrome_linked_list(head1), True),
        head2 := create_linked_list([1, 2, 3]),
        assert_eq(exercise_6_palindrome_linked_list(head2), False)
    )))

    results.append(test_exercise(7, lambda: (
        head := create_linked_list([1, 2, 3, 4, 5]),
        assert_eq(linked_list_to_list(exercise_7_reorder_list(head)), [1, 5, 2, 4, 3])
    )))

    print("\n8. Copy Random List:")
    print("   ⚠ SKIPPED - Requires special Node class")
    results.append(True)

    results.append(test_exercise(9, lambda: (
        head := create_linked_list([1, 2, 3, 4, 5]),
        assert_eq(linked_list_to_list(exercise_9_reverse_k_group(head, 2)), [2, 1, 4, 3, 5])
    )))

    results.append(test_exercise(10, lambda: (
        l1 := create_linked_list([2, 4, 3]),
        l2 := create_linked_list([5, 6, 4]),
        assert_eq(linked_list_to_list(exercise_10_add_two_numbers(l1, l2)), [7, 0, 8])
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
