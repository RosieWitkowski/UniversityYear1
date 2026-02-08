import input_handler as valid_input 

def shop(points: int, tickets: int) -> tuple[int, int]:
    menu = f"+= Menu =+\nB - Buy tickets\nP - Add/Remove points\nE - Exit\n"
    options = ['b', 'buy', 'ticket', 'tickets', 'buy tickets', 'add', 'remove', 'a', 'r', 'points', 'p', 'add points', 'remove points', 'add/remove', 'e', 'exit', 'quit', 'q']
    option = valid_input.get_choice(menu, options)

    if option in ['e', 'exit', 'quit', 'q']:
        print("Exiting...")
        return points, tickets, None 
    
    if option in options[:5]:
        points, tickets = buy_ticket(points, tickets)
        return points, tickets, None 
    else:
        points, change = change_points(points)
        return points, tickets, change 

def buy_ticket(points: int, tickets: int) -> tuple[int, int]:
    cost_per_ticket = 150
    while points >= cost_per_ticket:
        yn = ['y', 'yes', 'confirm', 'n', 'no']
        buy = valid_input.get_choice(f"Points balance: {points} | Tickets: {tickets}\nBuy ticket (yn)? ", yn)
        if buy in yn[:2]:
            tickets += 1
            points -= cost_per_ticket
            print("Ticket bought sucessfully!")
        else:
            print("Purchace cancelled!")
            return points, tickets
    print(f"Cannot afford more! Exiting ticket shop... (Points: {points} | Tickets {tickets})")
    return points, tickets
    

def change_points(points: int) -> tuple[int, int]:
    menu = f"Would you like to \nA - Add points\nR - Remove (accidental) points\n"
    # Includes B as an option for remove, as some users may assume that the second option is B if the first starts with an A
    options = ['a', 'add', 'add points', 'b', 'r', 'remove', 'remove points', 'remove (accidental) points', 'remove accidental points']
    option = valid_input.get_choice(menu, options)
    amount = valid_input.get_int("Amount to change by: ", 0, 1000)

    if option in options[:3]:
        points += amount
        print(f"Success! Points: {points}")
        return points, None
    else:
        if amount > points:
            yn = ['y', 'yes', 'n', 'no']
            warning = valid_input.get_choice("WARNING: This will take your points into negative. Proceed? ", yn)
            if warning in yn[2:]:
                print("Cancelled!")
                return points, amount 
        points -= amount
        print(f"Success! Points: {points}")
        return points, amount
    