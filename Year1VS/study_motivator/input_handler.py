def safe_input(prompt: str) -> str:
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("Error: User cancelled input")
        return ""
    
def get_string(prompt: str) -> str:
    while True:
        user_input = safe_input(prompt).strip().lower()
        if user_input == "":
            print("Error: input cannot be empty")
            continue 
        return user_input 

def get_choice(prompt: str, options) -> str:
    while True:
        choice = get_string(prompt)
        if choice not in options:
            print(f"Please select from the provided options ({options})")
            continue
        return choice 
    
def get_int(prompt: str, min: int, max: int) -> int:
    while True:
        num = get_string(prompt)
        try:
            num = int(num)
        except ValueError:
            print("Error: input must be numeric.")
            continue 
        if min is not None:
            if num < min:
                print(f"Error: number must be at least {min}")
                continue 
        if max is not None:
            if num > max:
                print(f"Error: number must be at most {max}")
                continue 
        return num 