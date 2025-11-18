# The "with" statement is the correct, modern way to handle files.
# It guarantees the file will be closed, even if errors occur.
with open("my_file.txt", "w") as f:
    # 'f' is our file handle
    # 'w' is the mode (write)
    f.write("Hello, world!")
# By the time the code gets here, my_file.txt is automatically closed


# Writing to a .txt file
data_to_save = ["First line", "Second line", "Third line"]
with open("log.txt", "w") as f:
    for line in data_to_save:
        f.write(line + "\n") # Don't forget the newline character!
        # Reading from a .txt file
with open("log.txt", "r") as f:
    lines = f.readlines() # lines = ["First line\n", "Second line\n", ...]
# You often need to strip the \n
clean_lines = [line.strip() for line in lines]
print(clean_lines) # ['First line', 'Second line', 'Third line']


import csv
# Writing to a .csv file
# Data: {'Bob': [85, 90], 'Alice': [92, 88]}
gradebook = {'Bob': [85, 90], 'Alice': [92, 88]}
with open("grades.csv", "w", newline='') as f:
    writer = csv.writer(f)
    for student, scores in gradebook.items():
        writer.writerow([student] + scores) # e.g., ['Bob', 85, 90]
# Reading from a .csv file
new_gradebook = {}
with open("grades.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        # row is always a list of STRINGS: e.g., ['Bob', '85', '90']
        new_gradebook[row[0]] = [int(s) for s in row[1:]]
print(new_gradebook)


import json
# Your Red Thread data structure
project_data = [
{'item': 'Coffee', 'price': 3.50},
{'item': 'Lunch', 'price': 12.00}
]
# Writing to a .json file (Your save_data() function)
with open("data.json", "w") as f:
    json.dump(project_data, f, indent=4) # indent=4 makes it readable!
# Reading from a .json file (Your load_data() function)
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print(loaded_data == project_data) # True


import json
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f) # Load data if file exists
    except FileNotFoundError:
        print("No save file found. Starting fresh.")
        return [] # Return an empty list
    except json.JSONDecodeError:
        print("Save file is corrupted! Starting fresh.")
        return [] # Also return an empty list
# Program Start
my_project_data = load_data()



