# Exercise 1: Output remains in main code, functions don't display them

# Original
print("+--- Original ---+")
def double_number(value):
    result = value * 2
    print(result)
 
my_num = double_number(10)
print(f"The number is {my_num}")

# Fixed
print("+--- Pure function ---+")
def double_number(value):
    result = value * 2
    return result 

my_num = double_number(10)
print(f"The number is {my_num}")

# Reflection: prints 'The number is None' because the original fn has no return value 

# Own example of a pure fn 
print("+--- Own example ---+")
def odd_even(num):
    return num % 2 == 0

print(odd_even(3))
print(odd_even(10))
