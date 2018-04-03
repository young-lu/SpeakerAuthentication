import json, requests

# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json").json()
data = response
# print(response)
# 9 people are currently in space.
print(data)
