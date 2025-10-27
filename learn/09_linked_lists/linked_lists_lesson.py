"""
INTERACTIVE LESSON: Linked Lists in Python

Linked Lists are linear data structures where elements are stored in nodes.
Each node contains data and a reference (link) to the next node.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_linked_lists.py
"""

# ============================================================================
# PART 1: WHAT ARE LINKED LISTS?
# ============================================================================
"""
Linked Lists store elements in separate nodes linked together.
- Each node contains: data + pointer to next node
- Types: Singly Linked, Doubly Linked, Circular
- No indexing: must traverse from head
- O(1) insertion/deletion at known position
- O(n) search and access by index
- Used in: implementing stacks/queues, hash table chaining, memory management
"""

# ============================================================================
# PART 2: BASIC LINKED LIST OPERATIONS
# ============================================================================

class ListNode:
    """Node for singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_basics_demo():
    """Demonstrates basic linked list operations."""
    # Creating nodes
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    # List: 1 -> 2 -> 3 -> None

    # Traversing
    current = head
    while current:
        print(current.val)
        current = current.next

    # Inserting at beginning
    new_head = ListNode(0, head)  # 0 -> 1 -> 2 -> 3

    # Inserting at end
    current = new_head
    while current.next:
        current = current.next
    current.next = ListNode(4)  # 0 -> 1 -> 2 -> 3 -> 4

    # Deleting a node (delete node with value 2)
    current = new_head
    while current.next and current.next.val != 2:
        current = current.next
    if current.next:
        current.next = current.next.next  # Skip node 2

    return new_head


# Helper functions
def create_linked_list(values: list) -> ListNode:
    """Create linked list from list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: ListNode) -> list:
    """Convert linked list to Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_reverse_linked_list(head: ListNode) -> ListNode:
    """
    Reverse a singly linked list.
    Classic interview question!

    Example:
        Input: 1 -> 2 -> 3 -> 4 -> None
        Output: 4 -> 3 -> 2 -> 1 -> None

    Hint: Use three pointers: prev, current, next
    """
    # TODO: Implement this function
    pass


def exercise_2_find_middle(head: ListNode) -> ListNode:
    """
    Find the middle node of a linked list.
    If two middle nodes, return the second one.

    Example:
        Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
        Output: Node with value 3

    Hint: Use slow and fast pointers (tortoise and hare)
    """
    # TODO: Implement this function
    pass


def exercise_3_detect_cycle(head: ListNode) -> bool:
    """
    Detect if linked list has a cycle.

    Example:
        1 -> 2 -> 3 -> 4
             ^         |
             |_________|
        Has cycle: True

    Hint: Use Floyd's cycle detection (slow/fast pointers)
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE LINKED LIST OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced linked list operations."""
    # Doubly linked list node
    class DListNode:
        def __init__(self, val=0, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    # Creating doubly linked list
    head = DListNode(1)
    second = DListNode(2)
    third = DListNode(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    # Can traverse both directions
    # Forward: 1 -> 2 -> 3
    # Backward: 3 <- 2 <- 1

    return head


def exercise_4_remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    Remove the nth node from the end of the list.

    Example:
        Input: 1 -> 2 -> 3 -> 4 -> 5, n = 2
        Output: 1 -> 2 -> 3 -> 5

    Hint: Use two pointers with n-node gap between them
    """
    # TODO: Implement this function
    pass


def exercise_5_merge_sorted_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists into one sorted list.

    Example:
        l1: 1 -> 2 -> 4
        l2: 1 -> 3 -> 4
        Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

    Hint: Use dummy head, compare nodes from both lists
    """
    # TODO: Implement this function
    pass


def exercise_6_palindrome_linked_list(head: ListNode) -> bool:
    """
    Check if linked list is a palindrome.

    Example:
        1 -> 2 -> 2 -> 1 -> None: True
        1 -> 2 -> 3 -> None: False

    Hint: Find middle, reverse second half, compare with first half
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED LINKED LIST TECHNIQUES
# ============================================================================

def exercise_7_reorder_list(head: ListNode) -> ListNode:
    """
    Reorder list: L0 → L1 → … → Ln-1 → Ln to
                  L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

    Example:
        Input: 1 -> 2 -> 3 -> 4 -> 5
        Output: 1 -> 5 -> 2 -> 4 -> 3

    Hint: Find middle, reverse second half, merge alternately
    """
    # TODO: Implement this function
    pass


def exercise_8_copy_random_list(head) -> 'Node':
    """
    Deep copy a linked list where each node has a random pointer.
    Node class: val, next, random

    Example:
        Input: 1 -> 2 -> 3 (with random pointers)
        Output: Deep copy of the entire structure

    Hint: Create new nodes interleaved, copy random pointers, then separate
    """
    # TODO: Implement this function
    # Note: Assume Node class has val, next, random attributes
    pass


def exercise_9_reverse_k_group(head: ListNode, k: int) -> ListNode:
    """
    Reverse nodes in k-group. If nodes < k at end, keep as is.

    Example:
        Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
        Output: 2 -> 1 -> 4 -> 3 -> 5

        Input: 1 -> 2 -> 3 -> 4 -> 5, k = 3
        Output: 3 -> 2 -> 1 -> 4 -> 5

    Hint: Count k nodes, reverse them, recursively process rest
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Linked Lists:

1. MEMORY MANAGEMENT
   - Operating system free memory blocks
   - Garbage collection algorithms
   - Memory allocators (malloc/free)
   Example: Linux kernel's free page list

2. HASH TABLE CHAINING
   - Collision resolution in hash tables
   - Each bucket is a linked list
   - Dynamic growth without rehashing bucket
   Example: Python dict implementation (uses linked lists in buckets)

3. UNDO FUNCTIONALITY
   - Doubly linked list for undo/redo
   - Navigate forward/backward through history
   - Insert/delete operations
   Example: Photoshop's history panel

4. MUSIC/VIDEO PLAYLISTS
   - Next/previous song navigation
   - Circular linked list for repeat
   - Insert/delete songs efficiently
   Example: Spotify playlist implementation

5. BROWSER CACHE (LRU)
   - Doubly linked list + hash map
   - Move recently used to front
   - Remove least recently used from back
   Example: Browser page caching

6. BLOCKCHAIN
   - Each block points to previous block
   - Immutable chain structure
   - Cryptographic linking
   Example: Bitcoin blockchain
"""

def exercise_10_add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Add two numbers represented by linked lists (digits in reverse order).
    Common interview question!

    Example:
        l1: 2 -> 4 -> 3  (represents 342)
        l2: 5 -> 6 -> 4  (represents 465)
        Output: 7 -> 0 -> 8  (represents 807)

    Hint: Add digit by digit, track carry
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("LINKED LIST LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Reverse Linked List:")
    try:
        head = create_linked_list([1, 2, 3, 4])
        result = exercise_1_reverse_linked_list(head)
        assert linked_list_to_list(result) == [4, 3, 2, 1]
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Find Middle:")
    try:
        head = create_linked_list([1, 2, 3, 4, 5])
        result = exercise_2_find_middle(head)
        assert result.val == 3
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Detect Cycle:")
    try:
        head = create_linked_list([1, 2, 3, 4])
        # Create cycle: 4 -> 2
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = head.next

        assert exercise_3_detect_cycle(head) == True

        # Test without cycle
        head2 = create_linked_list([1, 2, 3])
        assert exercise_3_detect_cycle(head2) == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Remove Nth From End:")
    try:
        head = create_linked_list([1, 2, 3, 4, 5])
        result = exercise_4_remove_nth_from_end(head, 2)
        assert linked_list_to_list(result) == [1, 2, 3, 5]
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. Merge Sorted Lists:")
    try:
        l1 = create_linked_list([1, 2, 4])
        l2 = create_linked_list([1, 3, 4])
        result = exercise_5_merge_sorted_lists(l1, l2)
        assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Palindrome Linked List:")
    try:
        head1 = create_linked_list([1, 2, 2, 1])
        assert exercise_6_palindrome_linked_list(head1) == True

        head2 = create_linked_list([1, 2, 3])
        assert exercise_6_palindrome_linked_list(head2) == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Reorder List:")
    try:
        head = create_linked_list([1, 2, 3, 4, 5])
        result = exercise_7_reorder_list(head)
        assert linked_list_to_list(result) == [1, 5, 2, 4, 3]
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8 (skipped - complex setup needed)
    print("\n8. Copy Random List:")
    print("   ⚠ SKIPPED - Requires special Node class with random pointer")

    # Test exercise 9
    print("\n9. Reverse K Group:")
    try:
        head = create_linked_list([1, 2, 3, 4, 5])
        result = exercise_9_reverse_k_group(head, 2)
        assert linked_list_to_list(result) == [2, 1, 4, 3, 5]
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Add Two Numbers:")
    try:
        l1 = create_linked_list([2, 4, 3])
        l2 = create_linked_list([5, 6, 4])
        result = exercise_10_add_two_numbers(l1, l2)
        assert linked_list_to_list(result) == [7, 0, 8]
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
