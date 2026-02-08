import json 

def save_file(data, filename: str) -> None:
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        print("> File saved sucessfully")


def load_file(filename: str) -> list[dict]:
    try:
        with open(filename, 'r') as f:
            print("> File loaded successfully")
            return json.load(f)
    except FileNotFoundError:
        print("[!] Error: File could not be found.")
        return None 
    except json.JSONDecodeError:
        print("[!] Error: File corrupted.")
        return None 
    return None 
