# Data may include optional fields, should consider this when accessing data to avoid crashes

print("+--- LBYL ---+\n(Best for this context)")

# Original code 
user_data = {"name": "Alice", "role": "Admin"}
 
"""
dept = user_data["department"]  -> Outputs KeyError
print(f"Department: {dept}")
"""

# Fixed (adding defensive code)
user_data = {"name": "Alice", "role": "Admin"}
user_data2 = {"name": "Bob", "role": "UI Designer", "department": "Design"}

dept = user_data.get("department")
if dept:
    print(f"Department: {dept}")
else:
    print("Department not found.")

dept = user_data2.get("department")
if dept:
    print(f"Department: {dept}")
else:
    print("Department not found.")

print("\n+--- EAFF ---+\n(Outputs the same, but typically not used in this context)")

try:
    dept = user_data["department"]
    print(f"Department: {dept}")
except KeyError:
    print("Department not found.")

try:
    dept = user_data2["department"]
    print(f"Department: {dept}")
except KeyError:
    print("Department not found.")
