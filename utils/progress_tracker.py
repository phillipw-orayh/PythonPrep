"""Progress tracker for logging and analyzing session history."""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
from collections import defaultdict

from config import SOLVED_LOG_FILE, STATS_FILE


class ProgressTracker:
    """Tracks session progress and generates analytics."""

    def __init__(self):
        """Initialize the progress tracker."""
        self.solved_log_file = SOLVED_LOG_FILE
        self.stats_file = STATS_FILE

    def log_session(
        self,
        session_number: int,
        question_title: str,
        difficulty: str,
        topics: List[str],
        time_taken_minutes: Optional[int] = None,
        passed: bool = False,
        notes: str = ""
    ) -> None:
        """
        Log a completed session with results.

        Args:
            session_number: Session number
            question_title: Title of the question
            difficulty: Difficulty level (easy, medium, hard)
            topics: List of topics/tags
            time_taken_minutes: Time taken to solve (in minutes)
            passed: Whether all tests passed
            notes: Optional notes or reflections
        """
        # Load existing log
        if self.solved_log_file.exists():
            with open(self.solved_log_file, 'r') as f:
                log_data = json.load(f)
        else:
            log_data = {"sessions": [], "last_session_number": 0}

        # Find existing session or create new entry
        session_entry = None
        for session in log_data["sessions"]:
            if session["session_number"] == session_number:
                session_entry = session
                break

        if not session_entry:
            session_entry = {
                "session_number": session_number,
                "question_file": "",
                "generated_at": None,
                "completed": False
            }
            log_data["sessions"].append(session_entry)

        # Update session entry
        session_entry.update({
            "question_title": question_title,
            "difficulty": difficulty,
            "topics": topics,
            "completed_at": datetime.now().isoformat(),
            "time_taken_minutes": time_taken_minutes,
            "passed": passed,
            "notes": notes,
            "completed": True
        })

        # Save updated log
        with open(self.solved_log_file, 'w') as f:
            json.dump(log_data, f, indent=2)

        # Update stats
        self._update_stats()

    def mark_session_generated(self, session_number: int) -> None:
        """
        Mark when a session was generated.

        Args:
            session_number: Session number
        """
        if self.solved_log_file.exists():
            with open(self.solved_log_file, 'r') as f:
                log_data = json.load(f)

            for session in log_data["sessions"]:
                if session["session_number"] == session_number:
                    session["generated_at"] = datetime.now().isoformat()
                    break

            with open(self.solved_log_file, 'w') as f:
                json.dump(log_data, f, indent=2)

    def get_session_log(self) -> List[Dict[str, Any]]:
        """
        Get all session log entries.

        Returns:
            List of session entries
        """
        if self.solved_log_file.exists():
            with open(self.solved_log_file, 'r') as f:
                log_data = json.load(f)
                return log_data.get("sessions", [])
        return []

    def _update_stats(self) -> None:
        """Update the statistics file based on session log."""
        sessions = self.get_session_log()

        # Calculate statistics
        total_sessions = len(sessions)
        completed_sessions = sum(1 for s in sessions if s.get("completed", False))

        # Count by difficulty
        by_difficulty = defaultdict(int)
        for session in sessions:
            if session.get("completed", False):
                difficulty = session.get("difficulty", "unknown").lower()
                by_difficulty[difficulty] += 1

        # Count by topic
        by_topic = defaultdict(int)
        for session in sessions:
            if session.get("completed", False):
                for topic in session.get("topics", []):
                    by_topic[topic.lower()] += 1

        # Calculate success rate
        passed_sessions = sum(1 for s in sessions if s.get("completed", False) and s.get("passed", False))
        success_rate = (passed_sessions / completed_sessions * 100) if completed_sessions > 0 else 0.0

        # Calculate average time
        times = [s.get("time_taken_minutes", 0) for s in sessions if s.get("completed", False) and s.get("time_taken_minutes")]
        average_time = sum(times) / len(times) if times else 0.0

        # Create stats dictionary
        stats = {
            "total_sessions": total_sessions,
            "completed_sessions": completed_sessions,
            "by_difficulty": dict(by_difficulty),
            "by_topic": dict(by_topic),
            "success_rate": round(success_rate, 2),
            "average_time_minutes": round(average_time, 2),
            "last_updated": datetime.now().isoformat()
        }

        # Save stats
        with open(self.stats_file, 'w') as f:
            json.dump(stats, f, indent=2)

    def get_stats(self) -> Dict[str, Any]:
        """
        Get current statistics.

        Returns:
            Dictionary with statistics
        """
        if self.stats_file.exists():
            with open(self.stats_file, 'r') as f:
                return json.load(f)
        return {
            "total_sessions": 0,
            "completed_sessions": 0,
            "by_difficulty": {},
            "by_topic": {},
            "success_rate": 0.0,
            "average_time_minutes": 0.0
        }

    def print_stats(self) -> None:
        """Print statistics in a formatted way."""
        stats = self.get_stats()

        print("\n" + "="*50)
        print("PROGRESS STATISTICS")
        print("="*50)
        print(f"\nTotal Sessions: {stats['total_sessions']}")
        print(f"Completed Sessions: {stats['completed_sessions']}")
        print(f"Success Rate: {stats['success_rate']:.1f}%")
        print(f"Average Time: {stats['average_time_minutes']:.1f} minutes")

        if stats['by_difficulty']:
            print("\nBy Difficulty:")
            for difficulty, count in sorted(stats['by_difficulty'].items()):
                print(f"  {difficulty.capitalize()}: {count}")

        if stats['by_topic']:
            print("\nBy Topic (Top 10):")
            sorted_topics = sorted(stats['by_topic'].items(), key=lambda x: x[1], reverse=True)
            for topic, count in sorted_topics[:10]:
                print(f"  {topic}: {count}")

        print("="*50 + "\n")

    def get_recent_sessions(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get most recent sessions.

        Args:
            limit: Maximum number of sessions to return

        Returns:
            List of recent session entries
        """
        sessions = self.get_session_log()
        completed_sessions = [s for s in sessions if s.get("completed", False)]

        # Sort by completion date (most recent first)
        sorted_sessions = sorted(
            completed_sessions,
            key=lambda x: x.get("completed_at", ""),
            reverse=True
        )

        return sorted_sessions[:limit]

    def print_recent_sessions(self, limit: int = 10) -> None:
        """
        Print recent sessions in a formatted way.

        Args:
            limit: Maximum number of sessions to display
        """
        sessions = self.get_recent_sessions(limit)

        if not sessions:
            print("\nNo completed sessions yet.")
            return

        print("\n" + "="*50)
        print(f"RECENT SESSIONS (Last {limit})")
        print("="*50)

        for session in sessions:
            status = "✓" if session.get("passed", False) else "✗"
            title = session.get("question_title", "Unknown")
            difficulty = session.get("difficulty", "?").upper()
            time_taken = session.get("time_taken_minutes", "?")
            completed_at = session.get("completed_at", "")[:10]  # Just the date

            print(f"\n{status} Session #{session['session_number']}: {title}")
            print(f"   Difficulty: {difficulty} | Time: {time_taken}m | Date: {completed_at}")

            if session.get("notes"):
                print(f"   Notes: {session['notes'][:60]}...")

        print("="*50 + "\n")
