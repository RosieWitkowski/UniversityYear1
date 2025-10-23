def valStr(options, msg):
    choice = ' '
    while choice not in options:
        choice = input(msg)
        choice = choice[0].upper()
    return choice

def main():
    choice = ""
    while choice != 'Q':
        choice = valStr(['A', 'S', 'Q'], "1. Add\n2. Subtract\n3. Quit\n")
        if choice == 'A':
            x, y = int(input("X: ")), int(input("Y: "))
            print(x + y)
        elif choice == 'S':
            x, y = int(input("X: ")), int(input("Y: "))
            print(x - y)
    print("Exiting")
main()