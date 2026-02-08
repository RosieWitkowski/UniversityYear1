import input_handler as input 

def shop(points: int, tickets: int) -> tuple[int, int]:
    menu = f"+= Menu =+\nB - Buy tickets\nP - Add/Remove points\n"
    options = ['b', 'buy', 'ticket', 'tickets', 'buy tickets', 'add', 'remove', 'a', 'r', 'points', 'p', 'add points', 'remove points', 'add/remove']
    option = input.get_choice(menu, options)

    if option in options[:5]:
        points, tickets = buy_ticket()
        return points, tickets
    else:
        points = change_points(points)
        return points, tickets

def buy_ticket():
    return 0, 0 

def change_points(points: int):
    menu = f"Would you like to \nA - Add points\nR - Remove (accidental) points\n"
    # Includes B as an option for remove, as some users may assume that the second option is B if the first starts with an A
    options = ['a', 'add', 'add points', 'b', 'r', 'remove', 'remove points', 'remove (accidental) points', 'remove accidental points']
    option = input.get_choice(menu, options)
    amount = input.get_int("Amount to change by: ", 0, 1000)

    if option in options[:3]:
        return points + amount 
    else:
        if amount > points:
            yn = ['y', 'yes', 'n', 'no']
            warning = input.get_choice("WARNING: This will take your points into negative. Proceed? ", yn)
            if warning in yn[2:]:
                print("Cancelled!")
                return points 
        return points - amount 
    
p, t = shop(0, 0)
print(p, t)