########################################
# app.py           					   #
# Description: The main python file    #
# to be run for "RecruitMe"            #
# Author: Ryan Williams				   #
# Last modified 12.4.2016              #
########################################
from flask import Flask, render_template, request, jsonify, url_for, json, g
from werkzeug import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL
import csv

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'mhixon'
app.config['MYSQL_DATABASE_PASSWORD'] = 'cis560'
app.config['MYSQL_DATABASE_DB'] = 'mhixon'
app.config['MYSQL_DATABASE_HOST'] = 'mysql.cis.ksu.edu'
app.config['MYSQL_USE_UNICODE'] = False
mysql.init_app(app)

# @function connect_to_mySQL
# Connects to mySQL
def connect_to_mySQL():
	return mysql.connect()

# @function execute_query
# Executes a query
# @param {query} the query to be executed
# @param {args} the arguments
# Enter a paramater like this:
# execute_query("""SELECT * FROM table)
# @return the rows in the query
def execute_query(query, args=()):
	conn = connect_to_mySQL()
	cursor = conn.cursor()
	cursor.execute(query, args)
	rows = cursor.fetchall()
	conn.commit()
	cursor.close()
	return rows

# @function viewdb
# Test function to view a database at localhost:5000/viewdb
@app.route("/viewdb")
def viewdb():
	rows = execute_query("""SELECT first_name, last_name FROM People""")
	return '<br>'.join(str(row) for row in rows) # Displays everything in db in the browser

@app.route('/')
def index():
	# conn = mysql.connect()
	# cursor = conn.cursor()
	# cursor.execute("SELECT * FROM month_discount")
	#data = cursor.fetchone()
	return render_template('index.html')

@app.route('/sign-up')
def signUp():
    return render_template('/sign-up.html')
	
@app.route('/login')
def login():
    return render_template('/login.html')

# @app.route('/student-view')
# def studentView():
# 	createStudents()
# 	return render_template('/student/student-view.html')

@app.route('/sign-up/recruiter')
def recruiter():
    return render_template('/recruiter/recruiter-sign-up.html')

@app.route('/sign-up/student')
def student():
	return render_template('/student/student-sign-up.html')

# @app.route('/students', methods=['GET'])
# def getStudents():
#     return jsonify({'students': tasks})

# @app.route('/students', methods=['POST'])
# def createStudents():
# 	student = {
#         'firstName': request.form['first'],
# 		'lastName' : request.form['last'],
# 		'email' : request.form['email'],
# 		'password' : request.form['pwd'],
# 		'studentID' : request.form['id'],
# 		'GPA' : request.form['GPA'],
# 		'major' : request.form['major']
#     }
#     query = execute_query("""insert into People(first_name, last_name, email, student_ID) values (%s,%s,%s,%s)""", [request.form['first'], request.form['last'], request.form['email'], request.form['id']]);
#     return jsonify({'student': student}), 201

##############################################
#          STUDENT VIEW FUNCTIONS			 #
##############################################
@app.route('/student-view', methods = ['POST', 'GET'])
def studentView():
	# student = {
	# 	'firstName': request.form['first'],
	# 	'lastName' : request.form['last'],
	# 	'email' : request.form['email'],
	# 	'password' : request.form['pwd'],
	# 	'studentID' : request.form['id'],
	# 	'GPA' : request.form['GPA'],
	# 	'major' : request.form['major'],
	# 	'university': request.form['university']
	# }
	# query = execute_query("""insert into People(first_name, last_name, email, ID) values (%s,%s,%s,%s)""", [student['firstName'], student['lastName'], student['email'], student['studentID']]);	
	# query = execute_query("""insert into Student(student_ID, major_ID, university_ID, GPA) values (%s,%s,%s,%s)""", [student['studentID'], student['major'], student['university'], student['GPA']]);	
	### PUT SQL QUERIES HERE ###
	query = execute_query("""SELECT distinct p.first_name, p.last_name, p.email,
	c.name, i.name, sr.low_end, sr.high_end, c.num_of_employees, m.name
	FROM People p
	JOIN Recruiter r ON r.recruiter_id = p.ID
	JOIN Company c ON c.company_ID = r.company_ID
	JOIN Company_Industry ci ON ci.company_ID = c.company_ID
	JOIN Industry i ON i.industry_ID = ci.industry_ID
	JOIN Salary_Range sr ON sr.salary_ID = c.salary_ID
	JOIN Company_Majors cm ON cm.company_ID = c.company_ID
	JOIN Major m ON m.major_ID = cm.major_ID""")
	line = str(query) # Convert the tuple to a string
	stringList = []
	parsedLine = parseString(line, True)
	stringList = createStringList(line)
	return render_template('/student/student-view.html', rows=stringList)

@app.route('/student-view/filter', methods=["GET", "POST"])
def filterRecruiters():
	company = request.form["companyradio"]
	industry = request.form.get("industryradio")
	pay = request.form["payradio"]
	query = ""
	print company
	if(company == "augue"):
		query = filterRecruiterCompany("Augue Porttitor Interdum Corp.")
	elif(company == "posuere"):
	  	query = filterRecruiterCompany("Posuere Vulputate Lacus PC")
	elif(company == "suspendisse"):
		query = filterRecruiterCompany("Suspendisse Non LLC")
	elif(industry == "education"):
		query = filterRecruiterIndustry("Education")
	elif(industry == "financial"):
		query = filterRecruiterIndustry("Financial Services")
	elif(industry == "utilties"):
		query = filterRecruiterIndustry("Services")
	elif(pay == "5000"):
		query = filterRecruiterSalary("5000")
	elif(pay == "6000"):
		query = filterRecruiterSalary("6000")
	elif(pay == "7000"):
		query = filterRecruiterSalary("7000")
	return render_template('/student/student-view.html', rows=query)

@app.route('/company/<company>', methods = ['POST', 'GET'])
def filterRecruiterCompany(company):
	query = execute_query("""SELECT distinct p.first_name, p.last_name, p.email,
	c.name, i.name, sr.low_end, sr.high_end, c.num_of_employees, m.name
	FROM People p
	JOIN Recruiter r ON r.recruiter_id = p.ID
	JOIN Company c ON c.company_ID = r.company_ID
	JOIN Company_Industry ci ON ci.company_ID = c.company_ID
	JOIN Industry i ON i.industry_ID = ci.industry_ID
	JOIN Salary_Range sr ON sr.salary_ID = c.salary_ID
	JOIN Company_Majors cm ON cm.company_ID = c.company_ID
	JOIN Major m ON m.major_ID = cm.major_ID
	WHERE c.name = %s""", [company])
	line = str(query) # Convert the tuple to a string
	stringList = []
	parsedLine = parseString(line, True)
	stringList = createStringList(parsedLine)
	return stringList

@app.route('/student-view/filter/industry/<industry>', methods = ['POST', 'GET'])
def filterRecruiterIndustry(industry):
	query = execute_query("""SELECT distinct p.first_name, p.last_name, p.email,
	c.name, i.name, sr.low_end, sr.high_end, c.num_of_employees, m.name
	FROM People p
	JOIN Recruiter r ON r.recruiter_id = p.ID
	JOIN Company c ON c.company_ID = r.company_ID
	JOIN Company_Industry ci ON ci.company_ID = c.company_ID
	JOIN Industry i ON i.industry_ID = ci.industry_ID
	JOIN Salary_Range sr ON sr.salary_ID = c.salary_ID
	JOIN Company_Majors cm ON cm.company_ID = c.company_ID
	JOIN Major m ON m.major_ID = cm.major_ID
	WHERE i.name = %s""", [industry])
	line = str(query) # Convert the tuple to a string
	stringList = []
	parsedLine = parseString(line, True)
	stringList = createStringList(parsedLine)
	return stringList

@app.route('/student-view/filter/salaryRange/<salaryRange>', methods = ['POST', 'GET'])
def filterRecruiterSalary(salaryRange):
	query = execute_query("""SELECT distinct p.first_name, p.last_name, p.email,
	c.name, i.name, sr.low_end, sr.high_end, c.num_of_employees, m.name
	FROM People p
	JOIN Recruiter r ON r.recruiter_id = p.ID
	JOIN Company c ON c.company_ID = r.company_ID
	JOIN Company_Industry ci ON ci.company_ID = c.company_ID
	JOIN Industry i ON i.industry_ID = ci.industry_ID
	JOIN Salary_Range sr ON sr.salary_ID = c.salary_ID
	JOIN Company_Majors cm ON cm.company_ID = c.company_ID
	JOIN Major m ON m.major_ID = cm.major_ID
	WHERE sr.low_end = %s""", [salaryRange])
	line = str(query) # Convert the tuple to a string
	stringList = []
	parsedLine = parseString(line, True)
	stringList = createStringList(parsedLine)
	return stringList

@app.route('/student-view/filter/numEmployees/<numEmployees>', methods = ['POST', 'GET'])
def filterRecruiterEmployees(numEmployees):
	query = execute_query("""SELECT distinct p.first_name, p.last_name, p.email,
	c.name, i.name, sr.low_end, sr.high_end, c.num_of_employees, m.name
	FROM People p
	JOIN Recruiter r ON r.recruiter_id = p.ID
	JOIN Company c ON c.company_ID = r.company_ID
	JOIN Company_Industry ci ON ci.company_ID = c.company_ID
	JOIN Industry i ON i.industry_ID = ci.industry_ID
	JOIN Salary_Range sr ON sr.salary_ID = c.salary_ID
	JOIN Company_Majors cm ON cm.company_ID = c.company_ID
	JOIN Major m ON m.major_ID = cm.major_ID
	WHERE c.num_of_employees = %s""", [numEmployees])
	line = str(query) # Convert the tuple to a string
	stringList = []
	parsedLine = parseString(line, True)
	stringList = createStringList(parsedLine)
	return stringList

@app.route('/student-view/filter/major/<major>', methods = ['POST', 'GET'])
def filterRecruiterMajor(major):
	query = execute_query("""SELECT distinct p.first_name, p.last_name, p.email,
	c.name, i.name, sr.low_end, sr.high_end, c.num_of_employees, m.name
	FROM People p
	JOIN Recruiter r ON r.recruiter_id = p.ID
	JOIN Company c ON c.company_ID = r.company_ID
	JOIN Company_Industry ci ON ci.company_ID = c.company_ID
	JOIN Industry i ON i.industry_ID = ci.industry_ID
	JOIN Salary_Range sr ON sr.salary_ID = c.salary_ID
	JOIN Company_Majors cm ON cm.company_ID = c.company_ID
	JOIN Major m ON m.major_ID = cm.major_ID
	WHERE m.name = %s""", [major])
	line = str(query) # Convert the tuple to a string
	stringList = []
	parsedLine = parseString(line, True)
	stringList = createStringList(parsedLine)
	return stringList

##############################################
#          RECRUITER VIEW FUNCTIONS			 #
##############################################
@app.route('/recruiter-view', methods = ['POST', 'GET'])
def recruiterView():
	# recruiter = {
	# 	'firstName': request.form['first'],
	# 	'lastName' : request.form['last'],
	# 	'email' : request.form['email'],
	# 	'id' : request.form['id'],
	# 	'password' : request.form['pwd'],
	# 	'company': request.form['company']
	# }
	# query = execute_query("""insert into People(first_name, last_name, email, ID) values (%s,%s,%s,%s)""", [recruiter['firstName'], recruiter['lastName'], recruiter['email'], recruiter['id']]);	
	# query = execute_query("""insert into Recruiter(recruiter_ID, company_ID) values (%s,%s)""", [recruiter['id'], recruiter['company']]);	

	### PUT SQL QUERIES HERE ###
	query = execute_query("""SELECT p.first_name, p.last_name, p.email, m.name,
	 u.name, s.GPA 
	FROM People p JOIN Student s ON s.student_ID = p.ID 
	JOIN Major m ON s.major_ID = m.major_ID
	JOIN University u ON u.university_ID = s.university_ID; """)
	line = str(query) # Convert the tuple to a string
	stringList = []
	parsedLine = parseString(line, False)
	stringList = createStringList(parsedLine)
	return render_template('/recruiter/recruiter-view.html', rows=stringList)

@app.route('/recruiter-view/filter', methods = ['POST', 'GET'])
def filterStudents():
	major = request.form["majorradio"]
	gpa = request.form["gparadio"]
	college = request.form["collegeradio"]
	query = ""
	print company
	if(major == "Accounting"): 
		query = filterStudentMajor('Accounting')
	elif(major == "Computer Science"):
	  	query = filterStudentMajor("Computer Science")
	elif(gpa == "2-3"):
		query = filterStudentGPA("2.00")
	elif(gpa == "3-4"):
		query = filterStudentGPA("3.00")
	elif(gpa == "4+"):
		query = filterStudentGPA("4.00")
	elif(college == "Kansas State University"):
		query = filterStudentCollege("Kansas State University")
	elif(college == "Oklahoma State University"):
		query = filterStudentCollege("Oklahoma State University")
	return render_template('/recruiter/recruiter-view.html', rows=query)

@app.route('/recruiter-view/major/<major>', methods = ['POST', 'GET'])
def filterStudentMajor(major):
	### PUT SQL QUERIES HERE ###
	query = execute_query("""SELECT p.first_name, p.last_name, p.email, m.name,
	 u.name, s.GPA 
	FROM People p JOIN Student s ON s.student_ID = p.ID 
	JOIN Major m ON s.major_ID = m.major_ID
	JOIN University u ON u.university_ID = s.university_ID
	WHERE m.name = %s; """, [major])
	line = str(query) # Convert the tuple to a string
	stringList = []
	parsedLine = parseString(line, False)
	stringList = createStringList(parsedLine)
	return render_template('/student/student-view.html', rows=stringList)
	#return stringList

def filterStudentGPA(gpa):
	### PUT SQL QUERIES HERE ###
	query = execute_query("""SELECT p.first_name, p.last_name, p.email, m.name,
	 u.name, s.GPA 
	FROM People p JOIN Student s ON s.student_ID = p.ID 
	JOIN Major m ON s.major_ID = m.major_ID
	JOIN University u ON u.university_ID = s.university_ID
	WHERE s.GPA = %s; """, [gpa])
	line = str(query) # Convert the tuple to a string
	stringList = []
	parsedLine = parseString(line, False)
	stringList = createStringList(parsedLine)
	return stringList

def filterStudentCollege(college):
	### PUT SQL QUERIES HERE ###
	query = execute_query("""SELECT p.first_name, p.last_name, p.email, m.name,
	 u.name, s.GPA 
	FROM People p JOIN Student s ON s.student_ID = p.ID 
	JOIN Major m ON s.major_ID = m.major_ID
	JOIN University u ON u.university_ID = s.university_ID
	WHERE u.name = %s; """, [college])
	line = str(query) # Convert the tuple to a string
	stringList = []
	parsedLine = parseString(line, False)
	stringList = createStringList(parsedLine)
	return stringList


# @Function parseString
# Removes unwanted symbols from the string
# @Param {line} The string to be parsed (NOT a tuple)
# @Param {student} true if student view, false if recruiter view
# @Return String without characters and | characters
def parseString(line, student):
	count = 0
	newWord = ""
	nextU = False
	for c in line:
		if c != "'" and c != "(":

			# Preserve all u's except for the one's we don't want
			# if(nextU):
			# 	nextU = False
			# 	continue
			# if(c == " " or c == "("):
			# 	nextU = True

			# Ensure we get rid of the u's before the words
			# Concatonate the string 
			if c != ",":
				newWord += c
				# Don't add a | character if we have reached the end
				if c == ")":
					count = -1
			# If there is a comma, replace it with a space
			else:
				count += 1
				if count > 2:
					# Add a dash for salary range
					if (count == 5) and student:
						newWord += "| $"
					elif (count == 6) and student:
						newWord += " -"
					else:
						newWord += " | "
	return newWord

# @Function createStringList
# Converts a string to a string list at each ")"
# @Param {line} The string to be converted
# @Return A string list
def createStringList(line):
	stringList = []
	string = ""
	for c in line:
		if c == ")":
			stringList.append(string)
			string = ""
		else:
			string += c
	return stringList

# @app.route('/recruiter-view', methods = ['POST', 'GET'])
# def recruiterView():
# 	_first = request.form['first']
# 	_last = request.form['last']
# 	_email = request.form['email']
# 	_password = request.form['pwd']

# 	result = request.form
# 	if(request == "POST"):
# 		return render_template("/recruiter/recruiter-view.php", success = True, result = result)
# 	elif(request == "GET"):
# 		result = request.form
#         return render_template('/recruiter/recruiter-view.php', result=result)

# Alternative to recruiterView(). If we can get this to work,
# we can add people to the database when they sign up
# @app.route('/recruiter_sign_up', methods=['POST', 'GET'])
# def recruiter_sign_up():
# 	_first = request.form['first']
# 	_last = request.form['last']
# 	_email = request.form['email']
# 	_password = request.form['pwd']
# 	_hashed_password = generate_password_hash(_password)
# 	#cursor.callproc('sp_createUser',(_first, _last, _email, _hashed_password))
# 	# else:
# 	return json.dumps({'html':'All fields good!'})

if __name__ == '__main__':
  app.run()