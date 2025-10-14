"""
This program takes an age as input, validates, then uses an if-else statement to decides which menu to reccomend the individual.
"""

def valNum(rangMin, rangMax, mesg):
    # Validates input is an integar and within (inclusive) the range given
    num = rangMax + 10
    while not str(num).isnumeric() or not(num >= rangMin and num <= rangMax):
        try: 
            num = int(input(mesg))
        except ValueError:
            print("Invalid input provided.")
    return num 


age = valNum(0, 150, 'Age: ')
print(f'Age given: {age}')

print("Welcome! Please use the ", end = "")
if age > 64:
    print("Seniors' ", end="")
elif age > 13:
    print("Adults' ", end="")
    if age < 18:
        print("or Childrens' ", end="")
elif age > 3:
    print("Childrens' ", end="")
else:
    print("Infants' ", end="")
print("menu.")