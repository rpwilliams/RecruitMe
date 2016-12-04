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
#     student = {
#         'firstName': request.form['first'],
# 		'lastName' : request.form['last'],
# 		'email' : request.form['email'],
# 		'password' : request.form['pwd'],
# 		'studentID' : request.form['id'],
# 		'GPA' : request.form['GPA'],
# 		'major' : request.form['major']
#     }
#     students.append(student)
#     return jsonify({'student': student}), 201

@app.route('/student-view', methods = ['POST', 'GET'])
def studentView():
	### PUT SQL QUERIES HERE ###
	result = request.form
	if(request == "POST"):
		return render_template("/student/student-view.html", success = True, result = result)
	elif(request == "GET"):
		result = request.form
        return render_template('/student/student-view.html', result=result)

@app.route('/recruiter-view', methods = ['POST', 'GET'])
def recruiterView():
	### PUT SQL QUERIES HERE ###
	query = execute_query("""SELECT p.first_name, p.last_name, p.email, m.name,
	 u.name, s.GPA 
	FROM People p JOIN Student s ON s.student_ID = p.ID 
	JOIN Major m ON s.major_ID = m.major_ID
	JOIN University u ON u.university_ID = s.university_ID; """)
	line = str(query) # Convert the tuple to a string
	stringList = []
	parsedLine = parseString(line)
	stringList = createStringList(parsedLine)
	return render_template('/recruiter/recruiter-view.html', rows=stringList)

# @Function parseString
# Removes unwanted symbols from the string
# @Param {line} The string to be parsed (NOT a tuple)
# @Return String without characters and | characters
def parseString(line):
	count = 0
	newWord = "";
	for c in line:
		if c != "'" and c != "u" and c != "(":
			# Concatonate the string 
			if c != ",":
				newWord += c
				# Don't add a | character if we have reached the end
				if c == ")":
					count = 0
			# If there is a comma, replace it with a space
			else:
				count += 1
				if count > 1:
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