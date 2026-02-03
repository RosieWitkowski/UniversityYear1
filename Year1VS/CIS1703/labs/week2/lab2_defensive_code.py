# Part A — Identifying User Input Failure Modes 
"""
In your lab notes (or comments), list at least 10 distinct ways a user can break a
simple input program for age = input("Age: )

1. No input
2. Keyboard Interruption (CTRL+C)
3. Non-numeric letters
4. Symbols
5. Negative 
6. Overly large (ages over e.g. 120 is unlikely)
7. Whitespace only
8. Keyboard shortcuts (CTRL+D, CTRL+Z)
9. Decimal number
10. Unexpected formatting (e.g. '1,2' instead of '12')


"""

# Part B — Designing the Input Contract (writing docstrings)
def get_non_empty_string(prompt: str) -> str:
    """Sanitizes whitespace and validates input is not empty

    Args:
        prompt: string desciption of what user should input
    
    Returns: 
        input: validated string, or empty string if invalid 
    """

def get_valid_integer(prompt: str, min_value: int, max_value: int) -> int:
    """Sanitizes whitespace and validates an input can be converted to an int within a specific range
    
    Args:
        prompt: string description of what user should input
        min_value: integer minimum for the range
        max_value: integar maximum for the range
        
    Returns:
        num: integer validated input
        
    Raises:
        ValueError: if cannot convert to int"""

# Part C - 