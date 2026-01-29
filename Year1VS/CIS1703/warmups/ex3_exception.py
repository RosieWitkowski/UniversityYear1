# Exercise 3: Users may provide 'dangerous' input, exceptions can catch these

# Original
"""num1 = 10
num2 = 0
 
result = num1 / num2
print(f"Result is {result}")
"""
# -> Outputs ZeroDivsion Error

# Fixed
num1, num2 = 0, 0 
try:
    num1 = int(input("Num1 = "))
    num2 = int(input("Num2 = "))
except ValueError:
    print("Please provide a number.")
    exit()
    

try:
    print(f"Answer = {num1/num2}")
except ZeroDivisionError:
    print("Cannot divide by zero.")