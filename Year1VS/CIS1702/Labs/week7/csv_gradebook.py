import csv 

studentbook = {
"Alice": [85, 90, 92],
"Bob": [78, 81, 85],
"Charlie": [95, 100, 98]
}

with open('gradebook.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['Student | Grades '])
    
    for student, grades in studentbook.items():
        writer.writerow([student] + grades)

with open('gradebook.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip header row

    for row in reader:
        student, grades = row[0], row[1:]
        avg = 0
        for grade in grades:
            avg += int(grade) 
        avg /= len(grades)
        print(f"{student}: Average Score = {avg:.1f}")