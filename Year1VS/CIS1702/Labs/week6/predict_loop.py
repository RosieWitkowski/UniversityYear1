total_actions = 0
player_level = 1

# A while loop that runs for levels 1, 2, and 3
while player_level < 4:
    print(f"Processing Level {player_level}...")

    # A nested for loop that runs 'player_level' times
    # e.g., for level 3, it runs 3 times (0, 1, 2)
    for action in range(player_level):
        total_actions = total_actions + 1
    
    player_level = player_level + 1

print(f"Total actions: {total_actions}")


# Expected output: 
'''
> Processing Level 1...
> Processing Level 2...
> Processing Level 3...
> Total actions: 6
'''
    