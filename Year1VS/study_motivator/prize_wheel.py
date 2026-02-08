from random import randint
import input_handler as valid_input

titles = ['Noob', 'Sprout', 'Determined', 'Successfull', 'Winner', 'Champion',]

def wheel(tickets: int, points: int, title: str) -> tuple[int, int, int, int, int, int, list[str]]:
    yn = ['y', 'yes', 're-roll', 'r', 'n', 'no', 'exit', 'cancel']
    ans = valid_input.get_choice("Roll the wheel? (y/n)? ", yn)
    if ans in yn[4:]:
            print("Cancelling... ")
            return tickets, 0, 0, 0, 0, 0, None, None 
    
    
    small, medium, big = 0, 0, 0
    rolls, ttl_miss = 0, 0
    prizes = []

    if tickets <= 0:
        print("Please purchase a ticket or tickets first!")
        print(f"Your balance: {tickets} Tickets, Points {points}")
        return tickets, 0, 0, 0, 0, 0, None, None 

    new_title = None 

    while tickets > 0:
        if new_title == None:
            title_index = titles.index(title)
        else:
            title_index = titles.index(new_title)
        print(f"Tickets: {tickets}")
        
        # Probabilities
        small_prize = randint(1, 5)
        title_prize = randint(1,10)
        medium_prize = randint(1, 10)
        big_prize = randint(1, 100)

        randomizer = randint(1, 3)

        rolls += 1
        tickets -= 1

        if randomizer == small_prize:
            prize = valid_input.get_string(f"!! YOU WON !! Enter name of [SMALL] prize here: ").title()
            small += 1
        elif randomizer == title_prize:
            if title_index != len(titles) - 1:
                new_title = titles[title_index + 1]
                titles.append(new_title)
                print(f"!! YOU WON !! You found new title '{new_title}'!")
            else:
                print("!! YOU WON!! Title already owned!")
            prize = 'New Title'
        elif randomizer == medium_prize:
            prize = valid_input.get_string(f"!! YOU WON !! Enter name of [MEDIUM] prize here: ").title()
            medium += 1
        elif randomizer == big_prize:
            prize = valid_input.get_string(f"!! YOU WON !! Enter name of [BIG] prize here: ").title()
            big += 1
        else:
            print("Miss!")
            prize = None 
            ttl_miss += 1
        
        if prize is not None:
            prizes.append(prize)

        if tickets > 0:
            ans = valid_input.get_choice("Re-roll (y/n)? ", yn)
            if ans in yn[4:]:
                print("Exiting... ")
                print(f"Rolls: {rolls} | Misses: {ttl_miss} | Scores: small {small} | medium: {medium} | big: {big}")
                print("Thank you for playing!")
                return tickets, rolls, ttl_miss, small, medium, big, ", ".join(prizes), titles
            # print(f"Rolls: {rolls} | Misses: {ttl_miss} | Scores: small {small} | medium: {medium} | big: {big}")
            print("Re-rolling...")

    print("You ran out of tickets!")
    print(f"Rolls: {rolls} | Misses: {ttl_miss} | Scores: small {small} | medium: {medium} | big: {big}")
    print("Thank you for playing!")
    return tickets, rolls, ttl_miss, small, medium, big, ", ".join(prizes), titles
