
# ? ----- Class Definitions ------

# Semester class stores the different semesters 
class Semester:
    def __init__(self, semesterData):
        self.semester = semesterData['SEM_ID']
        self.name = semesterData['SEM_NAME']
    
    def to_dict(self):
        return {
            'SEM_ID': self.semester,
            'SEM_NAME': self.name
        }

# School class stores the different schools (school of engineering, school of business, etc.)
class School:
    def __init__(self, schoolData):
        self.code = schoolData['SCHL_CODE']
        self.semester = schoolData['SEM_ID']
        self.name = schoolData['SCHL_NAME']

    def to_dict(self):
        return {
            'SCHL_CODE': self.code,
            'SEM_ID': self.semester,
            'SCHL_NAME': self.name
        }
    
# Program class stores the different course programs (computer science, electrical engineering, etc.)
class Program:
    def __init__(self, programData):
        self.id = programData['PROG_ID']
        self.schoolCode = programData['SCHL_CODE']
        self.semester = programData['SEM_ID']
        self.name = programData['PROG_NAME']

    def to_dict(self):
        return {
            'PROG_ID': self.id,
            'SCHL_CODE': self.schoolCode,
            'SEM_ID': self.semester,
            'PROG_NAME': self.name
        }

# Course class stores the different courses (CSCI 104, EE 109, etc.) and their details (GE requirements, units)
class Course:
    def __init__(self, courseData):
        self.courseID = courseData['CRS_UID']
        self.semester = courseData['SEM_ID']
        self.programID = courseData['PROG_ID']
        self.code = courseData['CRS_CODE']
        self.number = courseData['CRS_NUM']
        self.name = courseData['CRS_NAME']
        self.description = courseData['CRS_DESC']
        self.geaf = courseData['CRS_GEAF']
        self.gegh = courseData['CRS_GEGH']
        self.dcorel = courseData['CRS_DCOREL']
        self.unitsStr = courseData['CRS_UNITSTR']
        self.units = courseData['CRS_UNITS']
        self.prerequisites = courseData['CRS_PREREQ']
        self.corequisites = courseData['CRS_COREQ']
        self.crosslist = courseData['CRS_CROSS']
        self.notes = courseData['CRS_NOTE']

    def to_dict(self):
        return {
            'CRS_UID': self.courseID,
            'SEM_ID': self.semester,
            'PROG_ID': self.programID,
            'CRS_CODE': self.code,
            'CRS_NUM': self.number,
            'CRS_NAME': self.name,
            'CRS_DESC': self.description,
            'CRS_GEAF': self.geaf,
            'CRS_GEGH': self.gegh,
            'CRS_DCOREL': self.dcorel,
            'CRS_UNITSTR': self.unitsStr,
            'CRS_UNITS': self.units,
            'CRS_PREREQ': self.prerequisites,
            'CRS_COREQ': self.corequisites,
            'CRS_CROSS': self.crosslist,
            'CRS_NOTE': self.notes
        }


# Section class stores the different sections of a course (the lecture sections, the lab, etc. with their IDs)
class Section:
    def __init__(self, sectionData):
        self.id = sectionData['SCT_ID']
        self.courseID = sectionData['CRS_ID']
        self.semester = sectionData['SEM_ID']
        self.type = sectionData['SCT_TYPE']
        self.dclear = sectionData['SCT_DCLEAR']
        self.registered = sectionData['SCT_REG']
        self.seats = sectionData['SCT_SEATS']
        self.building = sectionData['SCT_BUILD']
        self.room = sectionData['SCT_ROOM']
        self.title = sectionData['SCT_TITLE']
        self.units = sectionData['SCT_UNITS']

    def to_dict(self):
        return {
            'SCT_ID': self.id,
            'CRS_ID': self.courseID,
            'SEM_ID': self.semester,
            'SCT_TYPE': self.type,
            'SCT_DCLEAR': self.dclear,
            'SCT_REG': self.registered,
            'SCT_SEATS': self.seats,
            'SCT_BUILD': self.building,
            'SCT_ROOM': self.room,
            'SCT_TITLE': self.title,
            'SCT_UNITS': self.units
        }

# Schedule class stores all the different schedules of a section (one row for each different day and time)
class Schedule:
    def __init__(self, scheduleData):
        self.sectionID = scheduleData['SCT_ID']
        self.scheduleID = scheduleData['SCH_ID']
        self.day = scheduleData['SCH_DAY']
        self.start = scheduleData['SCH_STARTTIME']
        self.end = scheduleData['SCH_ENDTIME']

    def to_dict(self):
        return {
            'SCT_ID': self.sectionID,
            'SCH_ID': self.scheduleID,
            'SCH_DAY': self.day,
            'SCH_STARTTIME': self.start,
            'SCH_ENDTIME': self.end
        }
# Instructor class stores the different instructors and their IDs
class Instructor:
    def __init__(self, instructorData):
        self.id = instructorData['INSTR_ID']
        self.name = instructorData['INSTR_NAME']

    def to_dict(self):
        return {
            'INSTR_ID': self.id,
            'INSTR_NAME': self.name
        }

# Teaches class stores the different instructors and the sections they teach by ID (multiple different instructors can teach the same section)
class Teaches:
    def __init__(self, teachingData):
        self.instructorID = teachingData['INSTR_ID']
        self.sectionID = teachingData['SCT_ID']
        self.semester = teachingData['SEM_ID']

    def to_dict(self):
        return {
            'INSTR_ID': self.instructorID,
            'SCT_ID': self.sectionID,
            'SEM_ID': self.semester
        }

