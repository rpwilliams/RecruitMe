/* Delete the tables if they already exist */
DROP TABLE IF EXISTS People;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Recruiter;
DROP TABLE IF EXISTS University;
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Industry;
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Major;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Salary_Range;
DROP TABLE IF EXISTS Student_Course;
DROP TABLE IF EXISTS Company_Majors;
DROP TABLE IF EXISTS Company_Industry;
DROP TABLE IF EXISTS Student_Company;


/* Create the schema for our tables */
CREATE TABLE People(	ID 				int not null primary key,
						first_name 		varchar(50) not null,
						last_name 		varchar(50) not null,
						email			varchar(50) not null);

CREATE TABLE Major(		major_ID 		int not null primary key,
						name 			varchar(50) not null);

CREATE TABLE University(university_ID	int not null primary key,
						name 			varchar(100) not null,
						state 			varchar(50) not null);

CREATE TABLE Student(	student_ID		int not null primary key,
						major_ID 		int not null,
						university_ID 	int not null,
						GPA 			varchar(8),
						grad_date 		varchar(40),
						FOREIGN KEY (student_ID) REFERENCES People (ID),
						FOREIGN KEY (major_ID) REFERENCES Major (major_ID),
						FOREIGN KEY (university_ID) REFERENCES University (university_ID));

CREATE TABLE Salary_Range(		salary_ID		int not null primary key,
								low_end 		varchar(50) not null,
								high_end 		varchar(50) not null);

CREATE TABLE Company(	company_ID 		int not null primary key,
						salary_ID 		int not null,
						name 			varchar(100) not null,
						num_of_employees varchar(50),
						FOREIGN KEY (salary_ID) REFERENCES Salary_Range (salary_ID));

CREATE TABLE Recruiter(	recruiter_ID 	int not null primary key,
						company_ID		int not null,
						FOREIGN KEY (recruiter_ID) REFERENCES People (ID),
						FOREIGN KEY (company_ID) REFERENCES Company (company_ID));

CREATE TABLE Course(	course_ID 		int not null primary key,
						title 			varchar(50) not null,
						credit_hours 	int);

CREATE TABLE Student_Course(	student_ID 		int not null,
								course_ID 		int not null,
								FOREIGN KEY (student_ID) REFERENCES People (ID),
								FOREIGN KEY (course_ID) REFERENCES Course (course_ID));


CREATE TABLE Industry( 	industry_ID 	int not null primary key,
						name 			varchar(50) not null);


CREATE TABLE Company_Majors(	company_ID 		int not null,
								major_ID 		int not null,
								FOREIGN KEY (company_ID) REFERENCES Company (company_ID),
								FOREIGN KEY (major_ID) REFERENCES Major (major_ID));

CREATE TABLE Company_Industry(	company_ID 		int not null,
								industry_ID 	int not null,
								FOREIGN KEY (company_ID) REFERENCES Company (company_ID),
								FOREIGN KEY (industry_ID) REFERENCES Industry (industry_ID));

CREATE TABLE Student_Company(	student_ID 		int not null,
								company_ID 		int not null,
								FOREIGN KEY (student_ID) REFERENCES People (ID),
								FOREIGN KEY (company_ID) REFERENCES Company (company_ID));



