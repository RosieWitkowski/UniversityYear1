from random import randint

def valInt(msg):
    num = 'A'
    while not num.isnumeric():
        try:
            num = input(msg)
        except ValueError:
            print("Please enter an integar.")
    return int(num)

def valChar(options, msg):
    letter = "2"
    while not letter.isalpha() or letter not in options:
        letter = input(msg)[0].upper()
    return letter


def round():
    attempts = 0

    correct_num = randint(1, 100)
    guess = valInt("Guess: ")

    while guess != correct_num:
        if guess > correct_num:
            print("Lower")
            guess = valInt("Guess: ")
        else:
            print("Higher")
            guess = valInt("Guess: ")
        attempts += 1
    print(f"Correct, {correct_num}! Attempts: {attempts}")

play = True 
while play:
    round()
    choice = valChar(['Y', 'N'], "Play again? Y/N")
    if choice == 'N':
        play = False 

