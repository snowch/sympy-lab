# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
expression = sp.sin(x)/x
left = sp.limit(expression, x, 0, dir="-")
right = sp.limit(expression, x, 0, dir="+")
results = {"Direct at zero": expression.subs(x,0),
           "Limit from the left": left,
           "Limit from the right": right,
           "Two-sided limit": left if left == right else "Does not exist"}


for label, value in results.items():
    print(f"{label}: {value}")
