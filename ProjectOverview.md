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

## Folder Structure

python-interview-prep/
│
├── questions/
│ ├── easy/
│ ├── medium/
│ ├── hard/
│ └── meta.json # Metadata for tracking frequency/difficulty
│
├── sessions/
│ ├── session_001_two_sum.py
│ ├── session_002_reverse_linked_list.py
│ └── ...
│
├── utils/
│ ├── question_generator.py # Creates new challenge file
│ ├── template.py # Base format for each challenge
│ ├── ai_feedback.py # (Optional) Connects to Claude or API for feedback
│ └── test_runner.py # Auto-runs tests on your solutions
│
├── data/
│ └── solved_log.json # Keeps track of completed problems and notes
│
├── README.md
└── requirements.txt