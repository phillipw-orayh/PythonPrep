"""Test runner for validating interview solutions."""

import sys
import subprocess
import time
from pathlib import Path
from typing import Optional, Dict, Any, List

from config import SESSIONS_DIR


class TestRunner:
    """Runs tests on session files and reports results."""

    def __init__(self):
        """Initialize the test runner."""
        self.sessions_dir = SESSIONS_DIR

    def run_tests(self, session_file: Path, verbose: bool = True) -> Dict[str, Any]:
        """
        Run tests on a specific session file.

        Args:
            session_file: Path to the session file
            verbose: Whether to print verbose output

        Returns:
            Dictionary with test results:
                - success: bool
                - passed: int (number of tests passed)
                - failed: int (number of tests failed)
                - errors: int (number of errors)
                - execution_time: float (seconds)
                - output: str (test output)
                - error_message: Optional[str]
        """
        if not session_file.exists():
            return {
                "success": False,
                "passed": 0,
                "failed": 0,
                "errors": 1,
                "execution_time": 0.0,
                "output": "",
                "error_message": f"Session file not found: {session_file}"
            }

        # Run unittest on the session file
        start_time = time.time()

        try:
            result = subprocess.run(
                [sys.executable, "-m", "unittest", str(session_file)],
                capture_output=True,
                text=True,
                timeout=30  # 30 second timeout
            )

            execution_time = time.time() - start_time

            # Parse unittest output
            output = result.stdout + result.stderr
            success = result.returncode == 0

            # Try to extract test counts from output
            passed, failed, errors = self._parse_test_counts(output)

            if verbose:
                print(output)

            return {
                "success": success,
                "passed": passed,
                "failed": failed,
                "errors": errors,
                "execution_time": execution_time,
                "output": output,
                "error_message": None if success else "Tests failed or had errors"
            }

        except subprocess.TimeoutExpired:
            execution_time = time.time() - start_time
            error_msg = "Test execution timed out (>30 seconds)"
            if verbose:
                print(f"ERROR: {error_msg}")
            return {
                "success": False,
                "passed": 0,
                "failed": 0,
                "errors": 1,
                "execution_time": execution_time,
                "output": "",
                "error_message": error_msg
            }

        except Exception as e:
            execution_time = time.time() - start_time
            error_msg = f"Error running tests: {str(e)}"
            if verbose:
                print(f"ERROR: {error_msg}")
            return {
                "success": False,
                "passed": 0,
                "failed": 0,
                "errors": 1,
                "execution_time": execution_time,
                "output": "",
                "error_message": error_msg
            }

    def _parse_test_counts(self, output: str) -> tuple[int, int, int]:
        """
        Parse test counts from unittest output.

        Args:
            output: Test output string

        Returns:
            Tuple of (passed, failed, errors)
        """
        import re

        passed = 0
        failed = 0
        errors = 0

        # Look for patterns like "Ran 5 tests in 0.001s"
        run_match = re.search(r'Ran (\d+) test', output)
        if run_match:
            total_tests = int(run_match.group(1))

            # Look for failures and errors
            # Pattern: "FAILED (failures=2, errors=1)"
            failed_match = re.search(r'failures=(\d+)', output)
            errors_match = re.search(r'errors=(\d+)', output)

            if failed_match:
                failed = int(failed_match.group(1))
            if errors_match:
                errors = int(errors_match.group(1))

            # Calculate passed tests
            passed = total_tests - failed - errors
        else:
            # If we can't parse, check if it says OK
            if "OK" in output:
                # Try to get test count
                ok_match = re.search(r'Ran (\d+)', output)
                if ok_match:
                    passed = int(ok_match.group(1))

        return passed, failed, errors

    def run_all_tests(self, verbose: bool = True) -> List[Dict[str, Any]]:
        """
        Run tests on all session files.

        Args:
            verbose: Whether to print verbose output

        Returns:
            List of test results for each session
        """
        session_files = sorted(self.sessions_dir.glob("session_*.py"))

        if not session_files:
            if verbose:
                print("No session files found.")
            return []

        results = []
        for session_file in session_files:
            if verbose:
                print(f"\n{'='*60}")
                print(f"Running tests for: {session_file.name}")
                print('='*60)

            result = self.run_tests(session_file, verbose=verbose)
            result["session_file"] = session_file.name
            results.append(result)

            if verbose:
                status = "✓ PASSED" if result["success"] else "✗ FAILED"
                print(f"\n{status} - {result['passed']} passed, "
                      f"{result['failed']} failed, {result['errors']} errors "
                      f"({result['execution_time']:.3f}s)")

        return results

    def get_summary(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate summary statistics from test results.

        Args:
            results: List of test results

        Returns:
            Dictionary with summary statistics
        """
        total_sessions = len(results)
        successful_sessions = sum(1 for r in results if r["success"])
        total_passed = sum(r["passed"] for r in results)
        total_failed = sum(r["failed"] for r in results)
        total_errors = sum(r["errors"] for r in results)
        total_time = sum(r["execution_time"] for r in results)

        return {
            "total_sessions": total_sessions,
            "successful_sessions": successful_sessions,
            "failed_sessions": total_sessions - successful_sessions,
            "total_tests_passed": total_passed,
            "total_tests_failed": total_failed,
            "total_errors": total_errors,
            "total_execution_time": total_time,
            "success_rate": (successful_sessions / total_sessions * 100) if total_sessions > 0 else 0
        }
