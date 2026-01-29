from flask import Flask as FL
from flask import request as req
from flask import render_template as rt
import datetime
import os
from flask import jsonify
app = FL(__name__,template_folder='template')
@app.route('/')
def index():
    return "This is Mr Lomax's Website."

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/goodbye')
def goodbye():
    return "Goodbye, World!"

@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}!"

@app.route('/goodbye/<name>')
def goodbye_name(name):
    return f"Goodbye, {name}!"

@app.route('/add')
def add():
    first_num= req.args.get('first', default=0, type=int)
    second_num= req.args.get('second', default=0, type=int)
    result = first_num + second_num
    return f"The sum of {first_num} and {second_num} is {result}."

@app.route("/factorial")
def factorial():
    num = req.args.get('n', default=0, type=int)
    if num < 0:
        return "silly silly no negatives i tested for that."
    result = 1
    for i in range(1, num + 1):
        result *= i
    return f"The factorial of {num} is {result}."

@app.route("/fibonacci")
def fibonacci():
    n = req.args.get('n', default=0, type=int)
    if n < 0:
        return "silly silly no negatives i tested for that."
    a =0
    b=1
    for _ in range(n):
        a, b = b, a + b
    return f"The {n}th Fibonacci number is {a}."
@app.route("/birthday", methods=["GET", "POST"])
def CnD():
    if req.method == "GET":
        return rt("index.php")

  
    birthdate = req.form.get("birthdate")  

    year, month, day = map(int, birthdate.split("-"))
    dob = datetime.date(year, month, day)
    today = datetime.date.today()

    birthday_this_year = datetime.date(today.year, dob.month, dob.day)

    if birthday_this_year > today:
        next_birthday = birthday_this_year
    else:
        next_birthday = datetime.date(today.year + 1, dob.month, dob.day)

    days_to_birthday = (next_birthday - today).days
    age = today.year - dob.year - (
        (today.month, today.day) < (dob.month, dob.day)
    )

    return (
        f"Your date of birth is {dob}<br>"
        f"You are {age} years old.<br>"
        f"Your next birthday is in {days_to_birthday} days on {next_birthday}."
        )
PHP_ENDPOINT = 'http://localhost/text.php'  

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Receives a file from the frontend and forwards it to the PHP backend.
    """
    if 'file' not in req.files:
        return jsonify({"status": "error", "message": "No file part"}), 400
    
    file = req.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400
    
    # Forward file to PHP using requests
    files = {'file': (file.filename, file.stream, file.content_type)}
    response = req.post(PHP_ENDPOINT, files=files)
    
    try:
        return jsonify(response.json()), response.status_code
    except:
        return response.text, response.status_code

@app.route('/read', methods=['GET'])
def read_file():
    """
    Receives a filename from the frontend, forwards it to the PHP backend, 
    and returns the content.
    """
    filename = req.args.get('filename')
    if not filename:
        return jsonify({"status": "error", "message": "No filename provided"}), 400
    
    response = requests.get(PHP_ENDPOINT, params={"filename": filename})
    
    if response.status_code == 200:
        return response.text, 200, {'Content-Type': 'text/plain'}
    else:
        try:
            return jsonify(response.json()), response.status_code
        except:
            return response.text, response.status_code


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)