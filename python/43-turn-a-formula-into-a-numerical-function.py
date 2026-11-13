# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x,a = sp.symbols("x a",real=True)
expression = a*x**2+1
numeric = sp.lambdify((x,a),expression,modules="math")
results = {"Symbolic formula": expression, "Numeric at (3,2)": numeric(3,2),
           "Exact substitution": expression.subs({x:3,a:2}),
           "Swapped inputs": numeric(2,3)}


for label, value in results.items():
    print(f"{label}: {value}")
