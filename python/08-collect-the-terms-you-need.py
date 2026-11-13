# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x,a,b = sp.symbols("x a b")
expression = a*x+b*x+2*a*x**2+b
results = {"Expression": expression, "Collected in x": sp.collect(expression,x),
           "Coefficient of x": sp.expand(expression).coeff(x,1),
           "Collected in a": sp.collect(expression,a)}


for label, value in results.items():
    print(f"{label}: {value}")
