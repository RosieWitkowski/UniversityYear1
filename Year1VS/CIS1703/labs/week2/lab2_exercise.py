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
def get_non_empty_string(prompt: str, max_attempts: int) -> str:
    """Sanitizes whitespace and validates input is not empty

    Args:
        prompt (str): desciption of what user should input
        max_attempts (int): maximum allowed attempts before loop stops 
    
    Returns: 
        input (str): validated string, or empty string if invalid 
    """
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        user_input = safe_input(prompt)
        if not user_input:
            print("Error: input cannot be empty")
            print(f"Attempt {attempts}/{max_attempts}")
            continue 
        user_input = user_input.strip()
        if user_input == "":
            print("Error: input cannot be empty")
            print(f"Attempt {attempts}/{max_attempts}")
            continue 
        return user_input
    print("[!] Max attempts reached, exiting program...")
    exit()

# Part D - Robust Integer Handling
def get_valid_integer(prompt: str, min_value: int, max_value: int, max_attempts: int) -> int:
    """Sanitizes whitespace and validates an input can be converted to an int within a specific range
    
    Args:
        prompt (str): description of what user should input
        min_value (int): minimum for the range
        max_value (int): maximum for the range
        max_attempts (int): maximum allowed attempts before loop stops 
        
    Returns:
        num (int): validated input
        
    Raises:
        ValueError: if cannot convert to int
    """
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        num = safe_input(prompt)
        if not num:
            print("Error: input is required.")
            print(f"Attempt {attempts}/{max_attempts}")
            continue 
        num = num.strip()
        if num == "":
            print("Error: input is required.")
            print(f"Attempt {attempts}/{max_attempts}")
            continue 
        
        try:
            num = int(num)
            if num >= min_value and num <= max_value:
                return num 
            print(f"Error: value must be between {min_value} and {max_value}")
        except ValueError:
            print("Error: please enter a valid integer")
            continue 
    print("[!] Max attempts reached, exiting program...")
    exit()

# Extension - Robust Float Handling
def get_valid_float(prompt: str, min_value: float, max_value: float, max_attempts: int) -> float:
    """Sanitzaises whitespace and validates an input can be typecast to a float within a specified range
    
    Args:
        prompt(str): text to be shown to user, prompting for a float
        min_value(float): minimum value for range
        max_value(float): maximum value for range
        max_attempts(int): maximum allowed attempts for input, before exiting program
    
    Returns:
        float: validated float

    Raises:
        ValueError: if cannot be converted to flaot
    """

    attempts = 0 
    while attempts < max_attempts:
        attempts += 1
        num = safe_input(prompt)
        if num is None:
            print("Error: input cannot be empty.")
            print(f"Attempt {attempts}/{max_attempts}")
            continue 
        num = num.strip()
        if num == "":
            print("Error: input cannot be empty.")
            print(f"Attempt {attempts}/{max_attempts}")
            continue 
        
        try:
            num = float(num)
            if num < min_value or num > max_value:
                print(f"Error: input not within range {min_value} to {max_value}")
                print(f"Attempt {attempts}/{max_attempts}")
                continue
        except ValueError:
            print("Error: input must be numeric.")
            print(f"Attempt {attempts}/{max_attempts}")
            continue 
        return num 
    
    print("Max attempts reached, exiting program...")
    exit()
    
# Part C - Input Engine
def safe_input(prompt: str) -> str:
    """Safely reads user input
    Args:
        prompt (str): text to be prompted to the user
        
    Returns:
        input (str): user's input
        None: if KeyboardInterrupt or EOFError
    """

    try:
        return input(prompt)
    except(KeyboardInterrupt, EOFError): 
        print("[!] User cancelled input.")
        return None 

# Testing
"""name = get_non_empty_string("Name: ")
print(f"Hello, {name.title()}")

age = get_valid_integer("Age: ", 0, 123)
print(f"Understood, you are {age} years old.")"""

# Part E - Advanced Input: Restriced Choices
def get_choice(prompt: str, choices: list[str], max_attempts: int) -> str:
    """Accepts only values in choice (case-insensitive), preserving the original format
    
    Args:
        prompt(str): text to be prompted to user 
        choices(list[str]): list of acceptable options
        max_attempts (int): maximum allowed attempts before loop stops 
        
    Returns:
        string: originaly formatted option that is within the allowed choices
    """
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        choice = safe_input(prompt)
        if choice is None:
            print("Error: Input is required.")
            print(f"Attempt {attempts}/{max_attempts}")
            continue 
        if choice.title() in choices:
            return choice 
        else:
            print("Error: Please chose a valid option from the choices.")
            print(f"Attempt {attempts}/{max_attempts}")
    print("[!] Max attempts reached, exiting program...")
    exit()

# Testing
"""options = ["Easy", "Medium", "Hard"]   
choice = get_choice(f"Difficulty ({options}): ", options)
print(f"Understood, you have chosen {choice} difficulty.") """

# Part F: Integration Program (main)
def main():
    default_attempts = 3

    user = get_non_empty_string("Username: ", default_attempts)
    age = get_valid_integer("Age (0-120): ", 0, 120, default_attempts)
    points = get_valid_float("Points (0-500.25)", 0, 500.25, default_attempts)

    roles = ['Admin', 'User', 'Guest']
    role = get_choice(f"Role ({roles}): ", roles, default_attempts)

    stay_signed = get_choice(f"Stayed signed in on this device? (y/n): ", ['Yes', 'No', 'Y', 'N'], default_attempts)

    print(f"== {role.upper()} LOGIN ==\nWelcome, user {user}!\nWe have verified your role ({role}) and age ({age}), signing you in...")
    if stay_signed[0].upper() == 'Y':
        print("Thank you for confirming your sign in option, we will keep you signed in.")
    else:
        print("Thank you for opting out to re-sign in, we will remember for next time.")
    print(f"You have: {points} points!")

if __name__ == "__main__":
    main()
