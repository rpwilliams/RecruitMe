from flask import Flask, render_template, request, jsonify, url_for
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# app.config['MYSQL_DATABASE_USER'] = 'mhixon'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'cis560'
# app.config['MYSQL_DATABASE_DB'] = 'mhixon'
# app.config['MYSQL_DATABASE_HOST'] = 'mysql.cis.ksu.edu'
# mysql.init_app(app)

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

@app.route('/recruiter-view')
def recruiterView():
	return render_template('/recruiter/recruiter-view.html')

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
	result = request.form
	if(request == "POST"):
		return render_template("/student/student-view.html", success = True, result = result)
	elif(request == "GET"):
		result = request.form
        return render_template('/student/student-view.html', result=result)

if __name__ == '__main__':
  app.run()