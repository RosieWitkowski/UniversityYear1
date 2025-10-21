from time import sleep 

def valNum(rangMin, rangMax, mesg):
    # Validates input is an integar and within (inclusive) the range given
    num = rangMax + 10
    while not str(num).isnumeric() or not(num >= rangMin and num <= rangMax):
        try: 
            num = int(input(mesg))
        except ValueError:
            print("Invalid input provided.")
    return num 

def game(deaths, survives):
    print("You hear a strange noise coming from the Ancient Manuscripts section. What do you do?")
    choice = valNum(1, 3, "1 - Go to bed\n2 - Run away\n3 - Investigate\n")

    # Bed route - survive
    if choice == 1:
        print("Weirdly enough, you go straight home and into bed.")
        sleep(.5)
        print("You're in bed.")
        sleep (1)
        print("You're asleep.")
        sleep(1)
        print("Zzzzzzz")
        sleep(1)
        print("Zzz")
        sleep(.5)
        
        print("- GAME END! -\nYou survived! Congrats...?")
        survives += 1 
        return deaths, survives
    # Run away route - mixed
    elif choice == 2:
        print("You tremble in your boots. No shame. In the hallway, you reach a fork. What do you do?\n")
        choice = valNum(1, 2, "1 - Sprint around the left corner\n2 - Run down the right corridoor")

        # Left - die
        if choice == 1:
            print("You hurriedly turn the closest corner and...")

            print("- GAME END! -\nYou slammed into a concentrate wall and died! Congrats...?")
            deaths += 1 
            return deaths, survives 
        # Right - mixed
        else:
            print("Well done, you manage to flee down the far right hall and scamper into an open classroom. What will you do next?\n")
            choice = valNum(1, 2, "1 - Hide\n2 - Fight\n")

            # Hide - die
            if choice == 1:
                print("Smart! You're already setelled in for the night. In fact, why not stay forever? You settle into cowardl- domestic life.")
                sleep(1)
                print("...")
                sleep(1)
                print("...")
                sleep(.5)

                print(" - GAME END! -\nYou spent the remainder of an afernoon trembling in the corner of a classroom, before succumbing to the harsh conditions and died.")            
                deaths += 1 
                return deaths, survives 
            # Fight - survive
            else:
                print("Summoning all of your courage, you boldly turn back and walk towards the library.")
                sleep(1)
                print("Your height beats faster... ")
                sleep(.5)
                print("Your steps feel faster, despite your growing hesitation...")
                sleep(.5)
                print("You have arrived.")
                sleep(.5)
                print("On the shelf, lies the book... stationary.")
                sleep(.5)
                print("... it's a book.")
                print("What do you want from me?")
                print("- GAME END! -\nYou survived! Congrats...?")
                survives += 1 
                return deaths, survives 
    # Investiage route - mixed 
    else: 
        print("You summon your courage and walk towards the shelf. You see the book, high on a tower of dusty door stoppers, taunting you with its unassuming paper-ness. What will you do?\n")
        choice = valNum(1, 2, "1 - Grab it\n2 - Accio!!")

        # Grab - die
        if choice == 1:
            print("You attempt to grab the book! Unfortunately, your stubby arms are no match for gravity...")

            print("- GAME END! -\nYou were crushed by a tower of falling books.")
            deaths += 1 
            return deaths, survives 
        # Accio - survive
        elif choice == 2: 
            print("Taking in a deep breath, you authoritavly yell 'ACCIO!!!'")
            sleep(1)
            print("...")
            sleep(.5)
            print("...")
            sleep(.5)

            print("- GAME END! -\nYou're not Harry Potter. Too embarassed to continue, you go home... and survive! Congrats!")
            survives += 1
            return deaths, survives 
        
deaths, survives = 0, 0

play = 1 
while play:
    deaths, survives = game(deaths, survives)
    print(f"- SCORE -\nDeaths: {deaths} Survives: {survives}")
    play = valNum(0, 1, "Play?\n1 - Yes\n0 - No\n")
