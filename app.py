from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Bisection method implementation
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if a >= b:
        return "Error: Lower bound (a) must be less than upper bound (b)."
    if f(a) * f(b) > 0:
        return "Error: f(a) and f(b) must have opposite signs."

    iterations = 0
    result = []

    while abs(b - a) > tol and iterations < max_iter:
        c = (a + b) / 2
        fc = f(c)
        result.append(f"Iteration {iterations}: a={a:.6f}, b={b:.6f}, f(c)={fc:.6f}")
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        iterations += 1

    root = (a + b) / 2
    result.append(f"Final Approximate Root: {root:.6f}")
    return "<br>".join(result)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bisection', methods=['GET', 'POST'])
def bisection():
    output = ""
    if request.method == 'POST':
        func_str = request.form['function']
        a = float(request.form['a'])
        b = float(request.form['b'])

        # Define the user function safely
        def user_function(x):
            return eval(func_str)

        try:
            output = bisection_method(user_function, a, b)
        except Exception as e:
            output = f"Error: {str(e)}"

    return render_template('bisection.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
