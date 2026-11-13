# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.Symbol("x")
expression = x+2
saved_x = x
x = 10
positive_x = sp.Symbol("x",positive=True)
results = {"Existing expression": expression, "Python name now": x,
           "Remaining symbols": expression.free_symbols,
           "Same labels, same objects?": saved_x == positive_x,
           "Explicit replacement": expression.subs(saved_x,10)}


for label, value in results.items():
    print(f"{label}: {value}")
