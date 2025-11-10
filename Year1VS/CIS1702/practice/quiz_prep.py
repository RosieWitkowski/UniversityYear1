# Prep for week 6 quiz using the 5 provided topics (loops, nested loops, functions, variable scope, assert)

'''
TOPIC 1
Loops
    for and while loops
    Understanding range()
'''
# For loop
names = ['Alice', 'Barry', 'Caleb']
print([f"Name: {name}" for name in names])
for name in names:
    print(name, end=" ")
print()

# While loop
play = True 
while play:
    print("= Round =")
    if input("Play again?")[0].upper() != 'Y':
        play = False 

# Range - simple
for x in range(0, 11):
    print(x)

# Range - consider start end as 'start' inclusive, 'end' exclusive
print("Even")
for n in range(2, 11):
    if n % 2 == 0:
        print(n)
print()

# Range - typecast
nums = ""
for x in range(1, 16):
    nums += str(x) + " "
print(nums)

# Range - step
nums = range(1, 11, 2)
print(*nums)

'''
Topic 2 
Nested loops
    Loop control and iteration logic
'''

# Nested loop - print a square 
height, width = int(input("Height: ")), int(input("Width: "))
for x in range(height):
    for y in range(width):
        print("#", end="")
    print()

# Loops cont. - print a right-angle triangle
height = int(input("Height: "))
print("= Triangle = ")
for x in range(1, height+1):
    print("#" * x)

# Loop - print a pyramid 
print(" = Pyramid = ")
width = 1
for x in range(height):
    print(" " * (height-x-1), end="")
    print("#" * width)
    width += 2

IDs = {
    '14290140' : 'Anne',
    '13814920' : 'Boyle',
    '10910211' : 'Cole'
}
for id, name in IDs.items():
    print(f"ID: {id} | Name: {name}")

'''
Topic 3
Functions
    Defining and calling functions
    The return keyword
    Function parameters and outputs
    Writing simple reusable functions
'''
# Defining fn
def print_meow():
    print("Meow\n=^w^=")

# Calling fn
print_meow()
for x in range(2):
    print_meow()

# Return values
def is_even(num):
    return True if num % 2 == 0 else False
 
even = is_even(4)
print(f"Is 4 even? Ans: {even}")

print(f"Is 9 even? Ans: {is_even(9)}")

# Paramters and outputs
print(is_even(31)) # Expected output: False
print(is_even(24)) # Expected output: True

# Simple reusable fns
def valid_str_option(options, msg):
    choice = options[0].upper() + 'AHKJSHKFKJ' # Ensures not one of the options
    max_len = len(options[0]) # For words that start with the same few letters
    while choice not in options: 
        choice = input(msg)[:max_len].upper()
    return choice

valid_str_option(['EN', 'AU', 'AM'], 'Enter England, Australia or America: ')

''' 
Topic 4
Variable Scope
    Local vs. global variables
    Understanding how variable values change inside and outside functions
'''
global_var = 100

def scope_test():
    global_var = 5
    print(global_var)
    return global_var

def best_practice(paramater):
    paramater = 2
    return paramater

print(scope_test())
print(global_var)

print(best_practice(300))

'''
Topic 5
The assert Statement
    Purpose and use in debugging and validation
'''

# Simple unit tests using assert
print("Running tests... ")
try:
    assert is_even(9) == False 
    assert is_even(300) == True
    assert is_even(2) == False # Should fail
    print("Tests passed!")
except AssertionError:
    print("Tests failed.")

print("Running tests 2... ")
assert is_even(3) == True # Should raise error and return before next line
print("Test 2 passed!")