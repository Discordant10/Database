from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'DA', 
    'location' : 'Delhi',
    'salary' : 'Rs 1,00,000'
  },
  {
    'id' : 2,
    'title' : 'WS', 
    'location' : 'Blr',
    'salary' : 'Rs 14,00,000'
  },
  {
    'id' : 3,
    'title' : 'SS', 
    'location' : 'Chenn',
    'salary' : 'Rs 11,00,000'
  },
  {
    'id' : 4,
    'title' : 'TT',
    'location' : 'GGT',
    'salary' : 'Rs 155,00,000'  
  },
  
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name = 'Jov')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)