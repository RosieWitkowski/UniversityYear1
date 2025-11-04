# 
def validate_int(msg):
    num = 'A'
    while not num.isnumeric():
        while True:
            try:
                num = input(msg)
                break
            except ValueError:
                print("Please enter an integar.")
    return int(num)

# Repeatedly asks for an input, until an option is provided that's within the given options
def validate_str(msg, options):
    choice = ''
    length = len(options[0]) # How far into input str to compare to options (for alliterative options)
    while choice not in options:
        choice = input(msg)[:length].upper()
    return choice 

# Example usages
validate_int("Number1: ")
validate_str('England/Egypt/Estonia\n', ['EN', 'EG', 'ES'])