# This simulates data we might get from a User API
fake_api_data = {
    "status": "success",
    "total_results": 2,
    "users": [
        {"id": 1, "name": "John", "contact": {"email": "john@test.com"}},
        {"id": 2, "name": "Jane", "contact": {"email": "jane@test.com"}}
    ]
}
# HINT:
# 1. Access the "users" list first: fake_api_data["users"]
# 2. Access the second item (index 1): ... [1]
# 3. Access the "contact" dictionary: ... ["contact"]
# 4. Access the "email" key: ... ["email"]

# Write your print statement here:
# print(fake_api_data......)

jane_email = fake_api_data['users'][1]['contact']
print(jane_email)


users = fake_api_data['users']
for user in users:
    print(f"{user['name']} | Contact: {user['contact']}")

