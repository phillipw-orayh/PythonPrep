#!/usr/bin/env python3
"""Command-line interface for Python Interview Prep."""

import argparse
import sys
from pathlib import Path

from utils.question_generator import QuestionGenerator
from utils.test_runner import TestRunner
from utils.progress_tracker import ProgressTracker
from config import SESSIONS_DIR


def cmd_new(args):
    """Generate a new session."""
    generator = QuestionGenerator()

    try:
        session_path = generator.generate_session(
            difficulty=args.difficulty,
            topic=args.topic
        )

        # Mark as generated
        tracker = ProgressTracker()
        session_number = int(session_path.stem.split('_')[1])
        tracker.mark_session_generated(session_number)

        print(f"\n✓ Session created: {session_path.name}")
        print(f"  Path: {session_path}")
        print("\nTo get started:")
        print(f"  1. Open {session_path}")
        print("  2. Implement your solution")
        print(f"  3. Run tests: python cli.py test {session_path.name}")
        print()

    except ValueError as e:
        print(f"\nError: {e}")
        print("Try adding questions to the question bank first.")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)


def cmd_test(args):
    """Run tests on a session."""
    runner = TestRunner()

    if args.session_file:
        # Test specific session
        session_path = SESSIONS_DIR / args.session_file
        if not session_path.exists():
            session_path = Path(args.session_file)

        if not session_path.exists():
            print(f"\nError: Session file not found: {args.session_file}")
            sys.exit(1)

        print(f"\nRunning tests for {session_path.name}...\n")
        result = runner.run_tests(session_path, verbose=True)

        print("\n" + "="*60)
        if result["success"]:
            print("✓ ALL TESTS PASSED!")
        else:
            print("✗ TESTS FAILED")

        print(f"  Passed: {result['passed']}")
        print(f"  Failed: {result['failed']}")
        print(f"  Errors: {result['errors']}")
        print(f"  Time: {result['execution_time']:.3f}s")
        print("="*60 + "\n")

        sys.exit(0 if result["success"] else 1)

    else:
        print("\nError: Please specify a session file to test.")
        print("Usage: python cli.py test <session_file>")
        sys.exit(1)


def cmd_test_all(args):
    """Run tests on all sessions."""
    runner = TestRunner()

    print("\nRunning tests on all sessions...\n")
    results = runner.run_all_tests(verbose=args.verbose)

    if not results:
        print("No session files found.")
        sys.exit(0)

    # Print summary
    summary = runner.get_summary(results)

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total Sessions: {summary['total_sessions']}")
    print(f"Successful: {summary['successful_sessions']}")
    print(f"Failed: {summary['failed_sessions']}")
    print(f"Success Rate: {summary['success_rate']:.1f}%")
    print(f"Total Tests Passed: {summary['total_tests_passed']}")
    print(f"Total Tests Failed: {summary['total_tests_failed']}")
    print(f"Total Errors: {summary['total_errors']}")
    print(f"Total Time: {summary['total_execution_time']:.3f}s")
    print("="*60 + "\n")

    sys.exit(0 if summary['failed_sessions'] == 0 else 1)


def cmd_list(args):
    """List available questions."""
    generator = QuestionGenerator()

    questions = generator.list_questions(difficulty=args.difficulty)

    if not questions:
        print("\nNo questions found in the question bank.")
        print("Add questions to the questions/ directory (easy/medium/hard).")
        sys.exit(0)

    print("\n" + "="*60)
    print("AVAILABLE QUESTIONS")
    print("="*60)

    for q in questions:
        topics_str = ", ".join(q['topics']) if q['topics'] else "None"
        print(f"\n{q['title']}")
        print(f"  Difficulty: {q['difficulty']}")
        print(f"  Topics: {topics_str}")
        print(f"  File: {q['file']}")

    print("="*60 + "\n")


def cmd_stats(args):
    """Show progress statistics."""
    tracker = ProgressTracker()

    tracker.print_stats()

    if args.recent:
        tracker.print_recent_sessions(limit=args.recent)


def cmd_log(args):
    """Log a completed session."""
    tracker = ProgressTracker()

    tracker.log_session(
        session_number=args.session_number,
        question_title=args.title,
        difficulty=args.difficulty,
        topics=args.topics.split(',') if args.topics else [],
        time_taken_minutes=args.time,
        passed=args.passed,
        notes=args.notes or ""
    )

    print(f"\n✓ Session #{args.session_number} logged successfully!")
    print("\nView stats with: python cli.py stats\n")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Python Interview Prep - Command Line Interface",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # New command
    parser_new = subparsers.add_parser('new', help='Generate a new session')
    parser_new.add_argument('--difficulty', choices=['easy', 'medium', 'hard'],
                           help='Filter by difficulty level')
    parser_new.add_argument('--topic', help='Filter by topic')
    parser_new.set_defaults(func=cmd_new)

    # Test command
    parser_test = subparsers.add_parser('test', help='Run tests on a session')
    parser_test.add_argument('session_file', nargs='?', help='Session file to test')
    parser_test.set_defaults(func=cmd_test)

    # Test-all command
    parser_test_all = subparsers.add_parser('test-all', help='Run tests on all sessions')
    parser_test_all.add_argument('-v', '--verbose', action='store_true',
                                help='Show verbose output')
    parser_test_all.set_defaults(func=cmd_test_all)

    # List command
    parser_list = subparsers.add_parser('list', help='List available questions')
    parser_list.add_argument('--difficulty', choices=['easy', 'medium', 'hard'],
                           help='Filter by difficulty level')
    parser_list.set_defaults(func=cmd_list)

    # Stats command
    parser_stats = subparsers.add_parser('stats', help='Show progress statistics')
    parser_stats.add_argument('--recent', type=int, metavar='N',
                            help='Show N most recent sessions')
    parser_stats.set_defaults(func=cmd_stats)

    # Log command
    parser_log = subparsers.add_parser('log', help='Log a completed session')
    parser_log.add_argument('session_number', type=int, help='Session number')
    parser_log.add_argument('--title', required=True, help='Question title')
    parser_log.add_argument('--difficulty', required=True,
                          choices=['easy', 'medium', 'hard'],
                          help='Difficulty level')
    parser_log.add_argument('--topics', help='Comma-separated list of topics')
    parser_log.add_argument('--time', type=int, help='Time taken in minutes')
    parser_log.add_argument('--passed', action='store_true',
                          help='Mark as passed')
    parser_log.add_argument('--notes', help='Optional notes')
    parser_log.set_defaults(func=cmd_log)

    # Parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    # Execute command
    args.func(args)


if __name__ == "__main__":
    main()
