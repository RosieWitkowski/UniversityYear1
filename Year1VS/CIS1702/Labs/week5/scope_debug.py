# BROKEN Code Block
player_score = 0 # This is a GLOBAL variable

def add_points(current_score):
    # Bug: This creates a new LOCAL variable
    current_score += 10
    print(f"[Inside Function] Score is now: {player_score}")
    return current_score

# --- Main Program ---
print(f"[Outside] Player score is: {player_score}")
player_score = add_points(player_score)
print(f"[Outside] Player score is: {player_score}") 

