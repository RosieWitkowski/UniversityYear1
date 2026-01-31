# Continutation of the pp_calc started during the programming 1 module 

def get_int(txt):
    while True:
        try:
            return int(input(txt))
        except ValueError:
            print("Please provide a number (e.g. 5).")


num = get_int("Number: ")
print(num)

