# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x,y = sp.symbols("x y")
expression = x+2*y
# For the fraction variant, limit the comparison to x != 0 and y != 0.
sequential = expression.subs([(x,y),(y,x)])
swapped = expression.subs({x:y,y:x},simultaneous=True)
results = {"Original": expression, "Sequential": sequential,
           "Simultaneous swap": swapped,
           "Numerical inputs": expression.subs({x:1,y:3})}


for label, value in results.items():
    print(f"{label}: {value}")
