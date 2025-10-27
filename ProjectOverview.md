# Python Interview Prep Project

## Overview
This project is designed to help me **master Python and its core data structures** through real-world coding interview practice.  
Each session generates a **new coding challenge file** containing:
- A **random interview question** from a curated bank (arrays, strings, trees, graphs, recursion, etc.)
- Optional **hints or constraints**
- Space to write my solution function
- Auto-generated **unit tests** (optional)
- A short **self-review checklist**

After solving, I’ll use **Claude** (or another AI assistant) to analyze my solution for:
- Time and space complexity
- Code clarity and optimization suggestions
- Alternative approaches
- Interview-style feedback

This process simulates a realistic interview prep cycle:
> Read → Plan → Code → Review → Improve

## Interview Simulation

- Add a timer (e.g., 25 minutes) to simulate real coding test pressure.
- Automatically hide hints until halfway through the timer.

---

## Project Goals
- Reinforce understanding of **Python fundamentals** and **data structures**
- Build confidence in **problem-solving under pressure**
- Develop structured thinking for **technical interviews**
- Create a personalized **repository of solved problems** for review

---

## Architecture

### Core Workflow

1. **Generate Session** - Run CLI command to create a new session file
   - Randomly selects question from bank (filtered by difficulty/topic if specified)
   - Generates Python file with problem statement, test cases, and solution skeleton
   - Updates tracking data with new session

2. **Solve Problem** - Work in the generated session file
   - Read problem description and constraints
   - Implement solution function
   - Run tests locally to verify correctness

3. **Review & Analyze** - Use test runner and AI feedback
   - Execute test suite to validate solution
   - Get complexity analysis and optimization suggestions
   - Log results and notes for future review

### Key Components

**Question Bank** - Structured repository of interview problems
- Each question is a JSON file with: title, description, examples, constraints, hints, test cases, difficulty, tags
- Organized by difficulty level for progressive learning
- Metadata tracks usage frequency and success rate

**Session Generator** - Creates executable practice files
- Reads question data and applies to template
- Generates standalone Python file with problem context, solution space, and tests
- Names files with incrementing session numbers and problem slugs

**Test Runner** - Validates solutions automatically
- Parses generated session files to extract solution function and test cases
- Executes tests and reports results (pass/fail, execution time)
- Can run single session or batch-test multiple completed sessions

**Progress Tracker** - Maintains solve history
- Logs each session with timestamp, difficulty, time taken, test results
- Provides analytics on strengths/weaknesses by topic
- Supports notes and reflections after each problem

## Folder Structure

```
python-interview-prep/
│
├── questions/                      # Question bank
│   ├── easy/
│   │   ├── two_sum.json
│   │   ├── reverse_string.json
│   │   └── ...
│   ├── medium/
│   │   ├── add_two_numbers.json
│   │   ├── longest_substring.json
│   │   └── ...
│   ├── hard/
│   │   ├── merge_k_sorted_lists.json
│   │   └── ...
│   └── meta.json                   # Tracks question stats
│
├── sessions/                       # Generated practice files
│   ├── session_001_two_sum.py
│   ├── session_002_reverse_linked_list.py
│   └── ...
│
├── utils/                          # Core utilities
│   ├── __init__.py
│   ├── question_generator.py       # Creates new session files
│   ├── template.py                 # Session file template
│   ├── test_runner.py              # Executes tests on solutions
│   ├── progress_tracker.py         # Logs and analyzes solve history
│   └── ai_feedback.py              # (Optional) AI-powered code review
│
├── data/
│   ├── solved_log.json             # Completed sessions log
│   └── stats.json                  # Performance analytics
│
├── cli.py                          # Main entry point for commands
├── config.py                       # Configuration settings
├── README.md
└── requirements.txt
```

## Usage Commands

```bash
# Generate a new session (random question)
python cli.py new

# Generate session with specific difficulty
python cli.py new --difficulty easy

# Generate session for specific topic
python cli.py new --topic arrays

# Run tests on current session
python cli.py test sessions/session_001_two_sum.py

# Run all session tests
python cli.py test-all

# View progress statistics
python cli.py stats

# Get AI feedback on a solution
python cli.py review sessions/session_001_two_sum.py
```

## Session File Structure

Each generated session file contains:

```python
"""
SESSION 001: Two Sum
Difficulty: Easy
Topics: Arrays, Hash Table
Generated: 2025-10-27
"""

# PROBLEM DESCRIPTION
# Given an array of integers nums and an integer target,
# return indices of the two numbers that add up to target.
# ...

# CONSTRAINTS
# - 2 <= nums.length <= 10^4
# - -10^9 <= nums[i] <= 10^9
# ...

# EXAMPLES
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# ...

# HINTS (reveal after 12 minutes)
# 1. Use a hash map to store seen values
# 2. For each number, check if target - number exists in map

# YOUR SOLUTION
def solution(nums, target):
    """
    Your implementation here
    """
    pass

# TEST CASES
import unittest

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(solution([2,7,11,15], 9), [0,1])

    def test_example_2(self):
        self.assertEqual(solution([3,2,4], 6), [1,2])

    # Additional test cases...

if __name__ == "__main__":
    unittest.main()

# SELF-REVIEW CHECKLIST
# [ ] Solution handles edge cases
# [ ] Time complexity: O(?)
# [ ] Space complexity: O(?)
# [ ] Code is readable and well-commented
# [ ] All tests pass
```