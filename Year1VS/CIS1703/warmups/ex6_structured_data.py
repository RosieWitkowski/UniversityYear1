# Best practice is to group related data rather than in seperate variables

inventory = []
inventory.append({"name": "Wrap", "price": 2.49, "status": 15})
inventory.append({"name": "Crisps", "price": 1.25, "status": 40})
inventory.append({"name": "Apple", "price": 0.24, "status": 35})
inventory.append({"name": "Banana", "price": 0.27, "status": 0})

print("+ --- Unformatted ---+")
print(inventory)

print("+--- Format display ---+")
for item in inventory:
    print(f"Name: {item['name']} | Price: {item['price']} | Stock: ", end="")
    if item['status'] > 0:
        print("In Stock")
    else:
        print("Out of Stock")