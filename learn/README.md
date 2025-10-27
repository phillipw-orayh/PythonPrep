# Interactive Data Structure Lessons

This directory contains interactive lessons for mastering Python data structures from basic to advanced concepts.

## Getting Started

⭐ **NEW LEARNERS: Start here!** ⭐

**Before diving into the lessons, complete the interview preparation guide:**

```bash
cd learn/00_introduction
python interview_guide.py
```

This guide provides:
- Data structure interview frequency rankings (which to prioritize)
- **7-Step Problem-Solving Framework** for any coding problem
- Systematic approach to break down intimidating problems
- 30-day structured learning roadmap
- Pattern recognition for choosing the right data structure

**Read the guide files:**
- `interview_guide.py` - Comprehensive framework and practice problems
- `quick_reference.md` - One-page cheat sheet (print this!)
- `problem_breakdown_template.md` - Template for practicing any problem

## Overview

Each data structure has its own folder with:
- **{topic}_lesson.py**: Interactive exercises to complete (e.g., `strings_lesson.py`)
- **answers/check_*.py**: Answer checker to validate your solutions

## Structure

### Introduction (START HERE)
0. **00_introduction** - Interview prep guide, problem-solving framework, and quick reference

### Basic Data Structures
1. **01_strings** (`strings_lesson.py`) - Text manipulation and processing
2. **02_lists** (`lists_lesson.py`) - Dynamic arrays and sequences
3. **03_tuples** (`tuples_lesson.py`) - Immutable sequences

### Intermediate Data Structures
4. **04_dictionaries** (`dictionaries_lesson.py`) - Key-value pairs and hash tables
5. **05_sets** (`sets_lesson.py`) - Unique collections and set operations
6. **06_stacks** (`stacks_lesson.py`) - LIFO (Last In First Out) data structure
7. **07_queues** (`queues_lesson.py`) - FIFO (First In First Out) data structure
8. **08_deques** (`deques_lesson.py`) - Double-ended queues

### Advanced Data Structures
9. **09_linked_lists** (`linked_lists_lesson.py`) - Node-based sequences
10. **10_heaps** (`heaps_lesson.py`) - Priority queues and heap operations
11. **11_trees** (`trees_lesson.py`) - Binary trees, BST, traversals
12. **12_graphs** (`graphs_lesson.py`) - Graph representations and algorithms
13. **13_tries** (`tries_lesson.py`) - Prefix trees for string operations

## How to Use

### Working on a Lesson

1. **Open the lesson file:**
   ```bash
   cd learn/01_strings
   python strings_lesson.py
   ```

2. **Implement the exercises:**
   - Open `strings_lesson.py` in your editor (or appropriate lesson file)
   - Find functions marked with `# TODO: Implement this function`
   - Write your solution
   - Save the file

3. **Test your implementation:**
   ```bash
   # Run the lesson's built-in tests
   python strings_lesson.py

   # Or use the dedicated answer checker
   python answers/check_strings.py
   ```

### Each Lesson Contains

Each lesson file is named `<topic>_lesson.py` (e.g., `strings_lesson.py`, `trees_lesson.py`)

1. **Introduction** - What is this data structure?
2. **Basic Operations** - Fundamental operations with examples
3. **Simple Exercises** - Beginner-friendly problems to solve
4. **Intermediate Operations** - More advanced techniques
5. **Advanced Exercises** - Challenge problems
6. **Industry Use Cases** - Real-world applications

### Checking All Lessons

To check all your completed lessons at once:

```bash
cd learn
python check_all_lessons.py
```

This will:
- Run all answer checkers sequentially
- Show which lessons passed/failed
- Provide a summary of your progress

## Learning Path

**Recommended Order (30-Day Roadmap):**

### Week 0: Foundation (START HERE!)
0. **Complete `00_introduction`** - Learn the 7-step framework and problem-solving approach

### Week 1: Critical Structures (Must Master)
1. **Arrays/Lists** (`02_lists`) - 70% of interview problems
2. **Strings** (`01_strings`) - 60% of interview problems
3. **Hash Maps/Sets** (`04_dictionaries`, `05_sets`) - 65% of interview problems

### Week 2: Sequential Structures (High Priority)
4. **Stacks** (`06_stacks`) - 40% of interview problems
5. **Queues** (`07_queues`, `08_deques`) - 35% of interview problems
6. **Linked Lists** (`09_linked_lists`) - 30% of interview problems

### Week 3: Hierarchical Structures (Important)
7. **Binary Trees** (`11_trees`) - 45% of interview problems
8. **Heaps** (`10_heaps`) - 25% of interview problems
9. **Graphs** (`12_graphs`) - 30% of senior interviews

### Week 4: Advanced + Practice
10. **Tries** (`13_tries`) - 15% of specialized problems
11. **Tuples** (`03_tuples`) - Supporting concepts
12. Mixed problem practice and mock interviews

**Interview Frequency Guide:**
- ⭐⭐⭐⭐⭐ CRITICAL: Lists, Strings, Hash Maps/Sets, Stacks, Queues, Trees
- ⭐⭐⭐⭐ IMPORTANT: Linked Lists, Heaps
- ⭐⭐⭐ ADVANCED: Graphs, Tries
- ⭐⭐ SUPPORTING: Tuples, Deques

## Tips for Success

- **Understand Before Coding**: Read the entire lesson section before implementing
- **Start Simple**: Begin with the basic exercises before attempting advanced ones
- **Test Frequently**: Run tests after each function to catch errors early
- **Read Industry Use Cases**: Understanding real-world applications helps retention
- **Practice**: Come back to previous lessons periodically to reinforce learning

## Example Workflow

```bash
# 1. Navigate to a lesson
cd 01_strings

# 2. Read the lesson and implement exercises
# (Open strings_lesson.py in your favorite editor)

# 3. Test your solutions
python strings_lesson.py

# 4. Check with answer checker
python answers/check_strings.py

# 5. Move to next lesson when all tests pass
cd ../02_lists
python lists_lesson.py
```

## Progress Tracking

You can track your progress by:
- Running individual answer checkers
- Using `check_all_lessons.py` for a complete overview
- Keeping notes on difficult concepts in each lesson

## Additional Resources

- Python official documentation: https://docs.python.org/3/tutorial/datastructures.html
- Time complexity reference: https://wiki.python.org/moin/TimeComplexity
- Algorithm visualizations: https://visualgo.net/

## Getting Help

If you're stuck on an exercise:
1. Review the hints provided in the function docstring
2. Check the demonstration functions in the lesson
3. Review the "Industry Use Cases" section for context
4. Use Claude Code or another AI assistant for explanations

Happy learning! 🚀
