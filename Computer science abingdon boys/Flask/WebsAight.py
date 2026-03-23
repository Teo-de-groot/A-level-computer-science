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

@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if req.method == 'POST':
        comment = req.form.get('comment')
        with open('comments.txt', 'a') as f:
            f.write(comment + '\n')
    comments = []
    if os.path.exists('comments.txt'):
        with open('comments.txt', 'r') as f:
            comments = f.readlines()
    return rt('text.php', comments=comments)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)