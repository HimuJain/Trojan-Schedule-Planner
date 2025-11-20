import requests
import json

dataListList = []
for i in range(9):
    a = i//3
    b = (i%3) + 1
    termCode = 20230 + (a*10) + b
    url = f"https://classes.usc.edu/api/Programs/TermCode?termCode={termCode}"
    response = requests.get(url)
    # print(response.status_code)  # Should print 200 if the request was successful
    # print(response.json())  # Print the JSON response from the API

    data = response.json()

    dataList = []

    for item in data:
        print(item["schools"][0]["prefix"], ":", item["prefix"])
        dataList.append((item["schools"][0]["prefix"], item["prefix"]))
    dataListList.append(dataList)
    print(termCode)

    # # print(data[1]["schools"][0]["prefix"])
    # # print(data[1]["prefix"])

    # # Programs = json.loads(data)

    # # print(Programs)
    for school, program in dataList:
        print(school, " ", program)
        url = f"https://classes.usc.edu/api/Courses/CoursesByTermSchoolProgram?termCode={termCode}&school={school}&program={program}"
        response = requests.get(url)
        data = response.json()
        for item in data['courses']:
            print(item['fullCourseName'], item['description'], item['courseUnits'][0])
            for section in item['sections']:
                print("  ", section['sisSectionId'], section['instructors'])
        



# import requests
# import csv

# # Gather data for 9 terms
# dataListList_schools = []
# dataListList_programs = []
# termCodes = []

# for i in range(9):
#     a = i // 3
#     b = (i % 3) + 1
#     termCode = 20230 + (a * 10) + b
#     termCodes.append(str(termCode))

#     url = f"https://classes.usc.edu/api/Programs/TermCode?termCode={termCode}"
#     response = requests.get(url)
#     data = response.json()

#     schools = {}
#     programs = {}

#     for item in data:
#         # --- School ---
#         if "schools" in item and item["schools"]:
#             school = item["schools"][0]
#             school_prefix = school.get("prefix")
#             school_name = school.get("name")
#             if school_prefix and school_name:
#                 schools[school_prefix] = school_name

#         # --- Program ---
#         program_prefix = item.get("prefix")
#         program_name = item.get("name")
#         if program_prefix and program_name:
#             # If linked to a school, record it
#             school_prefix = (
#                 item["schools"][0]["prefix"]
#                 if "schools" in item and item["schools"]
#                 else None
#             )
#             programs[program_prefix] = {
#                 "name": program_name,
#                 "school": school_prefix,
#             }

#     dataListList_schools.append(schools)
#     dataListList_programs.append(programs)

# # --- Write Schools CSV ---
# def write_schools_csv(filename, dataListList, termCodes):
#     all_codes = sorted({code for d in dataListList for code in d.keys()})
#     name_map = {code: name for d in dataListList for code, name in d.items()}

#     with open(filename, "w", newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(["Code", "Name"] + termCodes)

#         for code in all_codes:
#             row = [code, name_map.get(code, "")]
#             for d in dataListList:
#                 row.append("Y" if code in d else "")
#             writer.writerow(row)


# # --- Write Programs CSV ---
# def write_programs_csv(filename, dataListList, termCodes):
#     all_codes = sorted({code for d in dataListList for code in d.keys()})
#     name_map = {code: d[code]["name"] for d in dataListList for code in d.keys()}

#     with open(filename, "w", newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(["Code", "Name"] + termCodes)

#         for code in all_codes:
#             row = [code, name_map.get(code, "")]
#             for d in dataListList:
#                 if code in d:
#                     school_prefix = d[code]["school"]
#                     cell = f"{school_prefix}" if school_prefix else "Y"
#                 else:
#                     cell = ""
#                 row.append(cell)
#             writer.writerow(row)


# # --- Generate CSVs ---
# write_schools_csv("schools.csv", dataListList_schools, termCodes)
# write_programs_csv("programs.csv", dataListList_programs, termCodes)

# print("✅ Finished generating schools.csv and programs.csv")
# import requests
# import csv

# # --- Step 1: Fetch data for all terms ---

# dataListList_schools = []
# dataListList_programs = []
# termCodes = []

# for i in range(18):
#     a = i // 3
#     b = (i % 3) + 1
#     termCode = 20200 + (a * 10) + b
#     termCodes.append(str(termCode))

#     url = f"https://classes.usc.edu/api/Programs/TermCode?termCode={termCode}"
#     response = requests.get(url)
#     data = response.json()

#     schools = {}
#     programs = {}

#     for item in data:
#         # --- School ---
#         if "schools" in item and item["schools"]:
#             school = item["schools"][0]
#             school_prefix = school.get("prefix")
#             school_name = school.get("name")
#             if school_prefix and school_name:
#                 schools[school_prefix] = school_name

#         # --- Program ---
#         program_prefix = item.get("prefix")
#         program_name = item.get("name")
#         if program_prefix and program_name:
#             school_prefix = (
#                 item["schools"][0]["prefix"]
#                 if "schools" in item and item["schools"]
#                 else None
#             )
#             programs[program_prefix] = {
#                 "name": program_name,
#                 "school": school_prefix,
#             }

#     dataListList_schools.append(schools)
#     dataListList_programs.append(programs)

# # --- Step 2: Write schools.csv ---
# def write_schools_csv(filename, dataListList, termCodes):
#     all_codes = sorted({code for d in dataListList for code in d.keys()})
#     name_map = {code: name for d in dataListList for code, name in d.items()}

#     with open(filename, "w", newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(["Code", "Name"] + termCodes)

#         for code in all_codes:
#             row = [code, name_map.get(code, "")]
#             for d in dataListList:
#                 row.append("Y" if code in d else "")
#             writer.writerow(row)

# # --- Step 3: Write programs.csv ---
# def write_programs_csv(filename, dataListList, termCodes):
#     all_codes = sorted({code for d in dataListList for code in d.keys()})
#     name_map = {code: d[code]["name"] for d in dataListList for code in d.keys()}

#     with open(filename, "w", newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(["Code", "Name"] + termCodes)

#         for code in all_codes:
#             row = [code, name_map.get(code, "")]
#             for d in dataListList:
#                 if code in d:
#                     school_prefix = d[code]["school"]
#                     cell = f"Y {school_prefix}" if school_prefix else "Y"
#                 else:
#                     cell = ""
#                 row.append(cell)
#             writer.writerow(row)

# # --- Step 4: Write program_school_changes.csv ---
# def write_school_changes_csv(filename, dataListList, termCodes):
#     all_codes = sorted({code for d in dataListList for code in d.keys()})
#     name_map = {code: d[code]["name"] for d in dataListList for code in d.keys()}

#     changes = {}
#     for code in all_codes:
#         prev_school = None
#         row_cells = []
#         changed = False
#         missing_term = False

#         for d in dataListList:
#             if code in d:
#                 current_school = d[code]["school"]
#                 if prev_school is None:
#                     # First appearance
#                     row_cells.append(current_school if current_school else "")
#                 elif current_school == prev_school:
#                     row_cells.append("---")
#                 else:
#                     row_cells.append(current_school if current_school else "")
#                     changed = True
#                 prev_school = current_school
#             else:
#                 row_cells.append("")
#                 missing_term = True

#         # Include if either a change occurred OR it was missing in any term
#         if changed or missing_term:
#             changes[code] = row_cells

#     with open(filename, "w", newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(["Code", "Name"] + termCodes)
#         for code, row_cells in changes.items():
#             writer.writerow([code, name_map.get(code, "")] + row_cells)


# # --- Step 5: Generate all CSVs ---
# write_schools_csv("schools.csv", dataListList_schools, termCodes)
# write_programs_csv("programs.csv", dataListList_programs, termCodes)
# write_school_changes_csv("program_school_changes.csv", dataListList_programs, termCodes)

# print("✅ Generated: schools.csv, programs.csv, and program_school_changes.csv")
