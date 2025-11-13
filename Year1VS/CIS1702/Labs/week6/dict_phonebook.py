phonebook = {}

phonebook["Alice"] = "555-1234"
phonebook["Bob"] = "555-5678"

# Searching
name_search = input("Name: ").capitalize()
number = phonebook.get(name_search)
if number:
    print(f"Number: {number}")
else:
    print("Name not found.")

# Adding 
name, number = input("Name: ").capitalize(), input("Number: ")
phonebook[name] = number

# Printing
for name, number in phonebook.items():
    print(f"{name}: {number}")