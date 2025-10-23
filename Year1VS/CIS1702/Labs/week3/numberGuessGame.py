from random import randint

def valStr(options, msg):
    choice = ' '
    while choice not in options:
        choice = input(msg)
        choice = choice[0].upper()
    return choice

def valInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print("Invalid input")

def round(wins, losses):
    max_attempts, attempts = 10, 0
    num = randint(1, 100)
    guess = valInt("Guess: ")

    while guess != num:
        attempts += 1
        if attempts == max_attempts:
            print("Incorrect! Max attempts reached.")
            return wins, losses+1
        if guess > num:
            highLow = 'lower'
        else:
            highLow = 'higher'
        guess = int(input(f"Incorrect! Attempts remaining: {max_attempts - attempts} Guess again ({highLow}): "))

    print(f"Correct, it was {num}!")
    return wins+1, losses
    

def main():
    wins, losses = 0,0
    play = 'Y'
    print("Welcome to guess the number!\nYou will be given a random number between 1 and 100. Try to guess in as few as possible!")
    while play == 'Y':
        wins, losses = round(wins, losses)
        print(f"= Score =\nWins: {wins} Losses {losses}")
        play = valStr(['Y','N'], "Play again?(Y/N)")

if __name__ == "__main__":
    main()