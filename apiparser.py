import requests
import json

url = "https://classes.usc.edu/api/Programs/TermCode?termCode=20253"
response = requests.get(url)

# print(response.status_code)  # Should print 200 if the request was successful
# print(response.json())  # Print the JSON response from the API

data = response.json()
print(data[1])

# Programs = json.loads(data)

# print(Programs)