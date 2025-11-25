# 1. Create a List of Dictionaries
# This represents a database of students.
students = [
{"name": "Alice", "score": 85, "passed": True},
{"name": "Bob ❤️❤️❤️❤️", "score": 40, "passed": False},
{"name": "Charlie", "score": 92, "passed": True}
]
# 2. The Loop
# "student" is a temporary variable that holds ONE dictionary at a time.
print("--- Class Results ---")
for student in students:
    # 3. Access specific data using the ["keys"]
    name = student["name"]
    score = student["score"]
    print("Status: Pass") if student['passed'] == True else print("Status: Fail")
    
# 4. Print it nicely
print(f"Student: {name} | Score: {score}")
print("---------------------")