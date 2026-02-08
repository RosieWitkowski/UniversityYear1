from prize_wheel import wheel 
import file_manager as file
import input_handler as valid_input
from shop import shop
import stats_reset

def main():
    # Loading/initializing stats
    stats = file.load_file('scores.json')
    if stats is None:
        points = 0
        stats = ({
            'title': 'Noob',
            'total points': 0,
            'current points': 0,
            'current tickets': 0,
            'spins': 0,
            'total misses': 0,
            'small prizes won': 0,
            'medium prizes won': 0, 
            'big prizes won': 0,
            'prizes won': []
        })
    try:
        title = stats['title'] 
        points = stats['current points']
        tickets = stats['current tickets'] 
    except KeyError:
        print("Error: Unexpected indexing at stats initialization, exiting... ")
        exit()

    print("Welcome to StudyMotivator.IO!")
    while True:
        # Spinning wheel or opening shop
        print("+= MENU =+\nWhat would you like to do?")
        print(f"Points: {points} | Tickets: {tickets}")
        modes = ['o', 'open', 'shop', 's', 'open shop', 'wheel', 'w', 'open wheel', 'spin wheel', 'reset', 'r', 'reset stats']
        mode = valid_input.get_choice("\nS - Open shop\nW - Spin wheel\nR - Reset stats\n", modes)

        # Shop
        if mode in modes[:5]:
            points, tickets, change = shop(points, tickets)
            try:
                stats['current points'] = points 
                stats['current tickets'] = tickets 
                if change is not None:
                    stats['total points'] -= change 
                else:
                    stats['total points'] += points 
            except KeyError:
                print("Error: Unexpected indexing at stats shop saving, exiting...")
                print(f"> Stats dump: {tickets, rolls, ttl_miss, small, medium, big, prizes}")
                exit()
        # Prize wheel 
        elif mode in modes[5:9]:
            tickets, rolls, ttl_miss, small, medium, big, prizes = wheel(tickets, points)
            try:
                stats['title'] = title 
                stats['total points'] += points 
                stats['current points'] = points
                stats['current tickets'] = tickets 
                stats['spins'] += rolls
                stats['total misses'] += ttl_miss
                stats['small prizes won'] += small
                stats['medium prizes won'] += medium
                stats['big prizes won'] += big
                if prizes is not None:
                    stats['prizes won'].append(prizes)
            except KeyError:
                print("Error: Unexpected indexing at stats saving, exiting...")
                print(f"> Stats dump: {tickets, rolls, ttl_miss, small, medium, big, prizes}")
                exit()
        # Reset stats 
        else:
            stats, reset = stats_reset.reset(stats)
            if reset is not None:
                if reset == 'confirmed':
                    print("Thank you for using StudyMotivator.IO! Saving your stats and exiting...")
                    file.save_file(stats, 'scores.json')
                    exit() 


        yn = ['y', 'yes', 'continue', 'c', 'n', 'no', 'exit', 'cancel']
        ans = valid_input.get_choice("Continue (y/n)? ", yn)
        if ans in yn[4:]:
            print("Thank you for using StudyMotivator.IO! Saving your stats...")
            file.save_file(stats, 'scores.json')
            break 


if __name__ == "__main__":
    main()