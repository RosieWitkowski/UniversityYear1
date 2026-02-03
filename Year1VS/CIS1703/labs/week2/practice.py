amounts = [10.0, 5.50, 20.0]
total = sum(amounts)
print(total)

VALID_CATEGORIES = ["Food", "Transport", "Utilities", "Entertainment", "Other"]

def is_valid_category(category: str) -> bool:
    category = category.strip()
    if not category or category == "":
        return "Cannot be empty."
    
    return category.title() in VALID_CATEGORIES

def safe_input(prompt: str) -> str:
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\n[!] User cancelled input.")
        return ""
    
def get_valid_integer(prompt: str) -> int:
    while True:
        value_str = safe_input(prompt).strip()
        if not value_str:
            print('\n[!] Input required.')
            continue
        
        # Try to convert to int below
        try:
            num = int(value_str)
        except ValueError:
            print("\n[!] Input must be numeric.")
            continue 
        return num 

def get_valid_string(prompt: str) -> str:
    while True:
        user_input = safe_input(prompt).strip()
        if not user_input:
            print("\n[!] Input required.")
            continue 
        return user_input

name = "Lunch"
amount = 12.5
category = "Food"

expenses = []

# Create a record for 'Coffee', 3.50, 'Food'
record = {
    'name': 'Coffee',
    'amount': 3.50,
    'category': 'Food'
}

# Append to expenses
expenses.append(record)


# Assume helpers are available

print('--- Expense Tracker ---')

# 1. Get Name
name = get_valid_string("Name: ")

# 2. Get Amount
amount = get_valid_integer("Amount: ")

# 3. Save
expenses.append({'name': name, 'amount': amount, 'category': 'N/A'})
print(expenses)


# Test
print(is_valid_category('Food')) # Should be True
print(is_valid_category(' food  ')) # Should be True
print(is_valid_category(safe_input("Category: "))) 
print(is_valid_category('Car'))  # Should be False
print(get_valid_integer("Number: "))