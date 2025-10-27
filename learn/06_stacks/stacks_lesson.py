"""
INTERACTIVE LESSON: Stacks in Python

Stacks are LIFO (Last In, First Out) data structures - like a stack of plates.
The last item added is the first one removed.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_stacks.py
"""

# ============================================================================
# PART 1: WHAT ARE STACKS?
# ============================================================================
"""
Stacks follow the Last In, First Out (LIFO) principle.
- Think of a stack of plates: you add/remove from the top only
- Main operations: push (add to top), pop (remove from top), peek (view top)
- Python lists can be used as stacks
- O(1) time complexity for push and pop
- Used in: function call stacks, undo/redo, expression evaluation, backtracking
"""

# ============================================================================
# PART 2: BASIC STACK OPERATIONS
# ============================================================================

def stack_basics_demo():
    """Demonstrates basic stack operations using Python list."""
    # Creating a stack (using list)
    stack = []

    # Push (add to top)
    stack.append(1)  # Stack: [1]
    stack.append(2)  # Stack: [1, 2]
    stack.append(3)  # Stack: [1, 2, 3]

    # Peek (view top without removing)
    if stack:
        top = stack[-1]  # 3

    # Pop (remove from top)
    removed = stack.pop()  # Returns 3, Stack: [1, 2]

    # Check if empty
    is_empty = len(stack) == 0  # False

    # Size
    size = len(stack)  # 2

    return stack


class Stack:
    """Simple stack implementation using list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Add item to top of stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return top item."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return top item without removing."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Check if stack is empty."""
        return len(self._items) == 0

    def size(self):
        """Return number of items in stack."""
        return len(self._items)


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_reverse_string_with_stack(s: str) -> str:
    """
    Reverse a string using a stack.

    Example:
        reverse_string_with_stack("hello") -> "olleh"
        reverse_string_with_stack("Python") -> "nohtyP"

    Hint: Push all characters onto stack, then pop them all
    """
    # TODO: Implement this function
    pass


def exercise_2_balanced_parentheses(s: str) -> bool:
    """
    Check if parentheses in a string are balanced.
    Classic stack problem!

    Example:
        balanced_parentheses("()") -> True
        balanced_parentheses("(())") -> True
        balanced_parentheses("(()") -> False
        balanced_parentheses("())") -> False

    Hint: Push '(' onto stack, pop when you see ')'. Stack should be empty at end.
    """
    # TODO: Implement this function
    pass


def exercise_3_stack_min(operations: list) -> list:
    """
    Implement a stack that supports push, pop, and getting the minimum in O(1).
    Operations are tuples: ("push", value), ("pop",), ("min",)
    Return list of results for "min" and "pop" operations.

    Example:
        stack_min([("push", 5), ("push", 3), ("min",), ("push", 7), ("min",)])
        -> [3, 3]

    Hint: Maintain a separate stack that tracks minimums
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE STACK OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced stack usage."""
    # Multiple stacks for different purposes
    undo_stack = []
    redo_stack = []

    # Simulating undo/redo
    def do_action(action):
        undo_stack.append(action)
        redo_stack.clear()  # Clear redo on new action

    def undo():
        if undo_stack:
            action = undo_stack.pop()
            redo_stack.append(action)

    def redo():
        if redo_stack:
            action = redo_stack.pop()
            undo_stack.append(action)

    # Two-stack algorithm for queue
    stack1 = [1, 2, 3]
    stack2 = []

    # Transfer elements
    while stack1:
        stack2.append(stack1.pop())
    # stack2 now has elements in reverse: [3, 2, 1]

    return undo_stack, redo_stack


def exercise_4_evaluate_postfix(expression: str) -> int:
    """
    Evaluate a postfix (Reverse Polish Notation) expression.
    Operators are separated by spaces.

    Example:
        evaluate_postfix("3 4 +") -> 7
        evaluate_postfix("5 1 2 + 4 * + 3 -") -> 14
        # This is: 5 + ((1 + 2) * 4) - 3 = 14

    Hint: Push numbers onto stack. When you see operator, pop two operands,
    compute result, push back onto stack.
    """
    # TODO: Implement this function
    pass


def exercise_5_next_greater_element(nums: list) -> list:
    """
    For each element, find the next greater element to its right.
    Return -1 if no greater element exists.

    Example:
        next_greater_element([4, 5, 2, 10, 8]) -> [5, 10, 10, -1, -1]
        next_greater_element([1, 2, 3, 4]) -> [2, 3, 4, -1]

    Hint: Use stack to track indices of elements waiting for their next greater
    """
    # TODO: Implement this function
    pass


def exercise_6_valid_brackets(s: str) -> bool:
    """
    Check if brackets are valid: (), {}, []
    Must be closed in correct order.

    Example:
        valid_brackets("()[]{}") -> True
        valid_brackets("([)]") -> False (incorrect order)
        valid_brackets("{[]}") -> True

    Hint: Use stack, push opening brackets, pop and match with closing brackets
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED STACK TECHNIQUES
# ============================================================================

def exercise_7_simplify_path(path: str) -> str:
    """
    Simplify a Unix file path.
    Rules: '.' = current dir, '..' = parent dir, '//' = single '/'

    Example:
        simplify_path("/home/") -> "/home"
        simplify_path("/../") -> "/"
        simplify_path("/home//foo/") -> "/home/foo"
        simplify_path("/a/./b/../../c/") -> "/c"

    Hint: Split by '/', use stack to track valid directories
    """
    # TODO: Implement this function
    pass


def exercise_8_daily_temperatures(temperatures: list) -> list:
    """
    Given daily temperatures, return how many days until a warmer temperature.
    Return 0 if no warmer day exists.

    Example:
        daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
        -> [1, 1, 4, 2, 1, 1, 0, 0]
        # 73->74 is 1 day, 74->75 is 1 day, 75->76 is 4 days, etc.

    Hint: Use stack to track indices of days waiting for warmer temperature
    """
    # TODO: Implement this function
    pass


def exercise_9_decode_string(s: str) -> str:
    """
    Decode a string where k[encoded_string] means repeat encoded_string k times.

    Example:
        decode_string("3[a]2[bc]") -> "aaabcbc"
        decode_string("3[a2[c]]") -> "accaccacc"
        decode_string("2[abc]3[cd]ef") -> "abcabccdcdcdef"

    Hint: Use stack to handle nested brackets and repetition counts
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Stacks:

1. BROWSER HISTORY
   - Back button uses stack of visited pages
   - Forward button uses another stack
   - Each page visit pushes to back stack, clears forward stack
   Example: Chrome's navigation history

2. UNDO/REDO FUNCTIONALITY
   - Text editors, graphic design tools
   - Each action pushed to undo stack
   - Undo pops from undo stack, pushes to redo stack
   Example: Ctrl+Z / Ctrl+Y in any editor

3. FUNCTION CALL STACK
   - Programming language runtime
   - Each function call pushes stack frame
   - Return pops stack frame
   Example: Recursion, debugging stack traces

4. EXPRESSION EVALUATION
   - Compilers and interpreters
   - Parsing mathematical expressions
   - Converting infix to postfix notation
   Example: Calculator applications

5. SYNTAX PARSING
   - Code editors and IDEs
   - Checking bracket matching
   - Parsing HTML/XML tags
   Example: VSCode bracket colorization

6. BACKTRACKING ALGORITHMS
   - Maze solving
   - Game AI (chess, puzzles)
   - Depth-first search
   Example: Sudoku solver, path finding
"""

def exercise_10_asteroid_collision(asteroids: list) -> list:
    """
    Asteroids moving right (+) or left (-) collide and explode.
    Larger asteroid survives, same size both explode.
    Common interview question!

    Example:
        asteroid_collision([5, 10, -5]) -> [5, 10]
        # 10 and -5 collide, 10 survives

        asteroid_collision([8, -8]) -> []
        # Equal size, both explode

        asteroid_collision([10, 2, -5]) -> [10]
        # 2 and -5 collide, -5 survives; then 10 and -5 collide, 10 survives

    Hint: Use stack, push positive asteroids. When negative comes,
    check collisions with stack top.
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("STACK LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Reverse String with Stack:")
    try:
        assert exercise_1_reverse_string_with_stack("hello") == "olleh"
        assert exercise_1_reverse_string_with_stack("Python") == "nohtyP"
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Balanced Parentheses:")
    try:
        assert exercise_2_balanced_parentheses("()") == True
        assert exercise_2_balanced_parentheses("(())") == True
        assert exercise_2_balanced_parentheses("(()") == False
        assert exercise_2_balanced_parentheses("())") == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Stack Min:")
    try:
        result = exercise_3_stack_min([("push", 5), ("push", 3), ("min",), ("push", 7), ("min",)])
        assert result == [3, 3]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Evaluate Postfix:")
    try:
        assert exercise_4_evaluate_postfix("3 4 +") == 7
        assert exercise_4_evaluate_postfix("5 1 2 + 4 * + 3 -") == 14
        print("   ✓ PASSED")
    except (AssertionError, TypeError, ValueError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. Next Greater Element:")
    try:
        assert exercise_5_next_greater_element([4, 5, 2, 10, 8]) == [5, 10, 10, -1, -1]
        assert exercise_5_next_greater_element([1, 2, 3, 4]) == [2, 3, 4, -1]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Valid Brackets:")
    try:
        assert exercise_6_valid_brackets("()[]{}") == True
        assert exercise_6_valid_brackets("([)]") == False
        assert exercise_6_valid_brackets("{[]}") == True
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Simplify Path:")
    try:
        assert exercise_7_simplify_path("/home/") == "/home"
        assert exercise_7_simplify_path("/../") == "/"
        assert exercise_7_simplify_path("/a/./b/../../c/") == "/c"
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Daily Temperatures:")
    try:
        result = exercise_8_daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
        assert result == [1, 1, 4, 2, 1, 1, 0, 0]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. Decode String:")
    try:
        assert exercise_9_decode_string("3[a]2[bc]") == "aaabcbc"
        assert exercise_9_decode_string("3[a2[c]]") == "accaccacc"
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Asteroid Collision:")
    try:
        assert exercise_10_asteroid_collision([5, 10, -5]) == [5, 10]
        assert exercise_10_asteroid_collision([8, -8]) == []
        assert exercise_10_asteroid_collision([10, 2, -5]) == [10]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
