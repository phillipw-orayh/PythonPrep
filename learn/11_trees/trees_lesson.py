"""
INTERACTIVE LESSON: Trees in Python

Trees are hierarchical data structures with nodes connected by edges.
Each node has a value and references to child nodes.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_trees.py
"""

# ============================================================================
# PART 1: WHAT ARE TREES?
# ============================================================================
"""
Trees are hierarchical structures with a root and child nodes.
- Root: top node with no parent
- Leaf: node with no children
- Binary Tree: each node has at most 2 children
- Binary Search Tree (BST): left < parent < right
- Height: longest path from root to leaf
- Used in: file systems, databases, compilers, game AI, decision trees
"""

# ============================================================================
# PART 2: BASIC TREE OPERATIONS
# ============================================================================

class TreeNode:
    """Node for binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_basics_demo():
    """Demonstrates basic tree operations."""
    # Creating a tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Traversals
    def inorder(node):
        """Left -> Root -> Right"""
        if node:
            inorder(node.left)
            print(node.val)
            inorder(node.right)

    def preorder(node):
        """Root -> Left -> Right"""
        if node:
            print(node.val)
            preorder(node.left)
            preorder(node.right)

    def postorder(node):
        """Left -> Right -> Root"""
        if node:
            postorder(node.left)
            postorder(node.right)
            print(node.val)

    # Level-order (BFS)
    from collections import deque
    def levelorder(root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    return root


# Helper functions
def create_tree(values: list) -> TreeNode:
    """Create binary tree from level-order list (None for missing nodes)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_max_depth(root: TreeNode) -> int:
    """
    Find the maximum depth (height) of a binary tree.

    Example:
        Tree:     3
                 / \
                9  20
                   / \
                  15  7
        max_depth(root) -> 3

    Hint: Use recursion, depth = 1 + max(left_depth, right_depth)
    """
    # TODO: Implement this function
    pass


def exercise_2_invert_tree(root: TreeNode) -> TreeNode:
    """
    Invert a binary tree (mirror it).

    Example:
        Input:      4           Output:     4
                   / \                     / \
                  2   7                   7   2
                 / \ / \                 / \ / \
                1  3 6  9               9  6 3  1

    Hint: Swap left and right children recursively
    """
    # TODO: Implement this function
    pass


def exercise_3_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    Check if two binary trees are identical.

    Example:
        p:  1       q:  1
           / \         / \
          2   3       2   3
        same_tree(p, q) -> True

    Hint: Recursively compare values and subtrees
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE TREE OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced tree operations."""
    # Binary Search Tree (BST)
    class BST:
        def __init__(self):
            self.root = None

        def insert(self, val):
            """Insert value maintaining BST property."""
            if not self.root:
                self.root = TreeNode(val)
            else:
                self._insert_helper(self.root, val)

        def _insert_helper(self, node, val):
            if val < node.val:
                if node.left:
                    self._insert_helper(node.left, val)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    self._insert_helper(node.right, val)
                else:
                    node.right = TreeNode(val)

        def search(self, val):
            """Search for value in BST."""
            return self._search_helper(self.root, val)

        def _search_helper(self, node, val):
            if not node:
                return False
            if val == node.val:
                return True
            elif val < node.val:
                return self._search_helper(node.left, val)
            else:
                return self._search_helper(node.right, val)

    return BST


def exercise_4_level_order_traversal(root: TreeNode) -> list:
    """
    Return level-order traversal as list of lists (each level separately).

    Example:
        Tree:     3
                 / \
                9  20
                   / \
                  15  7
        Output: [[3], [9, 20], [15, 7]]

    Hint: Use queue (BFS), track level size
    """
    # TODO: Implement this function
    pass


def exercise_5_is_valid_bst(root: TreeNode) -> bool:
    """
    Validate if tree is a valid Binary Search Tree.

    Example:
        Tree:     5           Tree:     5
                 / \                   / \
                1   8                 1   4
                   / \                   / \
                  6   9                 3   6
        Valid BST: True      Valid BST: False (4 < 5)

    Hint: Check each node's value is within valid range (min, max)
    """
    # TODO: Implement this function
    pass


def exercise_6_path_sum(root: TreeNode, target: int) -> bool:
    """
    Check if there's a root-to-leaf path with sum equal to target.

    Example:
        Tree:     5
                 / \
                4   8
               /   / \
              11  13  4
             / \       \
            7   2       1
        path_sum(root, 22) -> True (5->4->11->2)

    Hint: Recursively subtract node value from target
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED TREE TECHNIQUES
# ============================================================================

def exercise_7_lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find lowest common ancestor of two nodes in a binary tree.

    Example:
        Tree:     3
                 / \
                5   1
               / \
              6   2
        LCA(6, 2) -> 5
        LCA(5, 1) -> 3

    Hint: If p and q are in different subtrees, current node is LCA
    """
    # TODO: Implement this function
    pass


def exercise_8_serialize_deserialize(root: TreeNode) -> str:
    """
    Serialize a binary tree to a string and deserialize back.
    Return the serialized string.

    Example:
        Tree:  1
              / \
             2   3
                / \
               4   5
        serialize(root) -> "1,2,None,None,3,4,None,None,5,None,None"

    Hint: Use preorder traversal with null markers
    """
    # TODO: Implement this function
    pass


def exercise_9_max_path_sum(root: TreeNode) -> int:
    """
    Find maximum path sum in a binary tree (any node to any node).
    Hard problem!

    Example:
        Tree:    -10
                 / \
                9  20
                   / \
                  15  7
        max_path_sum(root) -> 42 (15->20->7)

    Hint: At each node, consider path through it connecting left and right
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Trees:

1. FILE SYSTEMS
   - Directory structure (folders and files)
   - Hierarchical organization
   - Path navigation
   Example: Unix/Windows file system tree

2. DATABASES
   - B-trees and B+ trees for indexing
   - Fast search, insert, delete
   - Range queries
   Example: MySQL/PostgreSQL indexes

3. COMPILERS
   - Abstract Syntax Trees (AST)
   - Expression parsing
   - Code optimization
   Example: Python/Java compiler parsing

4. NETWORKING
   - Routing tables (prefix trees)
   - Domain Name System (DNS)
   - Decision trees for packet routing
   Example: Internet routing protocols

5. ARTIFICIAL INTELLIGENCE
   - Decision trees for ML
   - Game trees (chess, Go)
   - Minimax algorithm
   Example: Chess engines, random forests

6. HTML/XML PARSING
   - DOM (Document Object Model)
   - Nested tag structure
   - Tree traversal for rendering
   Example: Web browsers parsing HTML
"""

def exercise_10_binary_tree_cameras(root: TreeNode) -> int:
    """
    Place minimum cameras to monitor all nodes.
    Camera at node monitors itself, parent, and children.
    Challenging problem!

    Example:
        Tree:    0
                / \
               0   0
                \
                 0
                  \
                   0
        Output: 1 (camera at root's right child)

    Hint: Use postorder traversal with states (0=needs cover, 1=has camera, 2=covered)
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("TREE LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Max Depth:")
    try:
        root = create_tree([3, 9, 20, None, None, 15, 7])
        assert exercise_1_max_depth(root) == 3
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Invert Tree:")
    try:
        root = create_tree([4, 2, 7, 1, 3, 6, 9])
        result = exercise_2_invert_tree(root)
        assert result.left.val == 7 and result.right.val == 2
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Same Tree:")
    try:
        p = create_tree([1, 2, 3])
        q = create_tree([1, 2, 3])
        assert exercise_3_same_tree(p, q) == True

        p2 = create_tree([1, 2])
        q2 = create_tree([1, None, 2])
        assert exercise_3_same_tree(p2, q2) == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Level Order Traversal:")
    try:
        root = create_tree([3, 9, 20, None, None, 15, 7])
        result = exercise_4_level_order_traversal(root)
        assert result == [[3], [9, 20], [15, 7]]
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. Is Valid BST:")
    try:
        root1 = create_tree([2, 1, 3])
        assert exercise_5_is_valid_bst(root1) == True

        root2 = create_tree([5, 1, 4, None, None, 3, 6])
        assert exercise_5_is_valid_bst(root2) == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Path Sum:")
    try:
        root = create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        assert exercise_6_path_sum(root, 22) == True
        assert exercise_6_path_sum(root, 100) == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Lowest Common Ancestor:")
    try:
        root = create_tree([3, 5, 1, 6, 2, 0, 8])
        p = root.left  # 5
        q = root.left.right  # 2
        result = exercise_7_lowest_common_ancestor(root, p, q)
        assert result.val == 5
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Serialize Tree:")
    try:
        root = create_tree([1, 2, 3, None, None, 4, 5])
        serialized = exercise_8_serialize_deserialize(root)
        assert isinstance(serialized, str) and len(serialized) > 0
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. Max Path Sum:")
    try:
        root = create_tree([-10, 9, 20, None, None, 15, 7])
        result = exercise_9_max_path_sum(root)
        assert result == 42
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Binary Tree Cameras:")
    try:
        root = create_tree([0, 0, None, 0, 0])
        result = exercise_10_binary_tree_cameras(root)
        assert result == 1
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
