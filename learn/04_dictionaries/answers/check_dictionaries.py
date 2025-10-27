#!/usr/bin/env python3
"""
Answer Checker for Dictionaries Lesson
Run with: python answers/check_dictionaries.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dictionaries_lesson import (
    exercise_1_count_characters,
    exercise_2_invert_dict,
    exercise_3_merge_dicts,
    exercise_4_group_by_length,
    exercise_5_get_nested_value,
    exercise_6_find_duplicates,
    exercise_7_dict_diff,
    exercise_8_flatten_nested_dict,
    exercise_9_most_common_value,
    exercise_10_build_index
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
    """Check all dictionary exercises."""
    print("="*70)
    print("DICTIONARIES LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    # Exercise 1
    def test_1():
        assert exercise_1_count_characters("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        assert exercise_1_count_characters("aabbcc") == {'a': 2, 'b': 2, 'c': 2}
    results.append(test_exercise(1, test_1))

    # Exercise 2
    def test_2():
        assert exercise_2_invert_dict({"a": 1, "b": 2, "c": 3}) == {1: "a", 2: "b", 3: "c"}
    results.append(test_exercise(2, test_2))

    # Exercise 3
    def test_3():
        assert exercise_3_merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}
    results.append(test_exercise(3, test_3))

    # Exercise 4
    def test_4():
        result = exercise_4_group_by_length(["a", "bb", "ccc", "dd"])
        assert result == {1: ["a"], 2: ["bb", "dd"], 3: ["ccc"]}
    results.append(test_exercise(4, test_4))

    # Exercise 5
    def test_5():
        assert exercise_5_get_nested_value({"a": {"b": {"c": 42}}}, ["a", "b", "c"]) == 42
        assert exercise_5_get_nested_value({"x": {"y": 10}}, ["x", "y"]) == 10
    results.append(test_exercise(5, test_5))

    # Exercise 6
    def test_6():
        assert exercise_6_find_duplicates([1, 2, 2, 3, 3, 3, 4]) == {2: 2, 3: 3}
        assert exercise_6_find_duplicates(['a', 'b', 'a', 'c', 'a']) == {'a': 3}
    results.append(test_exercise(6, test_6))

    # Exercise 7
    def test_7():
        result = exercise_7_dict_diff({"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 5, "c": 3})
        assert result == {"b": (2, 5)}
    results.append(test_exercise(7, test_7))

    # Exercise 8
    def test_8():
        result = exercise_8_flatten_nested_dict({"a": {"b": 1, "c": 2}, "d": 3})
        assert result == {"a.b": 1, "a.c": 2, "d": 3}
    results.append(test_exercise(8, test_8))

    # Exercise 9
    def test_9():
        assert exercise_9_most_common_value({"a": 1, "b": 2, "c": 1, "d": 1}) == 1
    results.append(test_exercise(9, test_9))

    # Exercise 10
    def test_10():
        records = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        result = exercise_10_build_index(records, "id")
        assert result == {1: {"id": 1, "name": "Alice"}, 2: {"id": 2, "name": "Bob"}}
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
