import requests
import json
from nltk.tokenize import RegexpTokenizer
import os
from dotenv import load_dotenv
import re




def instructorValidity(profFirstName, profLastName):
    headers = {
        'X-Requested-With': 'XMLHttpRequest'
    }

    params = {
        'basic': f"{profFirstName} {profLastName}",
    }

    response = requests.get(
        'https://uscdirectory.usc.edu/web/directory/faculty-staff/proxy.php',
        params=params,
        headers=headers,
    )

    resp = response
    # print("Status:", resp.status_code)
    # print("Content-Type:", resp.headers.get("Content-Type"))
    # print("Length:", len(resp.text))
    # print(resp.json())
    data = resp.json()
    if type(data) is list:
        counter = 0
        for person in data:
            tokenizer = RegexpTokenizer(r'\w+')
            name_set = set(tokenizer.tokenize(person['displayname'][0]))
            if profFirstName in name_set and profLastName in name_set:
                counter += 1
        if counter == 1:
            return True, data
        else:
            return False, data
        # for person in data:
        #     print(person['displayname'])
    else:
        return True, data
        # print(data)

def buildingScraper():
    load_dotenv()
    map_api_key = os.getenv("NODE_MAP_API_KEY")

    url = "https://api.concept3d.com/categories/53722?map=1928&children&key=0001085cc708b9cef47080f064612ca5"
    response = (requests.get(url)).json()
    # print(response.status_code) 
    print(len(response["children"]["locations"]))
    for location in response["children"]["locations"]:
        clean = re.sub(r"\s*\([^()]*\)$", "", location["name"])
        print(clean)
        if location.get("reference"):
            print(location["reference"][0])
            print(location["lng"], location["lat"])
            url = f"https://geocode.maps.co/reverse?lat={location['lat']}&lon={location['lng']}&api_key={map_api_key}"
            address = (requests.get(url))
            if address.status_code == 200:
                address = address.json()
            else:
                print("error")
                address = {}
            print(address.get("display_name"))
        



def main():
    buildingScraper()
    dataListList = []
    for i in range(9):
        a = i//3
        b = (i%3) + 1
        termCode = 20230 + (a*10) + b
    termCode = 20253
    url = f"https://classes.usc.edu/api/Programs/TermCode?termCode={termCode}"
    response = requests.get(url)
    # print(response.status_code)  # Should print 200 if the request was successful
    # print(response.json())  # Print the JSON response from the API

    data = response.json()

    dataList = []

    for item in data:
        # print(item["schools"][0]["prefix"], ":", item["prefix"])
        dataList.append((item["schools"][0]["prefix"], item["prefix"]))
    dataListList.append(dataList)
    # print(termCode)

    for school, program in dataList:
        print(school, " ", program)
        url = f"https://classes.usc.edu/api/Courses/CoursesByTermSchoolProgram?termCode={termCode}&school={school}&program={program}"
        response = requests.get(url)
        data = response.json()
        for item in data['courses']:
            # print(item['fullCourseName'], item['description'], item['courseUnits'][0])
            for section in item['sections']:
                # print("  ", section['sisSectionId'])
                for instructor in section['instructors']:
                    # print(instructor['firstName'], instructor['lastName'])
                    results = instructorValidity(instructor['firstName'], instructor['lastName'])
                    if not results[0]:
                    #     print("Good")
                    # else:
                        print(f"Multiple Results Found for {section['sisSectionId']} in Course {item['fullCourseName']} with Instructor {instructor['firstName']} {instructor['lastName']}")
        


if __name__ == "__main__":
    main()