# Python Interview Prep Project

> **Recent Update:** Added comprehensive interview preparation module (`00_introduction`) with 7-step problem-solving framework, data structure frequency rankings, and systematic approach to break down any coding problem. All lesson files renamed to topic-specific names (e.g., `strings_lesson.py`). Complete answer checker coverage for all 13 lessons.

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
├── learn/                          # Interactive data structure lessons
│   ├── 00_introduction/            # ⭐ START HERE - Interview prep guide
│   │   ├── interview_guide.py      # 7-step framework & systematic approach
│   │   ├── quick_reference.md      # One-page cheat sheet (print this!)
│   │   ├── problem_breakdown_template.md  # Practice template
│   │   └── README.md               # Getting started guide
│   ├── 01_strings/
│   │   ├── strings_lesson.py       # String exercises
│   │   └── answers/
│   │       └── check_strings.py    # Answer checker
│   ├── 02_lists/
│   │   ├── lists_lesson.py
│   │   └── answers/check_lists.py
│   ├── 03_tuples/
│   │   ├── tuples_lesson.py
│   │   └── answers/check_tuples.py
│   ├── 04_dictionaries/
│   │   ├── dictionaries_lesson.py
│   │   └── answers/check_dictionaries.py
│   ├── 05_sets/
│   │   ├── sets_lesson.py
│   │   └── answers/check_sets.py
│   ├── 06_stacks/
│   │   ├── stacks_lesson.py
│   │   └── answers/check_stacks.py
│   ├── 07_queues/
│   │   ├── queues_lesson.py
│   │   └── answers/check_queues.py
│   ├── 08_deques/
│   │   ├── deques_lesson.py
│   │   └── answers/check_deques.py
│   ├── 09_linked_lists/
│   │   ├── linked_lists_lesson.py
│   │   └── answers/check_linked_lists.py
│   ├── 10_heaps/
│   │   ├── heaps_lesson.py
│   │   └── answers/check_heaps.py
│   ├── 11_trees/
│   │   ├── trees_lesson.py
│   │   └── answers/check_trees.py
│   ├── 12_graphs/
│   │   ├── graphs_lesson.py
│   │   └── answers/check_graphs.py
│   ├── 13_tries/
│   │   ├── tries_lesson.py
│   │   └── answers/check_tries.py
│   ├── check_all_lessons.py        # Master checker (runs all 13 lessons)
│   └── README.md                   # Complete learning guide
│
├── cli.py                          # Main entry point for commands
├── config.py                       # Configuration settings
├── README.md
└── requirements.txt
```

## Learning Mode - Interactive Lessons

The `learn/` directory contains structured, interactive lessons for mastering Python data structures and interview problem-solving techniques.

### ⭐ Start Here: Interview Preparation Guide

**NEW FEATURE:** Before diving into data structures, complete the interview preparation module!

```bash
cd learn/00_introduction
python interview_guide.py
```

The **00_introduction** module provides:
- **7-Step Problem-Solving Framework** - Systematic approach to ANY coding problem
- **Data Structure Interview Frequency Rankings** - Which structures appear most (60-70% vs 15-20%)
- **Pattern Recognition Guide** - Map problem keywords to the right data structure
- **30-Day Structured Roadmap** - Prioritized learning path
- **Quick Reference Cheat Sheet** - One-page guide (print and keep visible!)
- **Problem Breakdown Template** - Practice template for structured problem-solving

**Why start here?** Learn the systematic approach that makes interview problems less intimidating and helps you choose the right tool for each problem.

### How It Works

Each data structure folder contains:
1. **{topic}_lesson.py** - Interactive exercises covering:
   - What is this data structure?
   - Basic operations with examples
   - 10 exercises progressing from simple to advanced
   - Intermediate operations and techniques
   - Real-world industry use cases

2. **answers/check_*.py** - Automated answer checker that:
   - Validates all your exercise implementations
   - Provides immediate feedback (✓ PASSED / ✗ FAILED)
   - Reports which exercises pass/fail with detailed error messages

### Using the Lessons

```bash
# 1. START WITH THE FRAMEWORK (30-45 minutes, one time)
cd learn/00_introduction
python interview_guide.py        # Interactive guide with practice problems
cat quick_reference.md           # Print this for daily reference

# 2. THEN BEGIN DATA STRUCTURE LESSONS
cd learn/01_strings

# Complete exercises in strings_lesson.py, then test
python strings_lesson.py

# Or use the dedicated answer checker
python answers/check_strings.py

# Check all lessons at once (shows progress across all 13 lessons)
cd learn
python check_all_lessons.py
```

### Lesson Progression (30-Day Roadmap)

**Week 0: Foundation** (START HERE!)
- **00_introduction** - Interview framework & systematic problem-solving

**Week 1: Critical (Must Master)** - 60-70% of interview problems
- **01_strings** - 60% of problems
- **02_lists** - 70% of problems
- **04_dictionaries** - 65% of problems
- **05_sets** - 65% of problems

**Week 2: Important (High Priority)** - 30-45% of interview problems
- **06_stacks** - 40% of problems
- **07_queues** - 35% of problems
- **08_deques** - Specialized sliding window problems
- **09_linked_lists** - 30% of problems

**Week 3: Hierarchical (Important)** - 25-45% of interview problems
- **11_trees** - 45% of problems
- **10_heaps** - 25% of problems
- **12_graphs** - 30% of senior interviews

**Week 4: Advanced & Practice**
- **13_tries** - 15% of specialized problems
- **03_tuples** - Supporting concepts
- Mixed problem practice & mock interviews

**Interview Frequency Guide:**
- ⭐⭐⭐⭐⭐ CRITICAL: Lists, Strings, Hash Maps/Sets, Stacks, Queues, Trees
- ⭐⭐⭐⭐ IMPORTANT: Linked Lists, Heaps
- ⭐⭐⭐ ADVANCED: Graphs, Tries
- ⭐⭐ SUPPORTING: Tuples, Deques

See `learn/README.md` for complete learning guide and `learn/00_introduction/README.md` for framework details.

### Key Features of the Learn Directory

**📚 Complete Coverage:**
- 13 data structure lessons with 10 exercises each (130+ total exercises)
- Every lesson has a dedicated answer checker with detailed feedback
- All lesson files uniquely named (`strings_lesson.py`, `trees_lesson.py`, etc.)

**🎯 Interview-Focused:**
- Interview frequency rankings for each data structure (70% vs 15% problems)
- Systematic 7-step framework reduces intimidation and improves success rate
- Pattern recognition guide: "When problem says X, use Y"
- Real-world industry use cases for each data structure

**📊 Systematic Approach:**
- The 7-Step Framework works for ANY coding problem:
  1. Understand (inputs, outputs, constraints)
  2. Examples (work through concrete cases)
  3. Pattern (identify which DS/algorithm)
  4. Breakdown (write pseudocode plan)
  5. Complexity (analyze time/space)
  6. Code (implement cleanly)
  7. Test (verify with edge cases)

**🛠️ Practical Tools:**
- Quick reference cheat sheet (print and keep visible)
- Problem breakdown template (practice on any problem)
- Master checker runs all 13 lessons at once
- Structured 30-day roadmap with daily goals

**🚀 Progressive Learning:**
- Start with critical structures (Lists, Strings, Hash Maps) - 60-70% of problems
- Progress to important structures (Stacks, Queues, Trees) - 30-45% of problems
- Finish with advanced structures (Graphs, Tries) - 15-30% of problems

---

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
