import requests # Import the tool to talk to the web

url = "https://official-joke-api.appspot.com/random_joke"

# 1. Send the request
print("Calling the server...")
response = requests.get(url)
# 2. Check the Status Code (200 = Success, 404 = Not Found)
print(f"Status Code: {response.status_code}")
# 3. See the raw text data
print("Raw Data:")
print(response.text)