from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'mhixon'
app.config['MYSQL_DATABASE_PASSWORD'] = 'cis560'
app.config['MYSQL_DATABASE_DB'] = 'mhixon'
app.config['MYSQL_DATABASE_HOST'] = 'mysql.cis.ksu.edu'
mysql.init_app(app)

@app.route('/')
def index():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM month_discount")
	#data = cursor.fetchone()
	return render_template('index.html')
	
@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/sign-up')
def signUp():
    return render_template('/sign-up.html')

@app.route('/sign-up/recruiter')
def recruiter():
    return render_template('/recruiter/recruiter-sign-up.html')

@app.route('/sign-up/student')
def student():
    return render_template('/student/student-sign-up.html')

if __name__ == '__main__':
  app.run()