# Coding Interview Quick Reference Cheat Sheet

Print this page and keep it handy while practicing!

## 7-Step Framework

| Step | Time | Action |
|------|------|--------|
| 1. **UNDERSTAND** | 2-3 min | Define inputs, outputs, constraints, edge cases |
| 2. **EXAMPLES** | 2-3 min | Work through 2-3 concrete test cases |
| 3. **PATTERN** | 2-3 min | Identify algorithm/data structure |
| 4. **BREAKDOWN** | 3-5 min | Write pseudocode, plan approach |
| 5. **COMPLEXITY** | 1-2 min | Analyze time/space, consider optimizations |
| 6. **CODE** | 10-15 min | Implement solution with clean code |
| 7. **TEST** | 3-5 min | Verify with examples and edge cases |

---

## Problem Keywords → Data Structure

| When Problem Says... | Consider Using... |
|---------------------|-------------------|
| "Find pair/two elements that..." | **Hash Map** or **Two Pointers** |
| "Count frequency of..." | **Hash Map** (Counter) |
| "Remove duplicates" | **Set** or **Hash Map** |
| "Check if exists" | **Set** (O(1) lookup) |
| "Valid parentheses/brackets" | **Stack** |
| "Next greater/smaller element" | **Stack** (monotonic) |
| "Undo/reverse operations" | **Stack** |
| "Level order traversal" | **Queue** (BFS) |
| "Shortest path (unweighted)" | **Queue** (BFS) |
| "Sliding window maximum" | **Deque** |
| "Top K elements" | **Heap** (priority queue) |
| "Kth largest/smallest" | **Heap** |
| "Median of stream" | **Two Heaps** (max + min) |
| "Merge K sorted lists" | **Heap** |
| "Prefix matching/autocomplete" | **Trie** |
| "Tree/graph traversal" | **DFS** or **BFS** |
| "Shortest path (weighted)" | **Dijkstra's** (Heap + Graph) |
| "Cycle detection" | **Fast & Slow Pointers** or **DFS** |
| "In-place array manipulation" | **Two Pointers** |

---

## Common Algorithm Patterns

| Pattern | When to Use | Example Problems |
|---------|-------------|------------------|
| **Two Pointers** | Sorted array, pairs, triplets | Two Sum (sorted), Remove duplicates |
| **Sliding Window** | Subarray/substring conditions | Max sum subarray, Longest substring |
| **Fast & Slow Pointers** | Linked list cycle, middle | Detect cycle, Find middle |
| **Binary Search** | Sorted data, search space | Find element, First bad version |
| **BFS** | Shortest path, level order | Tree levels, Min steps |
| **DFS** | All paths, backtracking | Path sum, Generate combinations |
| **Backtracking** | Permutations, combinations | N-Queens, Subsets |
| **Dynamic Programming** | Optimization, counting ways | Fibonacci, Longest subsequence |
| **Greedy** | Local optimal → global optimal | Job scheduling, Jump game |
| **Monotonic Stack** | Next greater/smaller | Daily temperatures, Stock span |

---

## Data Structure Time Complexities

| Operation | Array | Hash Map | Set | Stack | Queue | Heap | Binary Search Tree |
|-----------|-------|----------|-----|-------|-------|------|--------------------|
| Access | O(1) | O(1) avg | - | - | - | - | O(log n) |
| Search | O(n) | O(1) avg | O(1) avg | O(n) | O(n) | O(n) | O(log n) |
| Insert | O(n) | O(1) avg | O(1) avg | O(1) | O(1) | O(log n) | O(log n) |
| Delete | O(n) | O(1) avg | O(1) avg | O(1) | O(1) | O(log n) | O(log n) |

---

## Edge Cases Checklist

### Arrays/Lists
- [ ] Empty array `[]`
- [ ] Single element `[1]`
- [ ] All same elements `[5, 5, 5]`
- [ ] Sorted vs unsorted
- [ ] Negative numbers
- [ ] Duplicates

### Strings
- [ ] Empty string `""`
- [ ] Single character `"a"`
- [ ] All same characters `"aaaa"`
- [ ] Special characters
- [ ] Case sensitivity
- [ ] Spaces/whitespace

### Linked Lists
- [ ] Null/None head
- [ ] Single node
- [ ] Two nodes
- [ ] Circular list
- [ ] Odd vs even length

### Trees
- [ ] Null/None root
- [ ] Single node
- [ ] Only left children
- [ ] Only right children
- [ ] Balanced vs unbalanced
- [ ] Complete binary tree

### Graphs
- [ ] Empty graph
- [ ] Single node
- [ ] Disconnected components
- [ ] Cycles vs acyclic
- [ ] Self-loops

### Numbers
- [ ] Zero
- [ ] Negative numbers
- [ ] Integer overflow
- [ ] Odd vs even
- [ ] Min/max integer values

---

## Optimization Strategies

| From | To | Method |
|------|-----|--------|
| O(n²) | O(n log n) | Sorting |
| O(n²) | O(n) | Hash Map |
| O(n) space | O(1) space | Two Pointers, Swap in place |
| Recursion | Iteration | Use stack/queue |
| Repeated calculations | O(1) lookup | Memoization, DP |
| Find max/min repeatedly | O(log n) | Heap |

---

## Interview Communication Tips

### Things to Say Out Loud
✅ "Let me make sure I understand the problem..."
✅ "Let me work through an example..."
✅ "I'm thinking about using [data structure] because..."
✅ "The time complexity would be O(n) because..."
✅ "Let me test with an edge case..."
✅ "Could I optimize this by..."

### Questions to Ask
❓ "Are there any constraints on time/space complexity?"
❓ "Can I assume the input is [sorted/non-negative/etc]?"
❓ "What should I return if there's no solution?"
❓ "Are there memory constraints?"
❓ "Can I modify the input array?"

---

## Quick Syntax Reminders (Python)

```python
# Hash Map
seen = {}
seen[key] = value
if key in seen: ...

# Set
unique = set()
unique.add(item)
if item in unique: ...

# Stack
stack = []
stack.append(item)  # push
item = stack.pop()  # pop

# Queue
from collections import deque
queue = deque()
queue.append(item)  # enqueue
item = queue.popleft()  # dequeue

# Heap
import heapq
heap = []
heapq.heappush(heap, item)
item = heapq.heappop(heap)

# Two Pointers
left, right = 0, len(arr) - 1
while left < right:
    # process
    left += 1
    right -= 1

# Sliding Window
window_start = 0
for window_end in range(len(arr)):
    # expand window
    while condition:
        # shrink window
        window_start += 1
```

---

## Time/Space Complexity Ranking

**Time Complexity** (fastest to slowest):
- O(1) - Constant
- O(log n) - Logarithmic
- O(n) - Linear ← **Target for most problems**
- O(n log n) - Linearithmic (sorting)
- O(n²) - Quadratic (nested loops)
- O(2ⁿ) - Exponential
- O(n!) - Factorial

**Space Complexity** (best to worst):
- O(1) - Constant ← **Best**
- O(log n) - Logarithmic (recursion depth)
- O(n) - Linear ← **Acceptable**
- O(n²) - Quadratic (2D arrays)

---

## The Golden Rules

1. **Understand first, code later** (Steps 1-5 before coding)
2. **Brute force is okay** (optimize after it works)
3. **Think out loud** (interviewer wants to hear your thought process)
4. **Test before you say "done"** (always verify)
5. **Ask questions** (clarify assumptions)
6. **Hash maps solve 50% of problems** (seriously!)
7. **Draw it out** (visualize the problem)
8. **Time yourself** (practice under pressure)

---

**Keep this sheet visible while practicing!**
**Print it, screenshot it, or keep it on a second monitor.**

Good luck! 🚀
