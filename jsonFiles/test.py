import requests
import json



for i in range(18):
    yearOnes = (i % 3) + 1
    yearTens = (i // 3)
    year = 20200 + yearTens * 10 + yearOnes

year = 20253

url = f"https://classes.usc.edu/api/Schools/TermCode?termCode={year}"
response = requests.get(url)
response = response.json()



for item in response:
    print(item["prefix"] + ": " + item["name"])
    print("  Programs:")

    for program in item["programs"]:
        print("    " + program["prefix"] + ": " + program["name"])

    # print(item["schools"][0]["prefix"] + " " + item["prefix"])

# print(data[1]["schools"][0]["prefix"])
# print(data[1]["prefix"])


# Programs = json.loads(data)

# print(Programs)

def find_multi_schedule_courses(data):
    courses_with_multi = set()  # use a set to avoid duplicates

    for course in data.get("courses", []):
        # print("new course")
        for section in course.get("sections", []):
            schedule = section.get("schedule", [])
            if len(schedule) > 1:
                courses_with_multi.add(course.get("fullCourseName"))
                # print(course.get("fullCourseName"))
                locs = [s.get("location") for s in schedule]
                days = [s.get("dayCode") for s in schedule]
                start_times = [s.get("startTime") for s in schedule]
                end_times = [s.get("endTime") for s in schedule]
                same_locations = len(set(locs)) == 1

                print(course.get("fullCourseName") + ":")
                for i in range(len(locs)):
                    print(f"  Location: {locs[i]}, Days: {days[i]}, Start: {start_times[i]}, End: {end_times[i]}")


    return courses_with_multi

# url = f"https://classes.usc.edu/api/Courses/CoursesByTermSchoolProgram?termCode=20253&school={school}&program={program}"
# response = requests.get(url)
# response = response.json()
