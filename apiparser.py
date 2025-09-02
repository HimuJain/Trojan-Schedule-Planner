import requests
import json

url = "https://classes.usc.edu/api/Programs/TermCode?termCode=20253"
response = requests.get(url)

# print(response.status_code)  # Should print 200 if the request was successful
# print(response.json())  # Print the JSON response from the API

data = response.json()

dataList = []

for item in data:
    print(item["schools"][0]["prefix"])
    print(item["prefix"])
    dataList.append((item["schools"][0]["prefix"], item["prefix"]))

# print(data[1]["schools"][0]["prefix"])
# print(data[1]["prefix"])

# Programs = json.loads(data)

# print(Programs)
for school, program in dataList:
    url = f"https://classes.usc.edu/api/Courses/CoursesByTermSchoolProgram?termCode=20253&school={school}&program={program}"
    response = requests.get(url)
    data = response.json()
    