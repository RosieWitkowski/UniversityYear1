"""
Scenario: You are developing a system that accepts prices entered by users.
A valid price must:
● Be numeric
● Be greater than 0
● Not exceed 1000
The system must reject invalid inputs with clear, human-friendly messages.
"""

def validate_price(text: str) -> float:
    """Validates price is numeric, positive and less than or equal to 1000

    Args:
        text: Str user input for the price

    Returns:
        float: Validated price

    Raises:
        ValueError: If text is non-numeric, less than 0 or over 1000
    
    """
    if not text.strip():
        raise ValueError("Price is required.")
    
    try:
        num = float(text)
    except ValueError:
        raise ValueError("Must be a number.")
    
    if num < 0:
            raise ValueError("Must be positive.")
    elif num > 1000.01:
        raise ValueError("Must not exceed 1000.")
    
    return num
        
# Provided example usage
user_input = input("Price: ")
try:
    price = validate_price(user_input)
    print(f"Accepted price: £{price:.2f}")
except ValueError as e:
    print(f"Error: {e}")