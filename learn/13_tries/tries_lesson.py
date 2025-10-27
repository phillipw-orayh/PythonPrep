"""
INTERACTIVE LESSON: Tries (Prefix Trees) in Python

Tries are tree-based data structures for efficient string operations.
Each node represents a character, paths represent strings.

Complete the exercises below by implementing the functions.
Run this file with: python lesson.py
Check your answers with: python answers/check_tries.py
"""

# ============================================================================
# PART 1: WHAT ARE TRIES?
# ============================================================================
"""
Tries (Prefix Trees) store strings character by character.
- Each node has children for possible next characters
- Paths from root to node spell prefixes
- Leaf nodes (or marked nodes) represent complete words
- O(m) for insert/search where m = string length
- Space-efficient for common prefixes
- Used in: autocomplete, spell check, IP routing, genome analysis
"""

# ============================================================================
# PART 2: BASIC TRIE OPERATIONS
# ============================================================================

class TrieNode:
    """Node in a Trie."""
    def __init__(self):
        self.children = {}  # character -> TrieNode
        self.is_end_of_word = False


class Trie:
    """Basic Trie implementation."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Search for exact word in trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Check if any word in trie starts with prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def trie_basics_demo():
    """Demonstrates basic trie operations."""
    trie = Trie()

    # Insert words
    trie.insert("apple")
    trie.insert("app")
    trie.insert("application")

    # Search
    print(trie.search("app"))  # True
    print(trie.search("appl"))  # False (not a complete word)

    # Prefix search
    print(trie.starts_with("app"))  # True
    print(trie.starts_with("banana"))  # False

    # Trie structure for "app", "apple":
    #       root
    #        |
    #        a
    #        |
    #        p
    #        |
    #        p (word ends here: "app")
    #        |
    #        l
    #        |
    #        e (word ends here: "apple")

    return trie


# ============================================================================
# PART 3: SIMPLE EXERCISES - Fill in the implementations
# ============================================================================

def exercise_1_implement_trie_class() -> Trie:
    """
    Implement a Trie class with insert, search, and starts_with methods.
    This is already provided above, but make sure you understand it!

    Return a Trie instance with "apple", "app", "banana" inserted.

    Hint: Use the Trie class above
    """
    # TODO: Implement this function
    pass


def exercise_2_longest_common_prefix(words: list) -> str:
    """
    Find the longest common prefix among a list of words using a Trie.

    Example:
        longest_common_prefix(["flower","flow","flight"]) -> "fl"
        longest_common_prefix(["dog","racecar","car"]) -> ""

    Hint: Insert all words, traverse from root while only one child exists
    """
    # TODO: Implement this function
    pass


def exercise_3_word_search_board(board: list, word: str) -> bool:
    """
    Search for word in 2D board. Word can be constructed from adjacent cells.
    Same cell cannot be used twice.

    Example:
        board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]
        word_search_board(board, "ABCCED") -> True
        word_search_board(board, "ABCB") -> False

    Hint: Depth First Search (DFS) with backtracking from each cell
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 4: INTERMEDIATE TRIE OPERATIONS
# ============================================================================

def intermediate_demo():
    """Demonstrates more advanced trie operations."""
    # Trie with word count
    class TrieWithCount:
        def __init__(self):
            self.root = TrieNode()

        def insert(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                    node.children[char].count = 0
                node = node.children[char]
                if not hasattr(node, 'count'):
                    node.count = 0
                node.count += 1
            node.is_end_of_word = True

        def count_prefix(self, prefix):
            """Count words starting with prefix."""
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return 0
                node = node.children[char]
            return node.count if hasattr(node, 'count') else 0

    # Autocomplete
    class AutocompleteTrie:
        def __init__(self):
            self.root = TrieNode()

        def insert(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True

        def autocomplete(self, prefix):
            """Return all words starting with prefix."""
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return []
                node = node.children[char]

            # DFS to find all words
            results = []
            self._dfs(node, prefix, results)
            return results

        def _dfs(self, node, current, results):
            if node.is_end_of_word:
                results.append(current)
            for char, child in node.children.items():
                self._dfs(child, current + char, results)

    return TrieWithCount, AutocompleteTrie


def exercise_4_add_search_word_wildcards(words: list, pattern: str) -> bool:
    """
    Add words to trie, then search with '.' as wildcard (matches any char).

    Example:
        words = ["bad", "dad", "mad"]
        add_search_word_wildcards(words, "pad") -> False
        add_search_word_wildcards(words, ".ad") -> True
        add_search_word_wildcards(words, "b..") -> True

    Hint: For '.', try all possible children recursively
    """
    # TODO: Implement this function
    pass


def exercise_5_word_break(s: str, word_dict: list) -> bool:
    """
    Check if string can be segmented into words from dictionary.

    Example:
        word_break("leetcode", ["leet", "code"]) -> True
        word_break("applepenapple", ["apple", "pen"]) -> True
        word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) -> False

    Hint: Use Trie + DP or DFS with memoization
    """
    # TODO: Implement this function
    pass


def exercise_6_replace_words(dictionary: list, sentence: str) -> str:
    """
    Replace words in sentence with their shortest root from dictionary.

    Example:
        dictionary = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        Output: "the cat was rat by the bat"

    Hint: Build trie from dictionary, for each word find shortest prefix
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 5: ADVANCED TRIE TECHNIQUES
# ============================================================================

def exercise_7_word_search_ii(board: list, words: list) -> list:
    """
    Find all words from list that exist in 2D board.
    Very challenging problem!

    Example:
        board = [
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
        ]
        words = ["oath","pea","eat","rain"]
        Output: ["oath","eat"]

    Hint: Build trie from words, DFS from each cell following trie paths
    """
    # TODO: Implement this function
    pass


def exercise_8_stream_checker(words: list, queries: list) -> list:
    """
    Check if any suffix of query stream matches a word.
    queries[i] adds a letter to stream.

    Example:
        words = ["cd","f","kl"]
        queries = ['a','b','c','d','e','f']
        Output: [False,False,False,True,False,True]
        # After 'd': stream is "abcd", suffix "cd" is in words
        # After 'f': stream is "abcdef", suffix "f" is in words

    Hint: Build trie with reversed words, check suffixes
    """
    # TODO: Implement this function
    pass


def exercise_9_palindrome_pairs(words: list) -> list:
    """
    Find all pairs of words that form palindromes when concatenated.
    Hard problem!

    Example:
        words = ["bat","tab","cat"]
        Output: [[0,1],[1,0]]  # "battab" and "tabbat"

    Hint: Build trie, for each word check if reverse forms palindrome
    """
    # TODO: Implement this function
    pass


# ============================================================================
# PART 6: INDUSTRY USE CASES
# ============================================================================
"""
Common Industry Applications of Tries:

1. AUTOCOMPLETE
   - Search engines
   - Text editors
   - Command-line interfaces
   Example: Google Search suggestions

2. SPELL CHECKING
   - Word processors
   - Code editors
   - Email clients
   Example: Microsoft Word red underlines

3. IP ROUTING
   - Network routers
   - Longest prefix matching
   - Fast packet forwarding
   Example: Internet routing tables

4. CONTACT LISTS
   - Phone apps
   - Email clients
   - Prefix search for names
   Example: iPhone contact search

5. BIOINFORMATICS
   - DNA sequence analysis
   - Genome assembly
   - Pattern matching
   Example: BLAST algorithm

6. TEXT INDEXING
   - Full-text search
   - Document retrieval
   - Suffix trees
   Example: Elasticsearch, database indexes
"""

def exercise_10_design_search_autocomplete(sentences: list, times: list, query: str) -> list:
    """
    Design autocomplete system that returns top 3 hot sentences.
    sentences[i] was typed times[i] times historically.
    Query is built character by character.

    Example:
        sentences = ["i love you", "island", "iroman", "i love leetcode"]
        times = [5, 3, 2, 2]
        query = "i"
        Output: ["i love you", "island", "i love leetcode"]
        # Top 3 by frequency

    Hint: Trie + priority queue, sort by frequency then lexicographically
    """
    # TODO: Implement this function
    pass


# ============================================================================
# TEST CASES - Do not modify
# ============================================================================

def run_tests():
    """Run all test cases."""
    print("="*60)
    print("TRIE LESSONS - TEST RESULTS")
    print("="*60)

    # Test exercise 1
    print("\n1. Implement Trie Class:")
    try:
        trie = exercise_1_implement_trie_class()
        assert trie.search("apple") == True
        assert trie.search("app") == True
        assert trie.starts_with("ban") == True
        print("   ✓ PASSED")
    except (AssertionError, TypeError, AttributeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 2
    print("\n2. Longest Common Prefix:")
    try:
        assert exercise_2_longest_common_prefix(["flower","flow","flight"]) == "fl"
        assert exercise_2_longest_common_prefix(["dog","racecar","car"]) == ""
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 3
    print("\n3. Word Search Board:")
    try:
        board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
        assert exercise_3_word_search_board(board, "ABCCED") == True
        assert exercise_3_word_search_board(board, "ABCB") == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 4
    print("\n4. Add Search Word Wildcards:")
    try:
        assert exercise_4_add_search_word_wildcards(["bad","dad","mad"], ".ad") == True
        assert exercise_4_add_search_word_wildcards(["bad","dad","mad"], "pad") == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 5
    print("\n5. Word Break:")
    try:
        assert exercise_5_word_break("leetcode", ["leet", "code"]) == True
        assert exercise_5_word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 6
    print("\n6. Replace Words:")
    try:
        result = exercise_6_replace_words(["cat", "bat", "rat"],
                                          "the cattle was rattled by the battery")
        assert result == "the cat was rat by the bat"
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 7
    print("\n7. Word Search II:")
    try:
        board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
        result = exercise_7_word_search_ii(board, ["oath","pea","eat","rain"])
        assert set(result) == {"oath", "eat"}
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 8
    print("\n8. Stream Checker:")
    try:
        result = exercise_8_stream_checker(["cd","f","kl"], ['a','b','c','d','e','f'])
        assert result == [False,False,False,True,False,True]
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 9
    print("\n9. Palindrome Pairs:")
    try:
        result = exercise_9_palindrome_pairs(["bat","tab","cat"])
        assert [0,1] in result and [1,0] in result
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    # Test exercise 10
    print("\n10. Design Search Autocomplete:")
    try:
        sentences = ["i love you", "island", "iroman", "i love leetcode"]
        times = [5, 3, 2, 2]
        result = exercise_10_design_search_autocomplete(sentences, times, "i")
        assert len(result) <= 3
        assert "i love you" in result
        print("   ✓ PASSED")
    except (AssertionError, TypeError):
        print("   ✗ FAILED - Check your implementation")

    print("\n" + "="*60)
    print("Complete all exercises to see all tests pass!")
    print("="*60)


if __name__ == "__main__":
    run_tests()
