import requests
import json
from nltk.tokenize import RegexpTokenizer
import os
from dotenv import load_dotenv
import re




def instructorValidity(profFirstName, profLastName):
    response = requests.get(
        'https://uscdirectory.usc.edu/web/directory/faculty-staff/proxy.php',
        params={'basic': f"{profFirstName} {profLastName}"} ,
        headers={'X-Requested-With': 'XMLHttpRequest'} ,
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

    buildingList = []

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
                address = (address.json()).get("display_name")
            else:
                print("error")
                address = ""
            building = {
                "build_id": location["reference"][0],
                "build_add": address,
                "build_name": clean,
                "build_long": location["lng"],
                "build_lat": location["lat"],
            }
            print(building)
            buildingList.append(building)
        
    return buildingList

def main():
    # buildingScraper()
    dataListList = []
    # for i in range(9):
    #     a = i//3
    #     b = (i%3) + 1
    #     termCode = 20230 + (a*10) + b
    termCode = 20253
    url = f"https://classes.usc.edu/api/Schools/TermCode?termCode={termCode}"
    response = requests.get(url)
    # print(response.status_code)  # Should print 200 if the request was successful
    # print(response.json())  # Print the JSON response from the API

    data = response.json()

    dataList = []
    schoolList = []
    for school in data:
        programList = []
        schoolPrefix = school["prefix"]
        for program in school["programs"]:
            courseList = []
            programPrefix = program["prefix"]

            url = f"https://classes.usc.edu/api/Courses/CoursesByTermSchoolProgram?termCode={termCode}&school={schoolPrefix}&program={programPrefix}"
            response = requests.get(url)
            data = response.json()

            for item in data['courses']:
                if(item["isCrosslisted"]):
                    continue
                # print(item['fullCourseName'], item['description'], item['courseUnits'][0])
                sectionList = []
                for section in item['sections']:
                    # print("  ", section['sisSectionId'])
                    instructorList = []
                    for instructor in section['instructors']:
                        # print(instructor['firstName'], instructor['lastName'])
                        instructor = {
                            "instr_first": instructor['firstName'],
                            "instr_last": instructor['lastName']
                        }
                        instructorList.append(instructor)
                    sectionData = {
                        # ! dclearance added to id, or to true/false?
                        "sct_id": section['sisSectionId'],
                        "sct_type": section['rnrMode'],
                        "sct_reg": section['registeredSeats'],
                        "sct_seats": section['totalSeats'],
                        "sct_title": "" if section.get("name") is None else section['name'],
                        # ! handle sct_units later too
                        "sct_instructors": instructorList,
                    }
                    sectionList.append(sectionData)
                course = {
                    "crs_code": item["scheduledCourseCode"]["courseHyphen"]+item["suffix"],
                    # CSCI-104L (for now)
                    "crs_name": item["name"],
                    "crs_desc": item["description"],
                    "crs_geaf": "", # ! to be added later
                    "crs_gegh": "", # ! to be added later
                    "crs_dcorelit" : "", # ! to be added later
                    # ! change logic for crs_unitstr, because there should be a selected range
                    "sections": sectionList
                }
            # print(school["prefix"], ":", program["prefix"])
            program = {
                "prgrm_id": programPrefix,
                "prgrm_name": program["name"],
                "courses": courseList,
            }
            programList.append(program)
        school = {
            "school_id": schoolPrefix,
            "school_name": school["name"],
            "programs": programList,
        }

        
        # print(item["schools"][0]["prefix"], ":", item["prefix"])
        print(school["prefix"], ":", program["prefix"])
        dataList.append((school["prefix"], program["prefix"]))
    dataListList.append(dataList)
    # print(termCode)

    for school, program in dataList:
        print(school, " ", program)
        url = f"https://classes.usc.edu/api/Courses/CoursesByTermSchoolProgram?termCode={termCode}&school={school}&program={program}"
        response = requests.get(url)
        data = response.json()
        for item in data['courses']:
            print(item['fullCourseName'], item['description'], item['courseUnits'][0])
            for section in item['sections']:
                print("  ", section['sisSectionId'])
                print("nope" if section.get("name") is None else section['name'])
                for instructor in section['instructors']:
                    # print(instructor['firstName'], instructor['lastName'])
                    results = instructorValidity(instructor['firstName'], instructor['lastName'])
                    if not results[0]:
                    #     print("Good")
                    # else:
                        print(f"Multiple Results Found for {section['sisSectionId']} in Course {item['fullCourseName']} with Instructor {instructor['firstName']} {instructor['lastName']}")
        


if __name__ == "__main__":
    main()