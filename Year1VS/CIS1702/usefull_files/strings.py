from time import sleep

# Colour escape sequences 
black, red, yellow, green, blue, magenta, white, reset_colour = '\x1b[30m', '\x1b[31m', '\x1b[33m', '\x1b[32m', '\x1b[34m', '\x1b[35m', '\x1b[37m', "\033[0m"

# Prints from a list of sentences, with a delay between each
def print_delay(msg, delay):
    for sentence in msg:
        print(sentence)
        sleep(delay)

# Example usages
print(red+'RED')
print(blue+'BLUE')
print(reset_colour, end="")

print_delay(['Hello, welcome to the challenge!', 'You must guess every answer correctly...', 'Please take your time!'], .75)