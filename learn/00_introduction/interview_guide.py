"""
INTERVIEW PREPARATION GUIDE
===========================

This guide provides:
1. Overview of all data structures and their interview frequency
2. Systematic framework for solving ANY coding interview problem
3. Pattern recognition for choosing the right data structure
4. Step-by-step problem breakdown methodology

Complete this guide before starting the individual lessons.
"""

# ============================================================================
# PART 1: DATA STRUCTURES - INTERVIEW FREQUENCY GUIDE
# ============================================================================

"""
CRITICAL (Must Master - 80% of Interview Problems)
===================================================
These data structures appear in the vast majority of coding interviews.
You MUST be comfortable with these to succeed.

1. ARRAYS/LISTS ⭐⭐⭐⭐⭐
   - Interview Frequency: VERY HIGH (appears in 70%+ of problems)
   - Why: Foundation for most algorithms, easy to test multiple concepts
   - Common Problems: Two pointers, sliding window, kadane's algorithm
   - Master These: Iteration, slicing, in-place modifications
   - Lesson: 02_lists

2. STRINGS ⭐⭐⭐⭐⭐
   - Interview Frequency: VERY HIGH (appears in 60%+ of problems)
   - Why: Text processing is universal, tests pattern matching skills
   - Common Problems: Palindromes, anagrams, pattern matching, parsing
   - Master These: Character manipulation, substring operations
   - Lesson: 01_strings

3. HASH TABLES (Dictionaries/Sets) ⭐⭐⭐⭐⭐
   - Interview Frequency: VERY HIGH (appears in 65%+ of problems)
   - Why: O(1) lookups enable efficient solutions to many problems
   - Common Problems: Two sum, frequency counting, caching, deduplication
   - Master These: Dictionary operations, set operations, hash collisions
   - Lessons: 04_dictionaries, 05_sets

4. STACKS ⭐⭐⭐⭐
   - Interview Frequency: HIGH (appears in 40%+ of problems)
   - Why: LIFO pattern is common in parsing, backtracking, and DFS
   - Common Problems: Balanced parentheses, next greater element, calculator
   - Master These: Push/pop operations, monotonic stack pattern
   - Lesson: 06_stacks

5. QUEUES ⭐⭐⭐⭐
   - Interview Frequency: HIGH (appears in 35%+ of problems)
   - Why: FIFO pattern essential for BFS and level-order processing
   - Common Problems: BFS, level-order traversal, sliding window maximum
   - Master These: Enqueue/dequeue, deque for sliding window
   - Lessons: 07_queues, 08_deques


IMPORTANT (High Value - 50% of Interview Problems)
===================================================
These appear frequently, especially in mid-level and senior interviews.

6. BINARY TREES ⭐⭐⭐⭐
   - Interview Frequency: HIGH (appears in 45%+ of problems)
   - Why: Tests recursion, DFS/BFS, and hierarchical thinking
   - Common Problems: Traversals, BST validation, path sum, LCA
   - Master These: Recursion, in-order/pre-order/post-order, level-order
   - Lesson: 11_trees

7. LINKED LISTS ⭐⭐⭐
   - Interview Frequency: MEDIUM-HIGH (appears in 30%+ of problems)
   - Why: Tests pointer manipulation and in-place operations
   - Common Problems: Reverse, cycle detection, merge, remove nth node
   - Master These: Two-pointer technique, dummy nodes, in-place modifications
   - Lesson: 09_linked_lists

8. HEAPS (Priority Queues) ⭐⭐⭐
   - Interview Frequency: MEDIUM (appears in 25%+ of problems)
   - Why: Efficient for top-k problems and greedy algorithms
   - Common Problems: Kth largest, merge k lists, median from stream
   - Master These: heapq module, max-heap simulation, heap invariants
   - Lesson: 10_heaps


ADVANCED (Specialized - 20% of Interview Problems)
===================================================
These appear in senior/specialized roles or advanced problem sets.

9. GRAPHS ⭐⭐⭐
   - Interview Frequency: MEDIUM (appears in 30%+ of senior interviews)
   - Why: Tests advanced algorithms and complex problem modeling
   - Common Problems: BFS/DFS, shortest path, connected components, topological sort
   - Master These: Adjacency list, DFS/BFS, Dijkstra's, Union-Find
   - Lesson: 12_graphs

10. TRIES ⭐⭐
    - Interview Frequency: LOW-MEDIUM (appears in 15%+ of problems)
    - Why: Specialized for string prefix/search problems
    - Common Problems: Autocomplete, word search, longest common prefix
    - Master These: Trie construction, prefix search, word break
    - Lesson: 13_tries

11. TUPLES ⭐⭐
    - Interview Frequency: LOW (rarely the focus, but used as tool)
    - Why: Immutable data, multiple return values, dictionary keys
    - Common Problems: Coordinate systems, constant data
    - Master These: Immutability, unpacking, as dict keys
    - Lesson: 03_tuples

12. DEQUES ⭐⭐
    - Interview Frequency: LOW-MEDIUM (often part of queue problems)
    - Why: Efficient for sliding window and double-ended operations
    - Common Problems: Sliding window maximum, palindrome check
    - Master These: appendleft/popleft, sliding window optimization
    - Lesson: 08_deques
"""


# ============================================================================
# PART 2: THE SYSTEMATIC PROBLEM-SOLVING FRAMEWORK
# ============================================================================

"""
THE 7-STEP INTERVIEW PROBLEM BREAKDOWN FRAMEWORK
=================================================

This framework helps you approach ANY coding problem systematically,
reducing intimidation and increasing your success rate.

STEP 1: UNDERSTAND THE PROBLEM (2-3 minutes)
---------------------------------------------
Goal: Ensure you fully understand what's being asked before coding.

Questions to ask yourself:
□ What are the inputs? (types, ranges, constraints)
□ What are the outputs? (type, format)
□ What are the edge cases? (empty input, single element, duplicates, etc.)
□ Are there any constraints? (time/space complexity, in-place, immutability)
□ Can I restate the problem in my own words?

Actions:
1. Read the problem statement twice
2. Write down inputs and outputs
3. Ask clarifying questions (in real interview, ask interviewer)
4. Identify edge cases

Example:
Problem: "Find two numbers in array that sum to target"
- Input: array of integers, target integer
- Output: indices of the two numbers
- Edge cases: no solution, multiple solutions, negative numbers
- Constraints: each input has exactly one solution


STEP 2: EXPLORE WITH EXAMPLES (2-3 minutes)
--------------------------------------------
Goal: Build intuition by working through concrete examples.

Actions:
1. Create 2-3 simple examples
2. Create 1-2 edge case examples
3. Manually solve each example step-by-step
4. Look for patterns in your solution approach

Example:
Problem: Two Sum
Examples:
- [2,7,11,15], target=9 → [0,1] (because 2+7=9)
- [3,2,4], target=6 → [1,2] (because 2+4=6)
- Edge: [3,3], target=6 → [0,1] (duplicates allowed)
- Edge: [1,2,3], target=10 → no solution?

Pattern noticed: Need to check if complement (target - num) exists


STEP 3: IDENTIFY THE PATTERN (2-3 minutes)
-------------------------------------------
Goal: Recognize which algorithmic pattern or data structure applies.

Common Interview Patterns:
□ Two Pointers (sorted array, linked list problems)
□ Sliding Window (subarray/substring problems)
□ Fast & Slow Pointers (cycle detection, middle finding)
□ Hash Map/Set (lookups, frequency counting, caching)
□ Stack (balanced parentheses, next greater, parsing)
□ Queue/BFS (shortest path, level-order)
□ DFS/Backtracking (permutations, combinations, path finding)
□ Binary Search (sorted array search, search space reduction)
□ Dynamic Programming (optimization, counting ways)
□ Greedy (local optimal leading to global optimal)
□ Heap (top-k, merge sorted, priority queue)

Pattern Selection Guide:
- "Find pair/triplet in array" → Two Pointers or Hash Map
- "Subarray/substring with condition" → Sliding Window
- "All permutations/combinations" → Backtracking
- "Shortest path/minimum steps" → BFS
- "Tree/graph traversal" → DFS or BFS
- "Top k elements" → Heap
- "Frequency/counting" → Hash Map
- "Matching/balancing" → Stack
- "Optimization/max/min" → Dynamic Programming or Greedy


STEP 4: BREAK DOWN THE SOLUTION (3-5 minutes)
----------------------------------------------
Goal: Create a step-by-step plan before writing any code.

Actions:
1. Write pseudocode or bullet points
2. Identify data structures needed
3. Outline the algorithm steps
4. Note any helper functions needed
5. Consider edge cases in your plan

Example (Two Sum):
Plan:
1. Create a hash map to store {value: index}
2. Loop through array:
   a. Calculate complement = target - current_num
   b. Check if complement exists in hash map
   c. If yes, return [map[complement], current_index]
   d. If no, add current_num to hash map
3. If loop completes, no solution exists

Data structures: Hash map (dictionary)
Edge cases: Check for duplicates, ensure not using same element twice


STEP 5: ANALYZE COMPLEXITY (1-2 minutes)
-----------------------------------------
Goal: Understand time/space tradeoffs before coding.

Questions:
□ What's the time complexity? O(?)
□ What's the space complexity? O(?)
□ Can I do better?
□ What's the optimal solution?

Common Optimizations:
- Nested loops (O(n²)) → Hash map (O(n))
- Repeated calculations → Memoization/DP
- Sorting might help → O(n log n) vs O(n²)
- Stack/Queue for iteration → Instead of recursion
- Two pointers → Instead of nested loops

Example (Two Sum):
Brute force: O(n²) time, O(1) space (nested loops)
Optimized: O(n) time, O(n) space (hash map)
Trade-off: Using space to save time


STEP 6: CODE THE SOLUTION (10-15 minutes)
------------------------------------------
Goal: Translate your plan into clean, working code.

Best Practices:
1. Start with function signature and docstring
2. Handle edge cases first
3. Write code following your pseudocode
4. Use meaningful variable names
5. Add comments for complex logic
6. Code incrementally and test as you go

Example:
def two_sum(nums: list, target: int) -> list:
    '''Find indices of two numbers that sum to target.'''
    # Edge case: empty or single element
    if len(nums) < 2:
        return []

    # Hash map to store {value: index}
    seen = {}

    # Iterate through array
    for i, num in enumerate(nums):
        complement = target - num

        # Check if complement exists
        if complement in seen:
            return [seen[complement], i]

        # Store current number
        seen[num] = i

    # No solution found
    return []


STEP 7: TEST AND VERIFY (3-5 minutes)
--------------------------------------
Goal: Ensure your solution works correctly.

Testing Checklist:
□ Test with your example cases
□ Test edge cases (empty, single element, all same, etc.)
□ Test boundary conditions (min/max values)
□ Walk through the code line-by-line for one example
□ Check for off-by-one errors
□ Verify time/space complexity

Common Edge Cases by Data Structure:
- Arrays: empty [], single element [1], all same [5,5,5]
- Strings: empty "", single char "a", all same "aaaa"
- Trees: null root, single node, unbalanced tree
- Linked Lists: null head, single node, circular
- Graphs: disconnected, single node, cycles

Example Testing:
✓ [2,7,11,15], target=9 → [0,1] ✓
✓ [3,3], target=6 → [0,1] ✓
✓ [], target=5 → [] ✓
✓ [1], target=5 → [] ✓
"""


# ============================================================================
# PART 3: PATTERN RECOGNITION - CHOOSING THE RIGHT DATA STRUCTURE
# ============================================================================

"""
QUICK REFERENCE: PROBLEM → DATA STRUCTURE MAPPING
==================================================

When you see these keywords/patterns in a problem, consider these data structures:

KEYWORDS → DATA STRUCTURE
-------------------------

"Find pair/two elements" → Hash Map or Two Pointers
"Count frequency" → Hash Map (Counter)
"Remove duplicates" → Set or Hash Map
"Fast lookup/search" → Hash Map or Set
"Check existence" → Set

"Valid parentheses/brackets" → Stack
"Next greater/smaller element" → Stack (Monotonic Stack)
"Reverse/undo operations" → Stack
"Expression evaluation" → Stack
"Backtracking/DFS" → Stack (or recursion)

"Level order" → Queue (BFS)
"Shortest path (unweighted)" → Queue (BFS)
"First-come-first-served" → Queue
"Sliding window maximum" → Deque

"Top K elements" → Heap
"Kth largest/smallest" → Heap
"Median from stream" → Two Heaps
"Merge K sorted" → Heap
"Priority scheduling" → Heap

"Tree/graph traversal" → DFS (recursion/stack) or BFS (queue)
"Connected components" → DFS or Union-Find
"Shortest path (weighted)" → Dijkstra's (Heap + Graph)
"Topological sort" → DFS or BFS (Graph)

"Prefix matching" → Trie
"Autocomplete" → Trie
"Word search in board" → Trie + DFS
"Dictionary operations" → Trie

"Ordered data" → List or Linked List
"Fast insert/delete at ends" → Deque or Linked List
"Fast insert/delete middle" → Linked List
"Binary search" → Sorted List


PROBLEM PATTERNS → APPROACH
----------------------------

"Find subarrays/substrings with condition" → Sliding Window
"Find all permutations/combinations" → Backtracking
"Optimize/maximize/minimize" → Dynamic Programming or Greedy
"Path in tree/graph" → DFS or BFS
"Cycle detection" → Fast & Slow Pointers or DFS
"Sorted array search" → Binary Search
"In-place array manipulation" → Two Pointers
"Range queries" → Prefix Sum or Segment Tree
"""


# ============================================================================
# PART 4: COMMON PITFALLS AND HOW TO AVOID THEM
# ============================================================================

"""
INTERVIEW ANTI-PATTERNS (WHAT NOT TO DO)
=========================================

❌ DON'T start coding immediately
   ✅ DO spend time understanding and planning (Steps 1-5)

❌ DON'T aim for perfect solution first try
   ✅ DO start with brute force, then optimize

❌ DON'T stay silent while solving
   ✅ DO think out loud, explain your reasoning

❌ DON'T ignore edge cases
   ✅ DO test with edge cases before submitting

❌ DON'T memorize solutions
   ✅ DO understand patterns and adapt them

❌ DON'T give up when stuck
   ✅ DO ask for hints, discuss trade-offs

❌ DON'T write messy code
   ✅ DO use clear variable names and structure

❌ DON'T forget to analyze complexity
   ✅ DO state time/space complexity explicitly


DEBUGGING CHECKLIST
===================
When your solution doesn't work:

□ Check off-by-one errors (< vs <=, index+1, etc.)
□ Verify loop boundaries (start, end, increment)
□ Test edge cases (empty, single element, all same)
□ Check variable initialization
□ Verify return statements (all paths return?)
□ Check for integer overflow
□ Verify array/string indexing
□ Check for null/None references
□ Trace through with simple example
"""


# ============================================================================
# PART 5: PRACTICE EXERCISES - APPLY THE FRAMEWORK
# ============================================================================

def practice_problem_1():
    """
    PRACTICE: Apply the 7-Step Framework

    Problem: Valid Palindrome
    Given a string s, determine if it is a palindrome, considering only
    alphanumeric characters and ignoring cases.

    Example:
        Input: "A man, a plan, a canal: Panama"
        Output: True

    YOUR TASK:
    Work through Steps 1-7 on paper before looking at the solution below.

    STEP 1: UNDERSTAND
    ------------------
    - Input: string (may contain spaces, punctuation, mixed case)
    - Output: boolean (True if palindrome, False otherwise)
    - Edge cases: empty string, single char, all spaces, all punctuation
    - Constraints: ignore non-alphanumeric, case-insensitive

    STEP 2: EXAMPLES
    ----------------
    - "A man, a plan, a canal: Panama" → "amanaplanacanalpanama" → True
    - "race a car" → "raceacar" → False
    - "ab_a" → "aba" → True
    - "" → "" → True (empty is palindrome)

    STEP 3: PATTERN
    ---------------
    Pattern: Two Pointers (left and right moving toward center)
    Data structure: String manipulation, no extra DS needed

    STEP 4: BREAKDOWN
    -----------------
    1. Create two pointers: left=0, right=len(s)-1
    2. While left < right:
       a. Skip non-alphanumeric from left
       b. Skip non-alphanumeric from right
       c. Compare characters (case-insensitive)
       d. If mismatch, return False
       e. Move pointers inward
    3. If loop completes, return True

    STEP 5: COMPLEXITY
    ------------------
    Time: O(n) - single pass through string
    Space: O(1) - only two pointers

    STEP 6: CODE (below)
    STEP 7: TEST (see test cases below)
    """
    # Solution implementation
    def is_palindrome(s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    # Test cases
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    print("✓ All practice tests passed!")


def practice_problem_2():
    """
    PRACTICE: Identify the Pattern

    Problem: Two Sum
    Given an array of integers nums and an integer target, return indices
    of the two numbers that sum to target.

    IDENTIFY:
    1. What pattern does this problem follow?
    2. What data structure should you use?
    3. What's the optimal time/space complexity?

    ANSWERS:
    1. Pattern: Hash Map for O(1) lookups
    2. Data structure: Dictionary {value: index}
    3. Time: O(n), Space: O(n)
    """
    def two_sum(nums: list, target: int) -> list:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

    # Test
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([3,2,4], 6) == [1,2]
    print("✓ Two Sum tests passed!")


def practice_problem_3():
    """
    PRACTICE: Choose the Right Data Structure

    For each problem description, identify:
    - The best data structure(s) to use
    - The expected time complexity
    - The key pattern/technique

    1. "Remove duplicates from an array"
       → Data Structure: Set
       → Complexity: O(n)
       → Pattern: Hash-based deduplication

    2. "Find the next greater element for each element in array"
       → Data Structure: Stack (Monotonic Stack)
       → Complexity: O(n)
       → Pattern: Monotonic stack pattern

    3. "Find shortest path from A to B in unweighted graph"
       → Data Structure: Queue (BFS)
       → Complexity: O(V + E)
       → Pattern: BFS for shortest path

    4. "Find the kth largest element in array"
       → Data Structure: Heap (Min-Heap of size k)
       → Complexity: O(n log k)
       → Pattern: Top-K with heap

    5. "Check if string has valid balanced parentheses"
       → Data Structure: Stack
       → Complexity: O(n)
       → Pattern: Matching pairs with stack
    """
    print("✓ Pattern recognition practice complete!")


# ============================================================================
# PART 6: YOUR INTERVIEW PREPARATION CHECKLIST
# ============================================================================

"""
30-DAY INTERVIEW PREP ROADMAP
==============================

WEEK 1: FOUNDATIONS (Critical Data Structures)
-----------------------------------------------
Day 1-2: Arrays/Lists (Lesson 02)
        - Practice: Two pointers, sliding window
Day 3-4: Strings (Lesson 01)
        - Practice: Palindromes, anagrams, parsing
Day 5-6: Hash Maps/Sets (Lessons 04, 05)
        - Practice: Two sum, frequency counting
Day 7:   Review and mixed practice

WEEK 2: SEQUENTIAL STRUCTURES
------------------------------
Day 8-9:   Stacks (Lesson 06)
          - Practice: Balanced parentheses, monotonic stack
Day 10-11: Queues/Deques (Lessons 07, 08)
          - Practice: BFS, sliding window
Day 12-13: Linked Lists (Lesson 09)
          - Practice: Reverse, cycle detection
Day 14:    Review and mixed practice

WEEK 3: HIERARCHICAL STRUCTURES
--------------------------------
Day 15-17: Binary Trees (Lesson 11)
          - Practice: Traversals, BST, path problems
Day 18-19: Heaps (Lesson 10)
          - Practice: Top K, merge sorted, median
Day 20-21: Graphs (Lesson 12)
          - Practice: BFS/DFS, shortest path
Day 21:    Review and mixed practice

WEEK 4: ADVANCED + MOCK INTERVIEWS
-----------------------------------
Day 22-23: Tries (Lesson 13)
          - Practice: Prefix search, autocomplete
Day 24-25: Dynamic Programming patterns
Day 26-27: Mixed problem practice
Day 28-30: Mock interviews and review

DAILY ROUTINE
-------------
1. Review framework (10 min)
2. Learn/review data structure (30 min)
3. Solve 2-3 easy problems (45 min)
4. Solve 1 medium problem (30 min)
5. Review solutions and patterns (15 min)

Total: ~2.5 hours/day
"""


# ============================================================================
# RUN THE GUIDE
# ============================================================================

if __name__ == "__main__":
    print("="*70)
    print("CODING INTERVIEW PREPARATION GUIDE")
    print("="*70)
    print("\nThis guide has been loaded successfully!")
    print("\nREAD the content above carefully, then:")
    print("1. Practice applying the 7-Step Framework")
    print("2. Review the data structure frequency guide")
    print("3. Start with Week 1 of the 30-day roadmap")
    print("\nRun practice problems:")
    print("  practice_problem_1()  # Valid Palindrome")
    print("  practice_problem_2()  # Two Sum")
    print("  practice_problem_3()  # Pattern Recognition")
    print("\n" + "="*70)

    # Optionally run practice
    print("\nRunning practice problems...")
    practice_problem_1()
    practice_problem_2()
    practice_problem_3()
    print("\n✓ Guide ready! Start with Lesson 01_strings when ready.")
    print("="*70)
