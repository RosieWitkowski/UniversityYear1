from random import randint
from time import sleep 

SLEEP_INTERVAL = .5

def main():
    play = True

    while play:
        choice = valid_char(['S', 'V'], "= Enter START to begin, or 'view' to see the answer book (spoilers) =\n")
        while choice != 'S':
            answers()
            choice = valid_char(['S', 'V'], "= Enter START to begin, or 'view' to see the answer book again =\n")

        gold = play_game()
        print(f"Congratulations, you completed Wizard Escape! Score (pointless): {gold}")

        choice = valid_char(['Y', 'N'], "= Play again? Y/N =\n")
        if choice == 'N':
            print("Thanks for playing!\nExiting game... ")
            play = False 

def valid_char(options, msg):
    min_len = len(options[0])
    choice = options[0][:min_len] + 'ASHSAFHLFSAKJ'

    while choice not in options:
        choice = input(msg)[0].upper()
    return choice 


def play_game():
    print("> You enter the odd dungeon... ")
    sleep(SLEEP_INTERVAL)

    puzzles, gold, misses = 0, 0, 0
    directions = []

    while puzzles < 3:
        if misses == 3:
            print("> The odd wizard gets bored of you going circles and takes pity(?)... ")
            sleep(SLEEP_INTERVAL)
            for n in range(3 - puzzles):
                print("You see... ")
                puzzles += 1
                gold = puzzle(puzzles, gold, directions)
            return gold 
        
        randomizer, direction = randint(1, 2), 0
        
        choice = valid_char(['L', 'R'], "> Will you turn left or right? ")
        if choice == 'L':
            print("> Heading left, you find... ", end="")
            sleep(SLEEP_INTERVAL)
            direction = 1
            directions.append(1)
        else:
            print("> Turning right, you see... ", end="")
            sleep(SLEEP_INTERVAL)
            direction = 2
            directions.append(2)
        
        if direction == randomizer:
            puzzles += 1
            gold = puzzle(puzzles, gold, directions)
        else:
            misses += 1
            gold = chest(gold)

    return gold

def puzzle(puzzles, gold, directions):
    print("an odd wizard!\n> The odd wizard prances around, cheering 'MWAHAHAHEE MWAHAHEE, CAN'T CATCH ME'")
    if puzzles == 1:
        gold = name_puzzle(gold)
    elif puzzles == 2:
        gold = number_puzzle(gold)
    else:
        gold = direction_puzzle(gold, directions)
    return gold

def chest(gold):
    print("An old wooden chest!\n> You gained 50 gold! It's completely useless!")
    gold += 50
    return gold

def name_puzzle(gold):
    names = ['ABRACADABRA', 'PLEASE', 'AEIOU', 'L33T']
    hints = ['the magic word!', 'the real magic word!', 'hmmm... the first 5 guesses in hangman mwahahahee!', "mwahahahee, I'm elit5!"]
    
    randomizer = randint(0, 3)
    name, hint = names[randomizer], hints[randomizer]
    text_box = ("> 'Wheeze, wheeze'", "> The odd wizard looks out of breathe", "> 'OK, fine... if you can guess my name I'll let you live!", "> A piece of (magical?) paper flutters before you...", f'> A hint, a hint! Here: {hint}')
    for text in text_box:
        print(text)
        sleep(SLEEP_INTERVAL)
    
    guess = input("> Name: ").upper()
    if guess == name:
        print("> Mwahahahee, correct! Here!\nYou look down to find a bunch of chocolate gold coins in your palm... thanks?\n> + 100 gold(?)!")
        gold += 100
    elif guess == 'ODD':
        print(f"> Huh, whose that? I'm {name}!!")
    else:
        print(f"> Mwahahaee, wrong! It's {name}!")
    
    sleep(SLEEP_INTERVAL)
    print("> A cloud of smoke suddenly engulfs you and the wizard is nowhere to be seen...\n> You continue on...")

    return gold 

def number_puzzle(gold):
    print("> Sensing your growing annoyance, the wizard stops his chant sheepishly")
    sleep(SLEEP_INTERVAL)
    text_box = ["> I know what you want! To get out of this smelly dungeon right?", "> Well fine, I'll let you in on a little secret... ", "> I'm the key to this whole place, and I'll let you out if you play my games! You've already played one, I'll let you off with 2 more!"]
    for text in text_box:
        print(text)
        sleep(SLEEP_INTERVAL)
    print("> Alright, you're game right? Then guess my favourite number! Mwahahahee!")

    guess = int(input("Number: "))
    if guess % 2 == 0:
        print("> Even, ewww!")
    else:
        print("> Mwahahee, odd is me! Correct!\n> Your pockets feel heavier... +100 gold")
        gold += 100

    sleep(SLEEP_INTERVAL)
    print("Once again you find yourself alone... ")
    return gold 

def direction_puzzle(gold, directions):
    text_box = ["> Hold on a minute...", "> Huh, these rooms all look the same...", "> Would you give me some directions?", "> Mwahahaee, I'll let you free! I'll let you free! If you tell me...", '> Despite his bravado, he looks desperate...']
    for text in text_box:
        print(text)
        sleep(SLEEP_INTERVAL)

    print("(Please input the direction you went in, one at a time, in order)")
    for direction in directions:
        guess = int(input('Direction (1 - Left, 2 - Right): '))
        if guess != direction:
            print("(Incorrect direction inputted)\n'Thanks!' cackles the odd wizard, rushing off in the wrong direction...")
            return gold
    
    prize = len(directions) * 75
    gold += prize
    print(f"> MWAHAHAHEE, I'M IMPRESSED!> Your pocket jinggles with the weight of + {prize} gold")
    return gold


def answers():
    print("= WARNING: Solutions to all challenges, do not read if you want to complete unaided =")
    print("> Name puzzle solution (and hint): Randomized each run, either Abracadabra (the magic word), Please (the real magic word), AEIOU (hangman), or L33T (elite)")
    print("> Number puzzle: any odd number (he is an odd wizard)")
    print("> Directions: different each run")

main()
