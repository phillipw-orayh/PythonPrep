"""Question generator for creating new interview session files."""

import json
import random
from pathlib import Path
from typing import Optional, List, Dict, Any

from config import (
    QUESTIONS_DIR, SESSIONS_DIR, SOLVED_LOG_FILE,
    EASY_DIR, MEDIUM_DIR, HARD_DIR, DIFFICULTY_LEVELS
)
from .template import generate_session_content


class QuestionGenerator:
    """Generates new session files from the question bank."""

    def __init__(self):
        """Initialize the question generator."""
        self.questions_dir = QUESTIONS_DIR
        self.sessions_dir = SESSIONS_DIR
        self.solved_log_file = SOLVED_LOG_FILE

        # Ensure directories exist
        self.sessions_dir.mkdir(exist_ok=True)

    def get_available_questions(
        self,
        difficulty: Optional[str] = None,
        topic: Optional[str] = None
    ) -> List[Path]:
        """
        Get list of available question files from the question bank.

        Args:
            difficulty: Filter by difficulty level (easy, medium, hard)
            topic: Filter by topic/tag

        Returns:
            List of paths to question JSON files
        """
        questions = []

        # Determine which directories to search
        if difficulty:
            if difficulty.lower() not in DIFFICULTY_LEVELS:
                raise ValueError(f"Invalid difficulty: {difficulty}. Must be one of {DIFFICULTY_LEVELS}")
            search_dirs = [self.questions_dir / difficulty.lower()]
        else:
            search_dirs = [EASY_DIR, MEDIUM_DIR, HARD_DIR]

        # Collect all JSON files (excluding meta.json)
        for directory in search_dirs:
            if directory.exists():
                for file in directory.glob("*.json"):
                    if file.name != "meta.json":
                        # If topic filter is specified, check if question has that topic
                        if topic:
                            with open(file, 'r') as f:
                                question_data = json.load(f)
                                topics = question_data.get("topics", [])
                                if topic.lower() in [t.lower() for t in topics]:
                                    questions.append(file)
                        else:
                            questions.append(file)

        return questions

    def get_next_session_number(self) -> int:
        """
        Get the next session number by reading the solved log.

        Returns:
            Next session number
        """
        if self.solved_log_file.exists():
            with open(self.solved_log_file, 'r') as f:
                log_data = json.load(f)
                return log_data.get("last_session_number", 0) + 1
        return 1

    def update_session_log(self, session_number: int, question_file: str) -> None:
        """
        Update the solved log with new session information.

        Args:
            session_number: The session number
            question_file: Name of the question file used
        """
        if self.solved_log_file.exists():
            with open(self.solved_log_file, 'r') as f:
                log_data = json.load(f)
        else:
            log_data = {"sessions": [], "last_session_number": 0}

        log_data["last_session_number"] = session_number
        log_data["sessions"].append({
            "session_number": session_number,
            "question_file": question_file,
            "generated_at": None,  # Will be updated by progress tracker
            "completed": False
        })

        with open(self.solved_log_file, 'w') as f:
            json.dump(log_data, f, indent=2)

    def generate_session(
        self,
        difficulty: Optional[str] = None,
        topic: Optional[str] = None,
        question_file: Optional[Path] = None
    ) -> Path:
        """
        Generate a new session file.

        Args:
            difficulty: Filter questions by difficulty level
            topic: Filter questions by topic
            question_file: Specific question file to use (overrides filters)

        Returns:
            Path to the generated session file

        Raises:
            ValueError: If no questions are available with the given filters
            FileNotFoundError: If specified question_file doesn't exist
        """
        # Get or select question file
        if question_file:
            if not question_file.exists():
                raise FileNotFoundError(f"Question file not found: {question_file}")
            selected_file = question_file
        else:
            available_questions = self.get_available_questions(difficulty, topic)

            if not available_questions:
                filter_msg = []
                if difficulty:
                    filter_msg.append(f"difficulty={difficulty}")
                if topic:
                    filter_msg.append(f"topic={topic}")
                filters = ", ".join(filter_msg) if filter_msg else "no filters"
                raise ValueError(f"No questions available with {filters}")

            # Randomly select a question
            selected_file = random.choice(available_questions)

        # Load question data
        with open(selected_file, 'r') as f:
            question_data = json.load(f)

        # Get next session number
        session_number = self.get_next_session_number()

        # Generate session content
        session_content = generate_session_content(session_number, question_data)

        # Create session filename
        title_slug = question_data.get("title", "question").lower()
        title_slug = title_slug.replace(" ", "_").replace("-", "_")
        # Remove special characters
        title_slug = "".join(c for c in title_slug if c.isalnum() or c == "_")
        session_filename = f"session_{session_number:03d}_{title_slug}.py"
        session_path = self.sessions_dir / session_filename

        # Write session file
        with open(session_path, 'w') as f:
            f.write(session_content)

        # Update log
        self.update_session_log(session_number, selected_file.name)

        return session_path

    def list_questions(self, difficulty: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List all available questions with their metadata.

        Args:
            difficulty: Filter by difficulty level

        Returns:
            List of dictionaries with question information
        """
        questions = []
        available_files = self.get_available_questions(difficulty)

        for file in available_files:
            with open(file, 'r') as f:
                data = json.load(f)
                questions.append({
                    "file": file.name,
                    "title": data.get("title", "Untitled"),
                    "difficulty": data.get("difficulty", "Unknown"),
                    "topics": data.get("topics", [])
                })

        return questions
