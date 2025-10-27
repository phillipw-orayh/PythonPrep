#!/usr/bin/env python3
"""
Answer Checker for Tries Lesson
Run with: python answers/check_tries.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tries_lesson import *


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
    print("TRIES LESSON - ANSWER CHECKER")
    print("="*70)

    results = []

    results.append(test_exercise(1, lambda: (
        trie := exercise_1_implement_trie_class(),
        assert_eq(trie.search("apple"), True),
        assert_eq(trie.search("app"), True),
        assert_eq(trie.starts_with("ban"), True)
    )))

    results.append(test_exercise(2, lambda: (
        assert_eq(exercise_2_longest_common_prefix(["flower","flow","flight"]), "fl"),
        assert_eq(exercise_2_longest_common_prefix(["dog","racecar","car"]), "")
    )))

    results.append(test_exercise(3, lambda: (
        board := [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],
        assert_eq(exercise_3_word_search_board(board, "ABCCED"), True),
        assert_eq(exercise_3_word_search_board(board, "ABCB"), False)
    )))

    results.append(test_exercise(4, lambda: (
        assert_eq(exercise_4_add_search_word_wildcards(["bad","dad","mad"], ".ad"), True),
        assert_eq(exercise_4_add_search_word_wildcards(["bad","dad","mad"], "pad"), False)
    )))

    results.append(test_exercise(5, lambda: (
        assert_eq(exercise_5_word_break("leetcode", ["leet", "code"]), True),
        assert_eq(exercise_5_word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)
    )))

    results.append(test_exercise(6, lambda:
        assert_eq(exercise_6_replace_words(["cat", "bat", "rat"],
                                           "the cattle was rattled by the battery"),
                  "the cat was rat by the bat")
    ))

    results.append(test_exercise(7, lambda: (
        board := [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']],
        result := exercise_7_word_search_ii(board, ["oath","pea","eat","rain"]),
        assert_eq(set(result), {"oath", "eat"})
    )))

    results.append(test_exercise(8, lambda:
        assert_eq(exercise_8_stream_checker(["cd","f","kl"], ['a','b','c','d','e','f']),
                  [False,False,False,True,False,True])
    ))

    results.append(test_exercise(9, lambda: (
        result := exercise_9_palindrome_pairs(["bat","tab","cat"]),
        assert_eq([0,1] in result and [1,0] in result, True)
    )))

    results.append(test_exercise(10, lambda: (
        sentences := ["i love you", "island", "iroman", "i love leetcode"],
        times := [5, 3, 2, 2],
        result := exercise_10_design_search_autocomplete(sentences, times, "i"),
        assert_eq(len(result) <= 3, True),
        assert_eq("i love you" in result, True)
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
