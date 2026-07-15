"""A readable alternative to many elif statements (available python 3.10) 
(Note, no considerations made for abbreviations, nicknames, casing, etc. in characters names -
in practice this would be neccesary to check for, but the focus of this code snippet is purely
match-casing)
"""

def check_char(character):
    print(f"======================\nChecking for {character}")
    
    # If-else
    print("> If-else")

    if character == 'Mabel_P' or character == 'Dipper_P':
        print("Twin")
    elif character in ['Wendy', 'Sous', 'Grunkle_S', 'Grunkle_F', 'PNW', 'Bill', 'Gideon', 'Robbie']:
        print("Main character.")
    else:
        print("Other or unkown character")

    # Match case
    print("> Match-case")

    match character:
        case 'Mabel_P' | 'Dipper_P':
            print("Twin")
        case 'Wendy' | 'Sous' | 'Grunkle_S' | 'Grunkle_F' | 'PNW' | 'Bill' | 'Gideon' | 'Robbie':
            print("Main character")
        case _:
            print("Other or unkown character")

check_char('Mabel_P') # Twin
check_char('Grunkle_S') # Main
check_char('Gideon') # Main
check_char('Toby_D') # Side (other/unkown)
check_char('Asdhasjkdhasjkd') # Invalid (other/unkown)