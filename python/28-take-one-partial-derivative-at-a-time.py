# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x,y = sp.symbols("x y",real=True)
expression = x**2+x*y+y**2
gradient = sp.Matrix([sp.diff(expression,v) for v in (x,y)])
results = {"Function": expression, "Gradient, order (x,y)": gradient,
           "Gradient at (1,2)": gradient.subs({x:1,y:2}),
           "Mixed partial": sp.diff(expression,x,y)}


for label, value in results.items():
    print(f"{label}: {value}")
