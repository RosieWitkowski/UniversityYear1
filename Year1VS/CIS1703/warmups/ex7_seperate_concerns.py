# Building on ex1, I/O should stay within the main code, not inside logic functions 

# Original
print("+--- Original ---+")
def double_number(value):
    result = value * 2
    print(result)
 
my_num = double_number(10)
print(f"The number is {my_num}") # Prints None due to function not returning

# Change one word 
print("+--- Fixed ---+")
def double_number(value):
    result = value * 2
    return(result)
 
my_num = double_number(10)
print(f"The number is {my_num}") 


# Playground
print("+--- Extra ---+")
def valid_int():
    while True:
        try:
            num = int(input("Number: "))
            return num
        except ValueError:
            print("Please provide a number.")

def cube(num):
    return num**3

def main():
    num = valid_int()
    ans = cube(num)
    print(f"{num}^3 = {ans}")

if __name__ == "__main__":
    main()

