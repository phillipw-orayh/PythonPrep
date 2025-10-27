#!/usr/bin/env python3
"""
Master Answer Checker for All Data Structure Lessons

This script runs all answer checkers for all data structure lessons.
Run with: python learn/check_all_lessons.py
"""

import subprocess
import sys
from pathlib import Path

# List of all lesson directories
LESSONS = [
    "01_strings",
    "02_lists",
    "03_tuples",
    "04_dictionaries",
    "05_sets",
    "06_stacks",
    "07_queues",
    "08_deques",
    "09_linked_lists",
    "10_heaps",
    "11_trees",
    "12_graphs",
    "13_tries"
]


def check_lesson(lesson_name):
    """Run the answer checker for a specific lesson."""
    lesson_path = Path(__file__).parent / lesson_name
    checker_path = lesson_path / "answers" / f"check_{lesson_name.split('_', 1)[1]}.py"

    if not checker_path.exists():
        return None, f"Checker not found: {checker_path}"

    try:
        result = subprocess.run(
            [sys.executable, str(checker_path)],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(lesson_path)
        )

        return result.returncode == 0, result.stdout + result.stderr

    except subprocess.TimeoutExpired:
        return False, "Checker timed out (>30 seconds)"
    except Exception as e:
        return False, f"Error running checker: {str(e)}"


def main():
    """Run all lesson checkers."""
    print("="*80)
    print("RUNNING ALL DATA STRUCTURE LESSON CHECKERS")
    print("="*80)

    results = {}
    for lesson in LESSONS:
        print(f"\n{'='*80}")
        print(f"CHECKING: {lesson.upper()}")
        print('='*80)

        success, output = check_lesson(lesson)

        if success is None:
            print(f"⚠ SKIPPED - {output}")
            results[lesson] = "skipped"
        elif success:
            print(output)
            print(f"\n✓ {lesson} - ALL TESTS PASSED")
            results[lesson] = "passed"
        else:
            print(output)
            print(f"\n✗ {lesson} - SOME TESTS FAILED")
            results[lesson] = "failed"

    # Print summary
    print("\n" + "="*80)
    print("SUMMARY OF ALL LESSONS")
    print("="*80)

    passed = sum(1 for r in results.values() if r == "passed")
    failed = sum(1 for r in results.values() if r == "failed")
    skipped = sum(1 for r in results.values() if r == "skipped")

    for lesson, result in results.items():
        if result == "passed":
            symbol = "✓"
        elif result == "failed":
            symbol = "✗"
        else:
            symbol = "⚠"

        print(f"  {symbol} {lesson}: {result.upper()}")

    print(f"\nTotal: {len(LESSONS)} lessons")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Skipped: {skipped}")

    print("="*80)

    if passed == len(LESSONS):
        print("🎉 CONGRATULATIONS! You've mastered all data structures!")
        return 0
    elif failed == 0 and skipped > 0:
        print(f"👍 All implemented lessons passed! {skipped} lesson(s) not yet created.")
        return 0
    else:
        print(f"💪 Keep going! {failed + skipped} lesson(s) need attention.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
