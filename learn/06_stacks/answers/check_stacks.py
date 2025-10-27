#!/usr/bin/env python3
"""
Answer Checker for Stacks Lesson
Run with: python answers/check_stacks.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stacks_lesson import *


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
    print("STACKS LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    results.append(test_exercise(1, lambda: (
        assert_eq(exercise_1_reverse_string_with_stack("hello"), "olleh"),
        assert_eq(exercise_1_reverse_string_with_stack("Python"), "nohtyP")
    )))

    results.append(test_exercise(2, lambda: (
        assert_eq(exercise_2_balanced_parentheses("()"), True),
        assert_eq(exercise_2_balanced_parentheses("(())"), True),
        assert_eq(exercise_2_balanced_parentheses("(()"), False),
        assert_eq(exercise_2_balanced_parentheses("())"), False)
    )))

    results.append(test_exercise(3, lambda:
        assert_eq(exercise_3_stack_min([("push", 5), ("push", 3), ("min",), ("push", 7), ("min",)]), [3, 3])
    ))

    results.append(test_exercise(4, lambda: (
        assert_eq(exercise_4_evaluate_postfix("3 4 +"), 7),
        assert_eq(exercise_4_evaluate_postfix("5 1 2 + 4 * + 3 -"), 14)
    )))

    results.append(test_exercise(5, lambda: (
        assert_eq(exercise_5_next_greater_element([4, 5, 2, 10, 8]), [5, 10, 10, -1, -1]),
        assert_eq(exercise_5_next_greater_element([1, 2, 3, 4]), [2, 3, 4, -1])
    )))

    results.append(test_exercise(6, lambda: (
        assert_eq(exercise_6_valid_brackets("()[]{}"), True),
        assert_eq(exercise_6_valid_brackets("([)]"), False),
        assert_eq(exercise_6_valid_brackets("{[]}"), True)
    )))

    results.append(test_exercise(7, lambda: (
        assert_eq(exercise_7_simplify_path("/home/"), "/home"),
        assert_eq(exercise_7_simplify_path("/../"), "/"),
        assert_eq(exercise_7_simplify_path("/a/./b/../../c/"), "/c")
    )))

    results.append(test_exercise(8, lambda:
        assert_eq(exercise_8_daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
    ))

    results.append(test_exercise(9, lambda: (
        assert_eq(exercise_9_decode_string("3[a]2[bc]"), "aaabcbc"),
        assert_eq(exercise_9_decode_string("3[a2[c]]"), "accaccacc")
    )))

    results.append(test_exercise(10, lambda: (
        assert_eq(exercise_10_asteroid_collision([5, 10, -5]), [5, 10]),
        assert_eq(exercise_10_asteroid_collision([8, -8]), []),
        assert_eq(exercise_10_asteroid_collision([10, 2, -5]), [10])
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
