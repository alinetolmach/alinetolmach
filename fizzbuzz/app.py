from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    content="A Programming school for dummies"
    lst= []
    for i in range (50):
        lst.append(fizzbuzz(i))
     
    return render_template('main.html', content=content, lst=lst)
@app.route("/fizzbuzz/<int:n>")
def two (n):
    content="A Programming school for dummies"
    lst= []
    for i in range (n):
        lst.append(fizzbuzz(i))
     
    return render_template('main.html', content=content, lst=lst)

def fizzbuzz(n):
    if n % 5== 0 and n % 3 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n
print (fizzbuzz (0))