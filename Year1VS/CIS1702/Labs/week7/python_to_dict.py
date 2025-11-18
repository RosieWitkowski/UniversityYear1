import json

# A list of dictionaries (simulating a project inventory or expense list)
starter_inventory = [
    {"id": 1, "name": "Wooden Sword", "rank": 'F'},
    {"id": 2, "name": "Wooden Shield", "rank": 'F'}
]

def save_inventory(inventory):
    with open('inventory.json', 'w') as f:
        json.dump(inventory, f, indent=4)
        print("> Inventory saved")

def print_inventory():
    with open('inventory.json', 'r') as f:
        inventory = json.load(f)
        for item in inventory:
            print(f"{item['name']} | Rank: {item['rank']} ID: {item['id']}")

def load_inventory():
    try:
        with open('inventory.json', 'r') as f:
            print("> Inventory loaded")
            return json.load(f)
    except FileNotFoundError:
        print("| No existing inventory found |\nCreating new inventory")
        return False
    except json.JSONDecodeError:
        print("| ERROR: File corrupted |\nCreating new inventory")
        return False

def delete_item(id, inventory):
    for i, row in enumerate(inventory):
        if row['id'] == id:
            inventory.pop(i)
            print('> Item deleted')
            save_inventory(inventory)
            return
    else:
        print("ERROR: Item not found")
        return 

def add_item(item):
    for row in inventory:
        if item['id'] == row['id']:
            print(f"> {item['name']} already owned")
            return 

    inventory.append(item)
    with open('inventory.json', 'w') as f:
        json.dump(inventory, f, indent=4)
        print(f"> {item['name']} added")
        save_inventory(inventory)

print("-- + Loading Inventory + --")
inventory = load_inventory()
if inventory == False:
    save_inventory(starter_inventory)
    inventory = load_inventory()
print_inventory()

print("-- + Inventory After Losing Item + --")
delete_item(int(input("ID to delete: ")), inventory)
print_inventory()

print("-- + Inventory After Gaining Items + --")
item = {"id": 2, "name": "Wooden Shield", "rank": 'D'}
add_item(item)
item = {"id": 5988124, "name": "The Ultimate Sword of Stabbing", "rank": 'A++'}
add_item(item)
item = {"id": 418198, "name": "Gold Axe", "rank": 'C'}
add_item(item)

inventory = load_inventory()
print_inventory()

print("-- + Inventory After Reset + --")
if input("Reset inventory to start default? ")[0].upper().strip() == 'Y':
    save_inventory(starter_inventory)
    print_inventory()
