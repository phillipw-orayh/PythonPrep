"""Template for generating session files."""

from datetime import datetime
from typing import Dict, List, Any


def generate_session_content(
    session_number: int,
    question_data: Dict[str, Any]
) -> str:
    """
    Generate the content for a session file based on question data.

    Args:
        session_number: The session number (e.g., 1, 2, 3)
        question_data: Dictionary containing question information with keys:
            - title: str
            - difficulty: str
            - topics: List[str]
            - description: str
            - constraints: List[str]
            - examples: List[Dict] with 'input' and 'output'
            - hints: List[str]
            - test_cases: List[Dict] with 'input' and 'expected'
            - function_signature: str (optional)

    Returns:
        String containing the complete session file content
    """
    title = question_data.get("title", "Untitled")
    difficulty = question_data.get("difficulty", "Unknown")
    topics = question_data.get("topics", [])
    description = question_data.get("description", "")
    constraints = question_data.get("constraints", [])
    examples = question_data.get("examples", [])
    hints = question_data.get("hints", [])
    test_cases = question_data.get("test_cases", [])
    function_signature = question_data.get("function_signature", "def solution(*args):\n    pass")

    # Format session number with leading zeros
    session_id = f"{session_number:03d}"

    # Format topics as comma-separated string
    topics_str = ", ".join(topics) if topics else "General"

    # Generate today's date
    today = datetime.now().strftime("%Y-%m-%d")

    # Build the session content
    content = f'''"""
SESSION {session_id}: {title}
Difficulty: {difficulty}
Topics: {topics_str}
Generated: {today}
"""

# PROBLEM DESCRIPTION
# {description}

'''

    # Add constraints
    if constraints:
        content += "# CONSTRAINTS\n"
        for constraint in constraints:
            content += f"# - {constraint}\n"
        content += "\n"

    # Add examples
    if examples:
        content += "# EXAMPLES\n"
        for i, example in enumerate(examples, 1):
            content += f"# Example {i}:\n"
            content += f"# Input: {example.get('input', '')}\n"
            content += f"# Output: {example.get('output', '')}\n"
            if example.get('explanation'):
                content += f"# Explanation: {example.get('explanation')}\n"
            content += "#\n"
        content += "\n"

    # Add hints
    if hints:
        content += "# HINTS (reveal after 12 minutes)\n"
        for i, hint in enumerate(hints, 1):
            content += f"# {i}. {hint}\n"
        content += "\n"

    # Add solution section
    content += "# YOUR SOLUTION\n"
    content += f"{function_signature}\n\n"

    # Add test cases
    content += "# TEST CASES\n"
    content += "import unittest\n\n"
    content += "class TestSolution(unittest.TestCase):\n"

    if test_cases:
        for i, test in enumerate(test_cases, 1):
            test_input = test.get('input', '')
            expected = test.get('expected', '')
            content += f"    def test_case_{i}(self):\n"
            content += f"        self.assertEqual(solution({test_input}), {expected})\n\n"
    else:
        content += "    def test_example(self):\n"
        content += "        # Add your test cases here\n"
        content += "        pass\n\n"

    content += 'if __name__ == "__main__":\n'
    content += "    unittest.main()\n\n"

    # Add self-review checklist
    content += "# SELF-REVIEW CHECKLIST\n"
    content += "# [ ] Solution handles edge cases\n"
    content += "# [ ] Time complexity: O(?)\n"
    content += "# [ ] Space complexity: O(?)\n"
    content += "# [ ] Code is readable and well-commented\n"
    content += "# [ ] All tests pass\n"

    return content


def parse_function_name(signature: str) -> str:
    """
    Extract function name from a function signature.

    Args:
        signature: Function signature string

    Returns:
        Function name
    """
    # Simple parser to extract function name
    if "def " in signature:
        parts = signature.split("def ")[1].split("(")
        return parts[0].strip()
    return "solution"
