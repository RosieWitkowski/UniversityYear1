player_health = 100 
# --- Bugged code ---
def take_damage():
    player_health = 90
    print("Player took damage!")

take_damage()
print(f"Player health is {player_health}")

# --- Fixed code ---
DAMAGE = 20

def take_damage(player_health):
    print("Player took damage!")
    return player_health - DAMAGE

player_health = 100     
player_health = take_damage(player_health)
print(f"Player health is {player_health}")