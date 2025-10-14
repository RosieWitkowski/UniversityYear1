# Examples of data types
strEx = "Rosie"
intEx = 21
floatEx = 155.9
boolEx = False 

print(f"{strEx} is a {type(strEx)}, it's a piece of text/pointers from one char to the next.")
print(f"{intEx} is an {type(intEx)}, it's a whole number.")
print(f"{floatEx} is a {type(floatEx)}, it'sa decimal number.")
print(f"{boolEx} is a {type(boolEx)}, it's either True or False. T/F can also be represented as 0 = F, 1 = T (is/not).")

strEx = 200
print(strEx, type(strEx))

"""
Python allows you to later change a variable's data type, because it's a dynamically typed language. This is also why there isn't a need
to specify a data type when initialising.
"""