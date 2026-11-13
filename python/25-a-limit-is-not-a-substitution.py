# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
expression = sp.sin(x)/x
results = {"Direct at zero": expression.subs(x,0),
           "Limit at zero": sp.limit(expression,x,0),
           "1/x from left": sp.limit(1/x,x,0,dir="-"),
           "1/x from right": sp.limit(1/x,x,0,dir="+")}


for label, value in results.items():
    print(f"{label}: {value}")
