def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2 

def mod(num1, num2):
    return num1 % num2 

def valInt(msg):
    num = 'A'
    while not num.isnumeric():
        try:
            num = input(msg)
        except ValueError:
            print("Please enter an integar.")
    return int(num)

def get_option(options, msg):
    letter = "2"
    while letter not in options:
        letter = input(msg).strip()[0].upper()
    return letter

def calc():
    num1, num2 = valInt('Num1: '), valInt("Num2: ")
    options = ['+', '-', '*', '/', '%']
    op = get_option(options, f"Operation ({options}): ")
    if op == '+':
        print(add(num1, num2))
    elif op == '-':
        print(subtract(num1, num2))
    elif op == '*':
        print(multiply(num1, num2))
    elif op == "/":
        print(divide(num1, num2))
    elif op == "%":
        print(mod(num1, num2))
    else:
        print("Error.")

while True:
    calc()
    if get_option(['N', 'Q', 'Y'], 'Calculate again? Y/N/Quit') in ['Q', 'N']:
        break 
