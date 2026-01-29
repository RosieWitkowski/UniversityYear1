# Exercise 2: Displaying input and return types

# Original
def format_user0(name, age):
    return f"User {name} is {age} years old."

# Rewritten
def formate_user(name: str, age:int) -> str:
    return f"User {name} is {type(age)} years old."

print(format_user0('lacey', 32))
print(formate_user("lacey", 32))
print(formate_user(5, "twenty"))