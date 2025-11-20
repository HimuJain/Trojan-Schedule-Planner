import requests
import json
from datetime import datetime, timedelta

from models import Semester, School, Program, Course, Section, Instructor, Schedule, Teaches

schoolList = []
programList = []
courseList = []

for i in range(18):
    yearOnes = (i % 3) + 1
    yearTens = (i // 3)
    year = 20200 + yearTens * 10 + yearOnes

sem_id = 20253

url = f"https://classes.usc.edu/api/Schools/TermCode?termCode={sem_id}"
response = requests.get(url)
response = response.json()



for school in response:
    schl_code = school["prefix"]
    schl_name = school["name"]
    # print(schl_code + ": " + schl_name)

    schoolObj = School({
        'SCHL_CODE': schl_code,
        'SEM_ID': sem_id,
        'SCHL_NAME': schl_name
    })
    schoolList.append(schoolObj)

    # print("  Programs:")

    for program in school["programs"]:

        prog_id = program["prefix"]
        prog_name = program["name"]
        # print("    " + prog_id + ": " + prog_name)

        programObj = Program({
            'PROG_ID': prog_id,
            'SCHL_CODE': schl_code,
            'SEM_ID': sem_id,
            'PROG_NAME': prog_name
        })
        programList.append(programObj)

        url = f"https://classes.usc.edu/api/Courses/CoursesByTermSchoolProgram?termCode=20253&school={schl_code}&program={prog_id}"
        response = requests.get(url)
        response = response.json()
        courses = response.get("courses", [])
        for course in courses:
            course_uid = course["courseId"]
            course_code = course["fullCourseName"]
            course_num = course["classNumber"]
            course_name = course["name"]
            course_desc = course["description"]
            course_geaf = ""
            course_gegh = ""
            course_dcorel = ""
            course_units_str = ""
            course_units = course["courseUnits"][0]
            course_prerequisites = ""
            course_corequisites = ""
            course_crosslist = ""
            course_notes = ""

            courseObj = Course({
                'CRS_UID': course_uid,
                'SEM_ID': sem_id,
                'PROG_ID': prog_id,
                'CRS_CODE': course_code,
                'CRS_NUM': course_num,
                'CRS_NAME': course_name,
                'CRS_DESC': course_desc,
                'CRS_GEAF': course_geaf,
                'CRS_GEGH': course_gegh,
                'CRS_DCOREL': course_dcorel,
                'CRS_UNITSTR': course_units_str,
                'CRS_UNITS': course_units,
                'CRS_PREREQ': course_prerequisites,
                'CRS_COREQ': course_corequisites,
                'CRS_CROSS': course_crosslist,
                'CRS_NOTE': course_notes
            })
            courseList.append(courseObj)

            # print("Course " + course_code)

            for section in course["sections"]:
                section_id = section["sisSectionId"]
                section_type = section["rnrMode"]
                section_dclearance = section["hasDClearance"]
                section_registered = section["registeredSeats"]
                section_seats = section["totalSeats"]
                section_title = section["name"]
                section_units = section["units"][0]
                # how to deal with buildings/seats
                scheduleStartTime = []
                scheduleEndTime = []
                scheduleBuilding = []
                scheduleRoom = []
                weekdays = []


                if(len(section["schedule"]) == 1):
                    continue
                for schedule in section["schedule"]:
                    days = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
                    startDay = datetime.strptime("2025-09-01", '%Y-%m-%d')
                    for day in schedule["days"]:
                        weekday = startDay + timedelta(days=days[day])
                        # print(weekday.strftime('%A'))
                        # print(day + str(days[day]))
                        # print(weekday.strftime('%w') + " " + schedule["startTime"])
                        start_time = datetime.strptime(weekday.strftime('%Y-%m-%d') + " " + schedule["startTime"], '%Y-%m-%d %H:%M')
                        # print(start_time.strftime('%w %H:%M'))
                        end_time = datetime.strptime(weekday.strftime('%Y-%m-%d') + " " + schedule["endTime"], '%Y-%m-%d %H:%M')
                        building = schedule["building"] if schedule["building"] else "TBA"
                        room = schedule["room"] if schedule["room"] else "TBA"
                        weekday = days[day]
                        # print("Section " + section_id + ", Course " + course_code)
                        # print("  Building: " + building + ", Room: " + room + ", Start: " + start_time.strftime('%w %H:%M') + ", End: " + end_time.strftime('%w %H:%M'))

                        scheduleStartTime.append(start_time)
                        scheduleEndTime.append(end_time)
                        weekdays.append(weekday)

                        tenMins = timedelta(minutes=10)
                        searchStartTime = end_time + tenMins
                        searchEndTime = start_time - tenMins
                        if(searchStartTime in scheduleStartTime):
                            index = scheduleStartTime.index(searchStartTime)
                            if(scheduleBuilding[index] == building):
                                print("Complete overlap for " + course_code)
                                # print("  Building: " + building + ", Room: " + room + ", Start: " + start_time.strftime('%w %H:%M') + ", End: " + end_time.strftime('%w %H:%M'))
                                # print("  Building: " + scheduleBuilding[index] + ", Room: " + scheduleRoom[index] + ", Start: " + scheduleStartTime[index].strftime('%w %H:%M') + ", End: " + scheduleEndTime[index].strftime('%w %H:%M'))
                            else:
                                print("TIME OVERLAP for " + course_code)
                                # print("  Building: " + building + ", Room: " + room + ", Start: " + start_time.strftime('%w %H:%M') + ", End: " + end_time.strftime('%w %H:%M'))
                                # print("  Building: " + scheduleBuilding[index] + ", Room: " + scheduleRoom[index] + ", Start: " + scheduleStartTime[index].strftime('%w %H:%M') + ", End: " + scheduleEndTime[index].strftime('%w %H:%M'))

                        elif(searchEndTime in scheduleEndTime):
                            index = scheduleEndTime.index(searchEndTime)
                            if(scheduleBuilding[index] == building):
                                print("Complete overlap for " + course_code)
                                # print("  Building: " + building + ", Room: " + room + ", Start: " + start_time.strftime('%w %H:%M') + ", End: " + end_time.strftime('%w %H:%M'))
                                # print("  Building: " + scheduleBuilding[index] + ", Room: " + scheduleRoom[index] + ", Start: " + scheduleStartTime[index].strftime('%w %H:%M') + ", End: " + scheduleEndTime[index].strftime('%w %H:%M'))
                            else:
                                print("TIME OVERLAP for " + course_code)
                                # print("  Building: " + building + ", Room: " + room + ", Start: " + start_time.strftime('%w %H:%M') + ", End: " + end_time.strftime('%w %H:%M'))
                                # print("  Building: " + scheduleBuilding[index] + ", Room: " + scheduleRoom[index] + ", Start: " + scheduleStartTime[index].strftime('%w %H:%M') + ", End: " + scheduleEndTime[index].strftime('%w %H:%M'))
                        elif(building in scheduleBuilding and weekday in weekdays):
                            index = scheduleBuilding.index(building)
                            print("Location overlap for " + course_code)
                            # print("  Building: " + building + ", Room: " + room + ", Start: " + start_time.strftime('%w %H:%M') + ", End: " + end_time.strftime('%w %H:%M'))
                            # print("  Building: " + scheduleBuilding[index] + ", Room: " + scheduleRoom[index] + ", Start: " + scheduleStartTime[index].strftime('%w %H:%M') + ", End: " + scheduleEndTime[index].strftime('%w %H:%M'))
                        else:
                            print("NO OVERLAP for " + course_code)
                            # print("  Building: " + building + ", Room: " + room + ", Start: " + start_time.strftime('%w %H:%M') + ", End: " + end_time.strftime('%w %H:%M'))
                            # print("  Building: " + scheduleBuilding[index] + ", Room: " + scheduleRoom[index] + ", Start: " + scheduleStartTime[index].strftime('%w %H:%M') + ", End: " + scheduleEndTime[index].strftime('%w %H:%M'))
                        scheduleBuilding.append(building)
                        scheduleRoom.append(room)

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


