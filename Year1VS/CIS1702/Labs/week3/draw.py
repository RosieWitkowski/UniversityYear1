symbol = input("Symbol: ") # e.g. '#', '*', 'A'

# Square 
rows, cols = 3, 3
for i in range(rows):
    for j in range (cols):
        print(symbol, end="")
    print()

# Triangle
try:
    rows = int(input("Size: "))
except ValueError:
    print("Invalid input")

for i in range(1, rows+1):
    print(symbol * i)