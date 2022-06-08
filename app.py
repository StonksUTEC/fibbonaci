from flask import Flask
import math
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"


@app.route('/factorial/<int:n>')
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return f"Factorial is: {result}"

def fibonacci_formula(n):
    phi = (1 + math.sqrt(5))/2
    left = pow(phi,n)
    right = pow(-phi, -n)
    return (left - right)/math.sqrt(5)

@app.route('/fibonacci/<int:n>')
def fibonacci(n):
    
    return f"Fibonacci is: {int(fibonacci_formula(n))}"


@app.route('/<name>')
def my_view_func(name):
    return name


if __name__ == "__main__":
    print(fibonacci_formula(2))
    app.run(debug=True)
