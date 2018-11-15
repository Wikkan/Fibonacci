from flask import Flask

app = Flask(__name__)

@app.route('/')
def fib():
    n = 10
    
    a = 0
    b = 1
     
    for x in range(n):
        a, b = b, a+b
    return a
