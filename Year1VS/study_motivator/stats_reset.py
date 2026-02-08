import input_handler as valid_input

def reset(stats: list[dict]) -> list[dict]:
    # Alternatives such as 'y' are not accepted here, as safety takes precidence over convenience for this action
    yn = ['yes','n', 'no', 'exit', 'cancel']
    confirm1 = valid_input.get_choice(f"! Are you sure you want to reset your stats? Type 'yes' to confirm or 'no' to cancel !\n", yn)
    if confirm1 != 'yes':
        print("Reset cancelled.")
        return stats, None 

    passcode = 'I am sure 123'
    confirm2 = valid_input.safe_input(f"!! This will reset ALL stats, are you compltely sure? Type EXACTLY '{passcode}' to confirm or 'no' to cancel !!\n")
    if confirm2 != passcode:
        print("Reset cancelled.")
        return stats, None 

    print("Reset confirmed, reseting stats... ")
    for key, value in stats.items():
        try:
            if key == 'title':
                stats[key] = 'Noob'
                continue 
        except KeyError:
            print("Unexpected indexing for stats, exiting... ")
            exit()
        try:
            if key == 'prizes won':
                stats[key] = []
                continue 
        except KeyError:
            print("Unexpected indexing for stats, exiting... ")
            exit()
        stats[key] = 0

    print("Stats reset.")
    return stats, 'confirmed'