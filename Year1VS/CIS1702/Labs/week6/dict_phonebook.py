phonebook = {}

phonebook["Alice"] = "555-1234"
phonebook["Bob"] = "555-5678"

# Searching
name_search = input("Name: ").capitalize()
if name_search in phonebook:
    print(f"Number: {phonebook[name_search]}")
else:
    print("Name not found.")

# Adding 
name, number = input("Name: ").capitalize(), input("Number: ")
phonebook[name] = number

# Printing
for name, number in phonebook.items():
    print(f"{name}: {number}")