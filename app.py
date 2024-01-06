from flask import Flask, render_template, jsonify

app = Flask(__name__)
print(__name__)
JOBS=[
  {
    'id':1,
    'name':'Software Developer Intern',
    'location':'Bangalore',
    'salary':'Rs. 37,00,000'
  },
  {
    'id':2,
    'name':'Data Analyst Intern',
    'location':'Bangalore',
    'salary':'Rs. 17,00,000'
  },
  {
   'id':3,
   'name':'Software Developer',
   'location':'Hyderabad',
   'salary':'Rs. 48,00,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
