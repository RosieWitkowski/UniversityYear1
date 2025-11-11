# Randomly selects either wizard or chest, with a minimum of 3 wizard interactions required and maximum of 3 misses
from random import randint

play = True 
while play:
    interactions, misses = 0, 0

    while interactions < 3 and misses < 3: 
        randomizer = randint(1, 10)
        if randomizer < 9:
            print("wizard")
            interactions += 1
        else:
            print("chest")
            misses += 1
    
    if interactions < 3:
        for n in range(3 - interactions):
            print("wizard")
            interactions = 3

    print(f"Misses: {misses}")

    if input("Play?")[0].upper() == 'N':
        play = False 


