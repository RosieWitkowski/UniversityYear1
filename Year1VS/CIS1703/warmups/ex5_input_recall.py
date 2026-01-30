"""
Concept: Program should not crash from bad user input but gracefully handle through loops
Task: Write a loop that repeatedly asks the user for their age until valid input is provided.
"""

age = 'a'
while True:
    try:
        age = int(input("Age: "))
        if age > -1:
            print(f"Understood, we will reccord your age as {age} years old.")
            break 
        else:
            print("Please provide a positive number.")
    except ValueError:
        print("Please provide a number.") 
    