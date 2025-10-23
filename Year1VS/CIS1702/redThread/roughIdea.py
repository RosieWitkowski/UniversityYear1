from random import randrange
from time import sleep

def main():
    points = 0
    modifier = 1 # Gets faster every round

    play = True
    while play:
        points = level(points, modifier)
        
        print("Play? Y/N")
        choice = 'B'
        while not choice.isalpha or (choice.upper()[0] not in ['Y', 'N']):
            choice = input().upper()[0]
        if choice == 'N':
            play = False
        
        modifier += .25
        
    print(f"= POINTS =\n{points}")
    

def level(points, modifier):
    # Start every round with a duck
    duck()
    round_ongoing = True 
    while round_ongoing: 
        animal, round_ongoing = round()

        stall = randrange(1, 2)
        stall /= modifier
        sleep(stall)
        print("TIME WAIT: ", stall)
        modifier += .05

    if animal == "SP":
        points += 1
    else:
        points += 2
    
    return points

def round():
    randSelect, attempts = randrange(1, 11), 0

    # Maximum ten animals per round before pig
    if attempts > 9:
        pig()
        return "regular", 0

    # Probability: Duck - 3/5, Frog - 1/5, Shiny Pig - 1/10, Pig - 1/10
    if randSelect <= 6:
        attempts += 1
        duck()
        return 'D', True
    elif randSelect <= 8:
        attempts += 1
        frog()
        return 'F', True
    elif randSelect == 9:
        attempts += 1
        shiny_pig()
        return 'SP', False
    else: 
        attempts += 1
        pig()
        return 'P', False


def pig():
    print("<pink background>")
    print("PIG!")
    print("= TAP HERE =")

def duck():
    print("<yellow background>")
    print("DUCK!")

def frog():
    print("<green background>")
    print("FROG!")

def shiny_pig():
    print("<holographic background>")
    print("PIG (SHINY)!")
    print("= TAP HERE! =")

if __name__ == "__main__":
    main()

