from time import sleep

def main():
    play = True
    while play:
        points = game()
        print(f"You scored: {points} points!")

        play = validate_str('Play again? Y/N ', ['Y', 'N'])
        if play == 'N':
            print("Thank you for playing!\nExiting... ")
            break 

def game():
    print_delay(['Ahead of you is a fork in the road...'], .75)
    choice = validate_str('Will you go left or right?', ['L', 'R'])

    if choice == 'L':
        points = first_left()
    else:
        points = first_right()

    return points 


def first_left():
    print_delay(["It's too dark to see anything... ", 'You reach out and feel what could be a torch.'], 1)
    choice = validate_str("Light the 'torch'(L), or attempt to keep moving?(M) (Please select L or M)", ['L', 'M'])

    if choice == 'L':
        print_delay(["You try lighting the torch against the stone wall...", 'Success! You can now see the long hallway ahead.'], 1)
        points = hallway1()
    else:
        print_delay(["You keep moving...", "THUD!", 'You fell in a pit and died...', 'GAME OVER!'], .75)
        points = -5 
    
    return points

def first_right():
    pass

def hallway1():
    print("Congratulations! You win!")
    return 100

# Repeatedly asks for an input, until an option is provided that's within the given options
def validate_str(msg, options):
    choice = ''
    length = len(options[0]) # How far into input str to compare to options (for alliterative options)
    while choice not in options:
        choice = input(msg)[:length].upper()
    return choice 

# Prints from a list of sentences, with a delay between each
def print_delay(msg, delay):
    for sentence in msg:
        print(sentence)
        sleep(delay)

main()
