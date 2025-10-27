# Python Interview Prep

A Python-based interview preparation tool that generates coding challenge sessions with automatic test cases and progress tracking.

## Overview

This project helps you master Python and core data structures through real-world coding interview practice. Each session generates a new coding challenge file containing:

- A random interview question from a curated bank
- Optional hints and constraints
- Space to write your solution function
- Auto-generated unit tests
- A self-review checklist

## Features

- **Question Bank**: Organized by difficulty (easy, medium, hard) and topics
- **Session Generator**: Creates standalone Python files with problems and tests
- **Test Runner**: Validates solutions automatically
- **Progress Tracker**: Logs session history and provides analytics
- **CLI Interface**: Simple commands for workflow management

## Installation

1. Clone or download this repository
2. Ensure Python 3.8+ is installed
3. No external dependencies required (uses standard library)

```bash
cd PythonPrep
python cli.py --help
```

## Quick Start

### 1. Add Questions to the Bank

Create JSON files in `questions/easy/`, `questions/medium/`, or `questions/hard/`:

```json
{
  "title": "Two Sum",
  "difficulty": "easy",
  "topics": ["arrays", "hash_tables"],
  "description": "Given an array of integers nums and an integer target, return indices of the two numbers that add up to target.",
  "constraints": [
    "2 <= nums.length <= 10^4",
    "-10^9 <= nums[i] <= 10^9"
  ],
  "examples": [
    {
      "input": "nums = [2,7,11,15], target = 9",
      "output": "[0,1]",
      "explanation": "nums[0] + nums[1] = 9"
    }
  ],
  "hints": [
    "Use a hash map to store seen values",
    "For each number, check if target - number exists"
  ],
  "test_cases": [
    {
      "input": "[2,7,11,15], 9",
      "expected": "[0,1]"
    },
    {
      "input": "[3,2,4], 6",
      "expected": "[1,2]"
    }
  ],
  "function_signature": "def solution(nums, target):\n    pass"
}
```

### 2. Generate a New Session

```bash
# Random question
python cli.py new

# Specific difficulty
python cli.py new --difficulty easy

# Specific topic
python cli.py new --topic arrays
```

### 3. Solve the Problem

Open the generated session file in `sessions/` and implement your solution.

### 4. Run Tests

```bash
# Test specific session
python cli.py test sessions/session_001_two_sum.py

# Run all session tests
python cli.py test-all
```

### 5. View Progress

```bash
# Show statistics
python cli.py stats

# Show recent sessions
python cli.py stats --recent 10
```

## CLI Commands

### Generate New Session
```bash
python cli.py new [--difficulty easy|medium|hard] [--topic TOPIC]
```

### Run Tests
```bash
python cli.py test <session_file>
python cli.py test-all [-v]
```

### List Questions
```bash
python cli.py list [--difficulty easy|medium|hard]
```

### View Statistics
```bash
python cli.py stats [--recent N]
```

### Log Session Manually
```bash
python cli.py log SESSION_NUMBER --title "Question Title" --difficulty easy --topics arrays,strings [--time MINUTES] [--passed] [--notes "Notes"]
```

## Project Structure

```
PythonPrep/
├── questions/              # Question bank
│   ├── easy/              # Easy questions (JSON)
│   ├── medium/            # Medium questions (JSON)
│   ├── hard/              # Hard questions (JSON)
│   └── meta.json          # Question metadata
├── sessions/              # Generated practice files
├── utils/                 # Core utilities
│   ├── question_generator.py
│   ├── template.py
│   ├── test_runner.py
│   ├── progress_tracker.py
│   └── ai_feedback.py
├── data/                  # Tracking data
│   ├── solved_log.json
│   └── stats.json
├── cli.py                 # CLI entry point
├── config.py              # Configuration
└── README.md
```

## Session File Format

Each generated session file contains:

```python
"""
SESSION 001: Two Sum
Difficulty: Easy
Topics: Arrays, Hash Table
Generated: 2025-10-27
"""

# PROBLEM DESCRIPTION
# Your problem here...

# CONSTRAINTS
# Your constraints here...

# EXAMPLES
# Your examples here...

# HINTS (reveal after 12 minutes)
# Your hints here...

# YOUR SOLUTION
def solution(nums, target):
    """Your implementation here"""
    pass

# TEST CASES
import unittest

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution([2,7,11,15], 9), [0,1])

if __name__ == "__main__":
    unittest.main()

# SELF-REVIEW CHECKLIST
# [ ] Solution handles edge cases
# [ ] Time complexity: O(?)
# [ ] Space complexity: O(?)
# [ ] Code is readable and well-commented
# [ ] All tests pass
```

## Tips for Success

1. **Time Yourself**: Use a 25-minute timer to simulate real interview pressure
2. **Read Carefully**: Understand the problem and constraints before coding
3. **Think First**: Plan your approach before implementing
4. **Test Edge Cases**: Consider empty inputs, single elements, duplicates, etc.
5. **Analyze Complexity**: Always determine time and space complexity
6. **Review and Improve**: Use AI assistants (Claude, ChatGPT) to review your solutions

## Customization

Edit `config.py` to customize:

- Session time limits
- Hint reveal timing
- Directory paths
- Available topics

## Future Enhancements

- Timer integration with hint reveals
- AI-powered solution feedback (via Claude or OpenAI API)
- Web interface for session management
- Spaced repetition algorithm for question selection
- Company-specific question filters
- Mock interview mode with time tracking

## License

This is a personal project for interview preparation. Feel free to use and modify as needed.
