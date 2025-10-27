#!/usr/bin/env python3
"""
Answer Checker for Tuples Lesson
Run with: python answers/check_tuples.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tuples_lesson import (
    exercise_1_tuple_to_list,
    exercise_2_swap_elements,
    exercise_3_find_min_max,
    exercise_4_count_occurrences,
    exercise_5_merge_tuples,
    exercise_6_tuple_intersection,
    exercise_7_nested_tuple_access,
    exercise_8_flatten_tuple,
    exercise_9_create_coordinate_map,
    exercise_10_parse_csv_row
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
    """Check all tuple exercises."""
    print("="*70)
    print("TUPLES LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    # Exercise 1
    def test_1():
        assert exercise_1_tuple_to_list((1, 2, 3)) == [1, 2, 3]
        assert exercise_1_tuple_to_list(('a', 'b', 'c')) == ['a', 'b', 'c']
    results.append(test_exercise(1, test_1))

    # Exercise 2
    def test_2():
        assert exercise_2_swap_elements(1, 2) == (2, 1)
        assert exercise_2_swap_elements('hello', 'world') == ('world', 'hello')
    results.append(test_exercise(2, test_2))

    # Exercise 3
    def test_3():
        assert exercise_3_find_min_max((3, 1, 4, 1, 5, 9, 2)) == (1, 9)
        assert exercise_3_find_min_max((10, 5, 20, 15)) == (5, 20)
    results.append(test_exercise(3, test_3))

    # Exercise 4
    def test_4():
        assert exercise_4_count_occurrences((1, 2, 2, 3, 2, 4), 2) == 3
        assert exercise_4_count_occurrences(('a', 'b', 'a', 'c'), 'a') == 2
    results.append(test_exercise(4, test_4))

    # Exercise 5
    def test_5():
        assert exercise_5_merge_tuples((1, 2), (3, 4), (5, 6)) == (1, 2, 3, 4, 5, 6)
        assert exercise_5_merge_tuples(('a',), ('b',), ('c',)) == ('a', 'b', 'c')
    results.append(test_exercise(5, test_5))

    # Exercise 6
    def test_6():
        assert exercise_6_tuple_intersection((1, 2, 3, 4), (3, 4, 5, 6)) == (3, 4)
        assert exercise_6_tuple_intersection(('a', 'b', 'c'), ('b', 'c', 'd')) == ('b', 'c')
    results.append(test_exercise(6, test_6))

    # Exercise 7
    def test_7():
        assert exercise_7_nested_tuple_access(((1, 2), (3, 4), (5, 6)), (1, 0)) == 3
    results.append(test_exercise(7, test_7))

    # Exercise 8
    def test_8():
        assert exercise_8_flatten_tuple(((1, 2), (3, 4), (5,))) == (1, 2, 3, 4, 5)
        assert exercise_8_flatten_tuple((('a',), ('b', 'c'), ('d',))) == ('a', 'b', 'c', 'd')
    results.append(test_exercise(8, test_8))

    # Exercise 9
    def test_9():
        result = exercise_9_create_coordinate_map([(1, 2), (3, 4), (5, 6)])
        assert result == {(1, 2): 0, (3, 4): 1, (5, 6): 2}
    results.append(test_exercise(9, test_9))

    # Exercise 10
    def test_10():
        assert exercise_10_parse_csv_row("John,Doe,30,USA") == ('John', 'Doe', '30', 'USA')
        assert exercise_10_parse_csv_row("apple,red,5") == ('apple', 'red', '5')
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
