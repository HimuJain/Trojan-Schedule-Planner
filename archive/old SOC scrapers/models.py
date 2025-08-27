from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass

class Semester(Base):
    __tablename__ = 'semesters'
    SEM_ID: Mapped[int] = mapped_column(primary_key=True, index=True)
    SEM_NAME: Mapped[str] = mapped_column(nullable=False)

    schools: Mapped[list["School"]] = relationship(back_populates="semester")
    departments: Mapped[list["Department"]] = relationship(back_populates="semester")
    courses: Mapped[list["Course"]] = relationship(back_populates="semester")
    sections: Mapped[list["Section"]] = relationship(back_populates="semester")
    instructors: Mapped[list["Instructor"]] = relationship(back_populates="semester")
    schedules: Mapped[list["Schedule"]] = relationship(back_populates="semester")
    

    def __repr__(self):
        return f"<Semester SEMESTER_ID={self.SEMESTER_ID}, SEMESTER_NAME={self.SEMESTER_NAME})>"


class School(Base):
    __tablename__ = 'schools'
    SCHL_CODE: Mapped[str] = mapped_column(primary_key=True, index=True)
    SEM_ID: Mapped[int] = mapped_column(ForeignKey('semesters.SEM_ID'), primary_key=True, index=True)
    SCHL_NAME: Mapped[str] = mapped_column(nullable=False)

    departments: Mapped[list["Department"]] = relationship(back_populates="school")
    semester: Mapped["Semester"] = relationship(back_populates="schools")

    def __repr__(self):
        return f"<School SCHL_CODE={self.SCHL_CODE}, SCHL_NAME={self.SCHL_NAME})>"
    
class Department(Base):
    __tablename__ = 'departments'
    SCHL_CODE: Mapped[str] = mapped_column(ForeignKey('school.SCHL_CODE'), primary_key=True, index=True)
    DEP_ID: Mapped[str] = mapped_column(primary_key=True, index=True)
    SEM_ID: Mapped[int] = mapped_column(ForeignKey('semesters.SEM_ID'), primary_key=True, index=True)
    DEP_NAME: Mapped[str] = mapped_column()

    schools: Mapped["School"] = relationship(back_populates="departments")
    courses: Mapped[list["Course"]] = relationship(back_populates="department")
    semester: Mapped["Semester"] = relationship(back_populates="departments")

    def __repr__(self):
        return f"<Department SCHL_CODE={self.SCHL_CODE}, DEP_ID={self.DEP_ID}, DEP_NAME={self.DEP_NAME})>"
    
class Course(Base):
    __tablename__ = 'courses'
    CRS_UID: Mapped[str] = mapped_column(primary_key=True, index=True)
    SEM_ID: Mapped[int] = mapped_column(ForeignKey('semesters.SEM_ID'), primary_key=True, index=True)

    DEP_ID: Mapped[str] = mapped_column(ForeignKey('departments.DEP_ID'), index=True)
    CRS_NUM: Mapped[str] = mapped_column(index=True, nullable=False)

    CRS_CODE: Mapped[str] = mapped_column(index=True, nullable=False)
    CRS_NAME: Mapped[str] = mapped_column(nullable=False)
    CRS_DESC: Mapped[str] = mapped_column(nullable=False)
    CRS_GEAF: Mapped[str] = mapped_column(index=True)
    CRS_GEGH: Mapped[str] = mapped_column(index=True)
    CRS_DCOREL: Mapped[str] = mapped_column(index=True)
    CRS_UNITSTR: Mapped[str] = mapped_column()
    CRS_UNITS: Mapped[int] = mapped_column(index=True)
    CRS_PREREQ: Mapped[str] = mapped_column(index=True)
    CRS_COREQ: Mapped[str] = mapped_column(index=True)
    CRS_CROSS: Mapped[str] = mapped_column(index=True)
    CRS_NOTE: Mapped[str] = mapped_column()

    department: Mapped["Department"] = relationship(back_populates="courses")
    sections: Mapped[list["Section"]] = relationship(back_populates="course")
    semester: Mapped["Semester"] = relationship(back_populates="courses")

    def __repr__(self):
        return f"<Course CRS_UID={self.CRS_UID}, SEM_ID={self.SEM_ID}, CRS_NUM={self.CRS_NUM}, CRS_NAME={self.CRS_NAME})>"

class Section(Base):
    __tablename__ = 'sections'
    SCT_ID: Mapped[str] = mapped_column(primary_key=True, index=True)
    CRS_UID: Mapped[str] = mapped_column(ForeignKey('courses.CRS_UID'), index=True)
    SEM_ID: Mapped[int] = mapped_column(ForeignKey('semesters.SEM_ID'), primary_key=True, index=True)
    SCT_TYPE: Mapped[str] = mapped_column(nullable=False)
    SCT_REG: Mapped[int] = mapped_column(nullable=False)
    SCT_SEATS: Mapped[int] = mapped_column(nullable=False)
    SCT_ROOM: Mapped[str] = mapped_column()
    SCT_TITLE: Mapped[str] = mapped_column()
    SCT_UNITS: Mapped[int] = mapped_column()

    course: Mapped["Course"] = relationship(back_populates="sections")
    teaches: Mapped[list["Teaches"]] = relationship(back_populates="section")
    schedules: Mapped[list["Schedule"]] = relationship(back_populates="section")
    semester: Mapped["Semester"] = relationship(back_populates="sections")



    def __repr__(self):
        return f"<Section SCT_ID={self.SCT_ID}, SEM_ID={self.SEM_ID}, CRS_UID={self.CRS_UID}, SCT_TYPE={self.SCT_TYPE}, SCT_REG={self.SCT_REG}, SCT_SEATS={self.SCT_SEATS})>"


class Schedule(Base):
    __tablename__ = 'schedules'
    SCH_ID: Mapped[str] = mapped_column(primary_key=True, index=True)
    SCT_ID: Mapped[str] = mapped_column(ForeignKey('sections.SCT_ID'), index=True)
    SEM_ID: Mapped[int] = mapped_column(ForeignKey('semesters.SEM_ID'), primary_key=True, index=True)
    SCH_DAY: Mapped[str] = mapped_column(nullable=False) # double check nullable
    SCH_STARTTIME: Mapped[str] = mapped_column(nullable=False)
    SCH_ENDTIME: Mapped[str] = mapped_column(nullable=False)

    section: Mapped["Section"] = relationship(back_populates="schedules")
    semester: Mapped["Semester"] = relationship(back_populates="schedules")

    def __repr__(self):
        return f"<Schedule SCH_ID={self.SCH_ID}, SCT_ID={self.SCT_ID}, SEM_ID={self.SEM_ID}, SCH_DAY={self.SCH_DAY}, SCH_STARTTIME={self.SCH_STARTTIME}, SCH_ENDTIME={self.SCH_ENDTIME})>"


class Instructor(Base):
    __tablename__ = 'instructors'
    INSTR_ID: Mapped[str] = mapped_column(primary_key=True, index=True)
    INSTR_NAME: Mapped[str] = mapped_column(nullable=False)

    teaches: Mapped[list["Teaches"]] = relationship(back_populates="instructor")
    semester: Mapped["Semester"] = relationship(back_populates="instructors")

    def __repr__(self):
        return f"<Instructor INSTR_ID={self.INSTR_ID}, INSTR_NAME={self.INSTR_NAME})>"

class Teaches(Base):
    __tablename__ = 'teaches'
    INSTR_ID: Mapped[str] = mapped_column(ForeignKey('instructors.INSTR_ID'), primary_key=True, index=True)
    SCT_ID: Mapped[str] = mapped_column(ForeignKey('sections.SCT_ID'), primary_key=True, index=True)
    SEM_ID: Mapped[int] = mapped_column(ForeignKey('semesters.SEM_ID'), primary_key=True, index=True)

    section: Mapped["Section"] = relationship(back_populates="teaches")
    instructor: Mapped["Instructor"] = relationship(back_populates="teaches")

    def __repr__(self):
        return f"<Teaches INSTR_ID={self.INSTR_ID}, SCT_ID={self.SCT_ID}, SEM_ID={self.SEM_ID})>"