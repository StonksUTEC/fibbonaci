from flask import Flask

app = Flask(__name__)
fib = [0, 1]

@app.route('/factorial/<int:n>')
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return f'Factorial is {result}'

@app.route('/fibonacci/<int:n>')
def fibonacci(n):
    if n < len(fib):
        print("already calculated")
        return f'Fibonacci is {fib[n]}'
    else:
        if n == 0:
            return f'Fibonacci is 0'
        first = fib[0]
        second = fib[1]
        for i in range(2, n):
            temp = second
            second = first + second
            first = temp
            fib.append(second)
        
        return f'Fibonacci is {second}'




if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=True)

