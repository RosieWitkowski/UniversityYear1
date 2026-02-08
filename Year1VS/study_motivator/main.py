from prize_wheel import wheel 
import file_manager as file

def main():
    stats = file.load_file('scores.json')
    if stats is None:
        points = 0
        stats = ({
            'total points': 0,
            'current points': 0,
            'spins': 0,
            'total misses': 0,
            'small prizes won': 0,
            'medium prizes won': 0, 
            'big prizes won': 0,
            'prizes won': []
        })
    else:
        try:
            points = stats['total points']
        except KeyError:
            print("Error: Unexpected indexing at stats[points], exiting... ")
            exit()
    
    rolls, ttl_miss, small, medium, big, prizes = wheel()

    try:
        stats['total points'] += points 
        stats['current points'] = points
        stats['spins'] += rolls
        stats['total misses'] += ttl_miss
        stats['small prizes won'] += small
        stats['medium prizes won'] += medium
        stats['big prizes won'] += big
        stats['prizes won'].append(prizes)
    except KeyError:
        print("Error: Unexpected indexing at stats saving, exiting...")
        exit()

    file.save_file(stats, 'scores.json')

if __name__ == "__main__":
    main()