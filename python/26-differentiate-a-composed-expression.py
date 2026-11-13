# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
expression = sp.exp(x**2)
derivative = sp.diff(expression,x)
results = {"Function": expression, "Derivative": derivative,
           "Value at 1": expression.subs(x,1), "Slope at 1": derivative.subs(x,1),
           "Second derivative": sp.diff(expression,x,2)}


for label, value in results.items():
    print(f"{label}: {value}")
