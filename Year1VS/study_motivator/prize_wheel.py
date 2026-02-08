from random import randint
"""
Based on simulations, chances are (very roughly):
    1/2 - 2/3 : Small prize hit
    1/3 : Miss 
    1/10 - 1/5 : Medium prize hit
    0/100 - 2/100 Big prize hit 
(To maintain these probabilities, keep the number of each type the same else un-commont and re-run for quick estimation)
"""

easy_prizes = ['snack', 'play game', 'watch tv']
medium_prizes = ['buy pens', 'buy game', 'buy book', 'buy small lego']
hard_prizes = ['buy hoodie', 'buy lego']

WIN = 1

def roll_prize(miss: int, small: int, medium: int, big: int) -> tuple[int, int, int, str]:
    if miss == 0:
        for prize in easy_prizes:
            chance = randint(1, 5)
            if chance == WIN:
                print(f"!! YOU WON !! [Small] Prize: {prize}")
                small += 1
                return small, medium, big, prize
    elif miss == 1:
        for prize in medium_prizes:
            chance = randint(1, 10)
            if chance == WIN:
                print(f"!! YOU WON !! [Medium] Prize: {prize}")
                medium += 1
                return small, medium, big, prize
    elif miss == 2:
        for prize in hard_prizes:
            chance = randint(1,100)
            if chance == WIN:
                print(f"!! YOU WON !! [Big] Prize: {prize}")
                big += 1
                return small, medium, big, prize
    return small, medium, big, None 

def wheel() -> tuple[int, int, int, int, int, list[str]]:
    small, medium, big = 0, 0, 0
    rolls, ttl_miss = 0, 0
    prizes = []
    while True:
    # while rolls < 101:
        rolls += 1

        miss = 0
        while miss < 3:
            small, medium, big, prize = roll_prize(miss, small, medium, big)
            miss += 1
            if prize is not None:
                prizes.append(prize)
                break 

        if miss == 3:
            print("Miss!")
            ttl_miss += 1

        try:
            ans = input("Re-roll?(y/n) ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"Rolls: {rolls} | Misses: {ttl_miss} | Scores: small {small} | medium: {medium} | big: {big}")
            print("Cancelled input, exiting...")
            exit()

        if ans == "" or ans in ['n', 'no', 'exit', 'cancell']:
            print(f"Rolls: {rolls} | Misses: {ttl_miss} | Scores: small {small} | medium: {medium} | big: {big}")
            print("Thank you for playing!")
            return rolls, ttl_miss, small, medium, big, prizes

        # print(f"Rolls: {rolls} | Misses: {ttl_miss} | Scores: small {small} | medium: {medium} | big: {big}")
        print("Re-rolling...")
