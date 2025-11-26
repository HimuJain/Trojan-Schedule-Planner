
-- -----------------------------------------------------
-- schema planner_db
-- -----------------------------------------------------
create schema if not exists planner_db;

-- -----------------------------------------------------
-- table planner_db.semester
-- -----------------------------------------------------
create table if not exists planner_db.semester (
  sem_id integer primary key,
  sem_name varchar(45) not null
);


-- -----------------------------------------------------
-- table planner_db.schoolofferings
-- -----------------------------------------------------
create table if not exists planner_db.schoolofferings(
  schl_code varchar(6) not null,
  sem_id integer not null,
  schl_name varchar(45) not null,
  primary key (schl_code, sem_id),
  foreign key (sem_id)
    references planner_db.semester (sem_id)
    );
create index school_semester_idx 
on planner_db.schoolofferings (sem_id);

-- -----------------------------------------------------
-- table planner_db.programofferings
-- -----------------------------------------------------
create table if not exists planner_db.programofferings (
  prgm_id varchar(4) not null,
  schl_code varchar(6) not null,
  sem_id int not null,
  prgm_name varchar(45) not null,
  primary key (prgm_id, sem_id),
  foreign key (sem_id , schl_code)
    references planner_db.schoolofferings (sem_id , schl_code),
  foreign key (sem_id)
    references planner_db.semester (sem_id)

    );
  
  create index department_school_idx 
  on planner_db.programofferings (sem_id, schl_code);


-- -----------------------------------------------------
-- table planner_db.course
-- -----------------------------------------------------
create table if not exists planner_db.course (
  crs_uid int primary key,
  crs_details varchar(45)
 );


-- -----------------------------------------------------
-- table planner_db.courseoffering
-- -----------------------------------------------------
create table if not exists planner_db.courseoffering (
  sem_id int not null,
  crs_uid int not null,
  prgm_id varchar(4) not null,
  crs_num varchar(7) not null,
  crs_code varchar(10) not null,
  crs_name varchar(45) not null,
  crs_desc text not null,
  crs_geaf varchar(1),
  crs_gegh varchar(1),
  crs_dcorelit smallint,
  crs_unitstr varchar(45),
  crs_unit integer,
  crs_preq text,
  crs_coreq text,
  crs_cross varchar(45),
  crs_note json,
  primary key (sem_id, crs_uid),
  foreign key (sem_id)
    references planner_db.semester (sem_id),
  foreign key (prgm_id , sem_id)
    references planner_db.programofferings (prgm_id , sem_id),
  foreign key (crs_uid)
    references planner_db.course (crs_uid)
    );
create index course_semester_idx 
on planner_db.courseoffering (sem_id);
create index courseoffering_programofferings_idx 
on planner_db.courseoffering (prgm_id, sem_id);
create index courseoffering_course_idx 
on planner_db.courseoffering (crs_uid);

-- -----------------------------------------------------
-- table planner_db.section
-- -----------------------------------------------------
create table if not exists planner_db.section (
  sct_id varchar(45) not null,
  sem_id int not null,
  crs_uid int not null,
  sct_type varchar(10) not null,
  sct_reg int not null,
  sct_seats int not null,
  sct_title varchar(50) null,
  sct_units int null,
  primary key (sct_id, sem_id),
  foreign key (sem_id)
    references planner_db.semester (sem_id),
  foreign key (crs_uid , sem_id)
    references planner_db.courseoffering (crs_uid , sem_id)
    );

create index section_semester_idx 
on planner_db.section (sem_id);
create index section_courseoffering_idx 
on planner_db.section (crs_uid, sem_id);


-- -----------------------------------------------------
-- table planner_db.instructor
-- -----------------------------------------------------

create type instr_status as enum ('good', 'multiple', 'none');
create table if not exists planner_db.instructor (
  instructor_id int primary key,
  instructor_name varchar(45) not null,
  instructor_status instr_status
);


-- -----------------------------------------------------
-- table planner_db.teaches
-- -----------------------------------------------------
create table if not exists planner_db.teaches (
  instructor_id int not null,
  sct_id varchar(45) not null,
  sem_id int not null,
  primary key (instructor_id, sct_id, sem_id),
  foreign key (instructor_id)
    references planner_db.instructor (instructor_id),
  foreign key (sct_id , sem_id)
    references planner_db.section (sct_id , sem_id),
  foreign key (sem_id)
    references planner_db.semester (sem_id)
    );

create index teaches_section_idx 
on planner_db.teaches(sct_id, sem_id);
create index teaches_semester_idx 
on planner_db.teaches(sem_id);
-- -----------------------------------------------------
-- table planner_db.building
-- -----------------------------------------------------
create table if not exists planner_db.building (
  build_id varchar(5) primary key,
  build_add text null,
  build_name text not null,
  build_long int not null,
  build_lat int not null
);


-- -----------------------------------------------------
-- table planner_db.room
-- -----------------------------------------------------
create table if not exists planner_db.room (
  build_id varchar(5) not null,
  room_num int not null,
  primary key (build_id, room_num),
  foreign key (build_id)
    references planner_db.building (build_id)
   );


-- -----------------------------------------------------
-- table planner_db.schedule
-- -----------------------------------------------------
    
create type day_enum as enum('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun');
create table if not exists planner_db.schedule (
  schd_id integer not null,
  schd_day day_enum,
  schd_sttime time,
  schd_entime time,
  sct_id varchar(45) not null,
  sem_id integer not null,
  build_id varchar(5) not null,
  room_num integer not null,
  primary key (schd_id, sct_id, sem_id),
  
  foreign key (sct_id , sem_id)
    references planner_db.section (sct_id , sem_id),
    
  foreign key (build_id , room_num)
    references planner_db.room (build_id , room_num),
  
  foreign key (sem_id)
    references planner_db.semester (sem_id)
    
    );
  
  create index schedule_section_idx 
  on planner_db.schedule(sct_id, sem_id);
  create index schedule_room_idx 
  on planner_db.schedule(build_id, room_num);
  create index schedule_semester_idx 
  on planner_db.schedule(sem_id);

-- -----------------------------------------------------
-- table planner_db.schoolgeneral
-- -----------------------------------------------------
create table if not exists planner_db.schoolgeneral (
  schl_code varchar(6) primary key,
  schl_name varchar(45) not null
);



-- -----------------------------------------------------
-- table planner_db.programgeneral
-- -----------------------------------------------------
create table if not exists planner_db.programgeneral (
  prgm_id varchar(4) primary key,
  prgm_name varchar(45) not null,
  schl_code varchar(6) not null,
  foreign key (schl_code)
    references planner_db.schoolgeneral (schl_code)
    
   );
create index programgeneral_schoolgeneral_idx 
on planner_db.programgeneral(schl_code);


-- -----------------------------------------------------
-- table planner_db.coursegeneral
-- -----------------------------------------------------
create table if not exists planner_db.coursegeneral (
  crs_uid integer primary key ,
  prgm_id varchar(4) not null,
  crsgen_code varchar(45) not null,
  crsgen_name varchar(45) not null,
  crsgen_desc varchar(45) not null,
  crsgen_geaf varchar(45),
  crsgen_gegh varchar(45),
  crsgen_dcorelit smallint,
  crsgen_unitstr varchar(45),
  crsgen_unit varchar(45),
  crsgen_preq varchar(45),
  crsgen_coreq varchar(45),
  crsgen_cross varchar(45),
  crsgen_note json,
  foreign key (prgm_id)
    references planner_db.programgeneral (prgm_id),
  foreign key (crs_uid)
    references planner_db.course (crs_uid)
  );
  create index coursegeneral_programgeneral_idx 
  on planner_db.coursegeneral(prgm_id);
  create index coursegeneral_course_idx 
  on planner_db.coursegeneral(crs_uid);

 


-- -----------------------------------------------------
-- table planner_db.coursecrosslist
-- -----------------------------------------------------
create table if not exists planner_db.coursecrosslist (
  sem_id int not null,
  crs_uid int not null,
  prgm_id varchar(4) not null,
  crs_num varchar(45) not null,
  primary key (sem_id, prgm_id, crs_num),
  foreign key (crs_uid)
    references planner_db.course (crs_uid),
  foreign key (sem_id)
    references planner_db.semester (sem_id),
  foreign key (prgm_id , sem_id)
    references planner_db.programofferings (prgm_id , sem_id)
   );


create index coursecrosslist_semester_idx 
on planner_db.coursecrosslist(sem_id);
create index coursecrosslist_programofferings_idx 
on planner_db.coursecrosslist(prgm_id, sem_id);