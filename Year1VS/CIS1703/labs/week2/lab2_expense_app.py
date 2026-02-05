from datetime import datetime
import json 

"""Basic Expense Entry and Viewing
Implement the core functionality to add a single expense (name, date, category, amount) and then view all entered expenses.
Focus on correct input capture and simple list storage."""

def add_expense(expenses: list[dict], categories, min_year, current_yr, max_attempts) -> list[dict]:
    print("+ -- Adding expense --+")
    name = get_string("Name: ", max_attempts)
    date = get_date("Date: ", min_year, current_yr, max_attempts)
    str_options = "/".join(categories)
    category = get_choice(f"Category ({str_options}): ", categories, str_options, max_attempts)
    amount = get_int('Amount: ', 0, None, max_attempts)
    cost = get_float('Cost: £', 0.0, None, max_attempts)

    item = {
        'name': name, 
        'date': date, 
        'category': category,
        'amount': amount,
        'cost': cost
    }
    expenses.append(item)
    print("+ -- Item added successfully -- +")
    return expenses 

"""Expense Editing and Deletion
Add functionality to allow users to select an expense by its index or a unique identifier and then edit its details or delete it entirely. 
This will involve searching for the specific expense in the stored data and modifying or removing it."""
def find_product(prompt: str, expenses: list[dict], max_attempts: int) -> int:
    name = get_string(prompt, max_attempts)
    print("Searching...")
    for index, product in enumerate(expenses):
        if product['name'] == name:
            print("Product found!")
            return index
    print("Product not found")
    return None
        
def delete_product(prompt: str, expenses:list[dict], max_attempts: int):
    idex = find_product(prompt, expenses, max_attempts)
    if idex is not None:
        expenses.pop(idex)
        print("Product deleted succesfully!")
    return expenses 

def edit_product(prompt: str, expenses:list[dict], min_year: int, current_yr:int, max_attempts:int):
    index = find_product(prompt, expenses, max_attempts)
    if index is None:
        return expenses 
    print(f"+-- Editing {expenses[index]} --+")
    categories = ['name','date', 'category','amount', 'cost']
    categories_str = "/".join(categories)
    choice = get_choice(f"Data to change ({categories_str}): ", categories, categories_str, max_attempts)
    choice = choice.lower()
    if choice in ['name', 'category']:
        expenses[index][choice] = get_string(f"{choice}: ", max_attempts)
    elif choice == 'date':
        expenses[index][choice] = get_date("Date (DD-MM-YYYY): ", min_year, current_yr, max_attempts)
    elif choice in ['amount', 'cost']:
        expenses[index][choice] = get_int(f"{choice}: ", 0, None, max_attempts)          
    else:
        print("Unexpected index.")
        exit()
    print("Edited successfully.")
    return expenses 


def populate_expenses(expenses: list[dict]) -> list[dict]:
    """Populates expenses with some default items"""
    expenses.append({
        'name': 'bike',
        'date': '05-02-2026',
        'category': 'vehicle',
        'amount': 12,
        'cost': 100
    })
    expenses.append({
        'name': 'apple',
        'date': '05-01-2026',
        'category': 'food',
        'amount': 32,
        'cost': .53
    })
    expenses.append({
        'name': 'car',
        'date': '03-02-2026',
        'category': 'vehicle',
        'amount': 5,
        'cost': 20000
    })
    expenses.append({
        'name': 'chocolate',
        'date': '18-04-2025',
        'category': 'food',
        'amount': 100,
        'cost': 1.20
    })

    return expenses

def print_expenses(expenses: list[dict]) -> None:
    print("+ -- Printing expenses -- +")
    for product in expenses:
        for key, value in product.items():
            if key == 'cost' or key == 'price':
                try:
                    print(f"{key}: £{value:.2f}")
                    continue
                except ValueError:
                    pass
            print(f"{key}: {value}")
        print("+-----------------+")
    print("+ -- Items printed successfully -- +")


"""Total Expense Calculation
Extend the application to calculate and display the sum of all recorded expenses. 
This involves iterating through stored expenses and accumulating their amounts."""
def calculate_cost(expenses: list[dict]) -> float:
    sum = 0
    for product in expenses:
        try:
            sum += product['amount'] * product['cost']
        except TypeError:
            print("Error: Unexpected value for price field.\nExiting program...")
            exit()
    return float(sum)

"""Category Filtering with Validation
Add the ability to filter expenses by category. 
Implement robust validation for the category input to ensure it matches one of the allowed options, 
and then display the filtered results."""

def safe_input(prompt: str) -> str:
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("[!] Error: user cancelled input")
        return ""
    
def get_string(prompt: str, max_attempts: int) -> str:
    attempts = 0
    while attempts < max_attempts:
        attempts += 1 
        user_input = safe_input(prompt).strip()
        if user_input == "":
            print("Error: Input cannot be empty.")
            continue 
        return user_input 
    print("Max attempts reached, exiting program...")
    exit()

def get_int(prompt: str, min_value: int, max_value: int,  max_attempts: int) -> int:
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        num = safe_input(prompt).strip()
        if num == "":
            print("Error: number cannot be empty.")
            continue 
        try:
            num = int(num)
        except ValueError:
            print("[!] Error: number be numeric (e.g. 1, 2).")
            continue

        if (min_value is not None and num < min_value) or (max_value is not None and num > max_value):
            if min_value is not None and max_value is not None:
                print(f"Error: number must be within range {min_value} to {max_value}")
            elif min_value is None:
                print(f"Error: number must be less than or equal to {max_value}")
            else:
                print(f"Error: number must be more than or equal to {min_value}")
        return num 
    print("Max attempts reached, exiting the program...")
    exit()

def get_float(prompt: str, min_value: float, max_value: float, max_attempts: int) -> float:
    attempts = 0 
    while attempts < max_attempts:
        attempts += 1 
        num = safe_input(prompt).strip()
        if num == "":
            print("Error: number cannot be empty.")
            continue 
        try:
            num = float(num)
        except ValueError:
            print("Error: number must be numeric.")
            continue 

        if min_value is not None and max_value is not None:
            if num < min_value or num > max_value:
                print(f"Error, must be within range {min_value} to {max_value}")
                continue
        elif min_value is not None:
            if num < min_value:
                print(f"Error: input must be equal to or greater than {min_value}")
                continue
        else:
            if num > max_value:
                print(f"Error: input must be equal to or less than {max_value}")
                continue 
        
        return num
    print("Max attempts reached, exiting the program...")
    exit()

"""Date and Amount Validation with Error Handling
Implement robust validation specifically for the date (YYYY-MM-DD format) and amount (numeric, greater than zero) fields. 
Use try-except blocks to gracefully handle non-numeric input for amounts and invalid date formats, prompting the user to re-enter valid data."""
def get_date(prompt: str, min_year, current_yr: int, max_attempts: int) -> str:
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        date = safe_input(prompt).strip()
        if date == "":
            print("Error: date cannot be empty.")
            continue
        try:
            d,m,y = date.split("-")
        except ValueError:
            print("Error: Please provide date in specified format.")
            continue
        
        try:
            d = int(d)
            m = int(m)
            y = int(y)
        except ValueError:
            print("Error: date must be numeric.")
            continue

        if y > current_yr or m > 12 or y < min_year:
            print("Error: year or month invalid.")
            continue 

        if (d > 29 and m == 2) or d >= 31 and d not in [3, 4, 9, 11]:
            print("Error: invalid day.")
            continue 

        return f"{d}-{m}-{y}"
    print("Max attempts reached, exiting the program...")
    exit()

def get_choice(prompt: str, options: list[str], str_options: str, max_attempts: int) -> str:
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        choice = safe_input(prompt).lower()
        if choice == "":
            print(f"Error: Input cannot be empty.\nAttempt {attempts}/{max_attempts}")
            continue 
        if choice not in options:
            print(f"Error: Please select from valid options ({str_options})\nAttempt {attempts}/{max_attempts}")
            continue 
        return choice 
    print("[!] Max attempts reached, exiting the program...")
    exit()

def filter_expenses(expenses: list[dir], type: str, category: str) -> list[dict]:
    filtered = []
    for product in expenses:
        if product[type] == category:
            filtered.append(product)
    return filtered

"""Data Persistence (Saving and Loading)
Implement functionality to save the current list of expenses to a file (e.g., CSV or JSON) and load them back into the application when it starts. 
This will introduce file I/O operations and serialization/deserialization."""
def load_file(filename: str) -> list[dict]:
    try:
        with open(filename, 'r') as f:
           print("> Expenses loaded successfully")
           return json.load(f)
    except FileNotFoundError:
        print("Error: file not found")
        return None
    except json.JSONDecodeError:
        print("Error: file corrupted")
        return None

def save_file(filename: str, expenses: list[dict]) -> None:
    with open(filename, 'w') as f:
        json.dump(expenses, f, indent=4)
        return print("> Expenses saved successfully")

"""Full Application Menu and Control Flow
Integrate all previous functionalities (add, view, calculate total, filter) into a menu-driven interface. 
Ensure the program continues to loop until an explicit exit option is chosen, and handles invalid menu choices gracefully."""
def main():
    categories = ['vehicle', 'food', 'other']
    categories_str = "/".join(categories)
    yn = ['y', 'yes', 'no', 'n',]
    yn_str = "/".join(yn)
    menu = ['add', 'edit', 'delete', 'print', 'total', 'filter']
    menu_str = "/".join(menu)

    default_max = 3
    min_yr, current_yr = 1940, int(datetime.now().year)

    expenses = load_file('expenses.json')
    if expenses is None:
        expenses = []
    while True:
        print(f"+-- MENU --+")
        select = get_choice(f"Please select from: {menu_str} ", menu, menu_str, default_max)
        if select == 'add':
            expenses = add_expense(expenses, categories, min_yr, current_yr, default_max)
        elif select == 'edit':
            expenses = edit_product(f"Name of product to edit: ", expenses, min_yr, current_yr, default_max) 
        elif select == 'delete':
            expenses = delete_product(f"Name of product to delete: ", expenses, default_max)
        elif select == 'print':
            print_expenses(expenses)
        elif select == 'total':
            cost = calculate_cost(expenses)
            print(f"Total cost: £{cost:.2f}")
        elif select == 'filter':
            category = get_choice(f"Sort by category ({categories}): ", categories, categories_str, default_max)
            print(f"\n+-- Sorting by category: {category} --+")
            print_expenses(filter_expenses(expenses, 'category', category))
        else:
            print("Unexpected index.")
            exit() 
        """add_expense(expenses, categories, 1990, current_yr, default_max)
        expenses = populate_expenses(expenses)
        print_expenses(expenses)

        cost = calculate_cost(expenses)
        print(f"Total cost: £{cost:.2f}")

        
        category = get_choice(f"Sort by category ({categories}): ", categories, categories_str, default_max)
        filtered = filter_expenses(expenses, 'category', category)
        print(f"\n+-- Sorting by category: {category} --+")
        print_expenses(filtered)
        """
        choice = get_choice(f"Continue? {yn_str}: ", yn, yn_str, default_max)
        if choice in yn[2:]:
            print("Thank you for using ExpenseApp.IO, see you next time!")
            save_file("expenses.json", expenses)
            exit()

if __name__ == "__main__":
    main()