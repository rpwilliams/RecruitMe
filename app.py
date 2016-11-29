from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recruiter')
def recruiter():
    return render_template('/recruiter/recruiter.html')

if __name__ == '__main__':
  app.run()