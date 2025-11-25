products = [
    {'item':'cookie', 'price':1.00},
    {'item':'brownie', 'price':2.50},
    {'item':'cheesecake', 'price':2.75},
    {'item':'trifle', 'price':3.00}
]

print("+-- Price List --+")
for product in products:
    print(f"{product['item']} -- £{product['price']:.2f}")