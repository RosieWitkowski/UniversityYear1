"""
LECTURE DEMO: Building a Robust Expense Tracker
------------------------------------------------
This code combines:
1.  Week 2 Lab skills (Defensive Programming & Error Handling)
2.  Week 3 Portfolio Task 1 (Expense Tracker Logic)

Read the comments to understand how we stop the program from crashing!
"""

# ==============================================================================
# PART 1: DEFENSIVE TOOLS (Your "Safety Net")
# ==============================================================================

def safe_input(prompt):
    """
    A custom input function that handles user interruptions safely.
    """
    # We use a 'try' block because the standard input() function is dangerous.
    # It can crash your program if the user presses Ctrl+C or Ctrl+D.
    try:
        # Attempt to read input from the user normally.
        return input(prompt)
    
    # If the user presses Ctrl+C (KeyboardInterrupt) or Ctrl+D (EOFError)...
    except (KeyboardInterrupt, EOFError):
        # ...we catch the error here so the program doesn't crash.
        print("\n[!] Input cancelled by user.")
        
        # We return 'None' as a signal to tell other functions: "Stop what you are doing."
        return None


def get_valid_string(prompt):
    """
    Asks the user for a string and ensures it isn't empty.
    Used for: Expense Name.
    """
    # Start an infinite loop. We will only break out when we get valid input.
    while True:
        # Call our custom 'safe_input' function instead of the standard 'input'.
        user_input = safe_input(prompt)
        
        # CHECK: Did the user press Ctrl+C? (Is the input None?)
        if user_input is None:
            return None # Exit function immediately, passing the signal up.
            
        # SANITIZE: Remove any spaces from the start and end of the string.
        cleaned_input = user_input.strip()

        # VALIDATE: Check if the string is empty after cleaning.
        if cleaned_input == "":
            # If it is empty, complain to the user.
            print("Error: Input cannot be empty. Please try again.")
            # 'continue' jumps back to the start of the 'while' loop to ask again.
            continue 
            
        # If we reach this line, the input is valid. Return it to the main program.
        return cleaned_input


def get_positive_float(prompt):
    """
    Asks for a number and ensures it is a valid decimal greater than zero.
    Used for: Expense Amount.
    """
    while True:
        # 1. Get the raw string input safely.
        user_input = safe_input(prompt)
        
        # 2. Check for cancellation (Ctrl+C).
        if user_input is None: return None
        
        # 3. Attempt to convert the string to a float (decimal number).
        try:
            # This line will crash (ValueError) if the user types "abc" or "£10".
            value = float(user_input)
            
        # 4. Catch the ValueError if conversion failed.
        except ValueError:
            # Tell the user what went wrong, but don't crash.
            print(f"Error: '{user_input}' is not a valid number.")
            # Loop again to give them another chance.
            continue

        # 5. Logic Check: The number works, but is it positive?
        if value <= 0:
            print("Error: Amount must be greater than zero.")
            continue
            
        # 6. If we survived all checks, return the valid number.
        return value


def get_choice(prompt, options):
    """
    Forces the user to pick from a specific list of options.
    Used for: Expense Category.
    """
    while True:
        # Get input safely.
        user_input = safe_input(prompt)
        if user_input is None: return None
        
        # Sanitize: Convert to Title Case (e.g., "food" -> "Food") so it looks nice.
        cleaned_input = user_input.strip().title() 
        
        # VALIDATE: Check if their input exists in our allowed 'options' list.
        if cleaned_input in options:
            return cleaned_input
        
        # If not, show them the valid options and loop again.
        print(f"Error: Invalid choice. Options are: {', '.join(options)}")


# ==============================================================================
# PART 2: THE EXPENSE TRACKER (Week 3 Task 1 Logic)
# ==============================================================================

def add_expense_feature(expense_list):
    """
    Logic for the 'Add Expense' menu option.
    Notice how clean this code is because we hid the validation logic above!
    """
    print("\n--- Add New Expense ---")
    
    # STEP 1: Get the Name
    # We use our helper function. It handles the loops and errors for us.
    name = get_valid_string("Enter expense name: ")
    
    # If name is None, it means the user hit Ctrl+C. We should stop adding.
    if name is None: return 
    
    # STEP 2: Get the Amount
    # This guarantees we get a valid positive number.
    amount = get_positive_float("Enter amount (£): ")
    if amount is None: return
    
    # STEP 3: Get the Category
    # We define exactly what categories are allowed for Portfolio Task 1.
    valid_categories = ["Food", "Transport", "Utilities", "Entertainment", "Other"]
    category = get_choice("Enter category (Food/Transport/Utilities): ", valid_categories)
    if category is None: return

    # STEP 4: Save the Data
    # Create a dictionary to group these three pieces of data together.
    expense_record = {
        "name": name,
        "amount": amount,
        "category": category
    }
    
    # Add this dictionary to our main list of expenses.
    expense_list.append(expense_record)
    
    # Confirm success to the user.
    print(f"Success: Added '{name}' for £{amount:.2f} in {category}.")


def main():
    """
    The Main Program Loop
    """
    # Create an empty list to store all our expenses.
    my_expenses = []
    
    # This loop keeps the program running until the user chooses 'Exit'.
    while True:
        print("\n=== EXPENSE TRACKER MENU ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        # We reuse 'safe_input' here so the menu doesn't crash on Ctrl+C either.
        choice = safe_input("Select an option: ")
        
        # Basic menu logic
        if choice == "1":
            add_expense_feature(my_expenses)
        
        elif choice == "2":
            # Simple print to show it works (You will format this better in Task 1)
            print(f"\nCurrent Expenses: {my_expenses}")
        
        elif choice == "3" or choice is None:
            # Exit cleanly.
            print("Goodbye!")
            break
        
        else:
            print("Invalid selection.")

# This line checks if we are running this file directly (not importing it).
if __name__ == "__main__":
    main()