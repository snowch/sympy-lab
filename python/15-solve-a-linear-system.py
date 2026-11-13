# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x,y = sp.symbols("x y")
residuals = [x+y-10,2*x+3*y-24]
solutions = sp.linsolve(residuals,(x,y))
pair = next(iter(solutions))
results = {"Solution tuples (x,y)": solutions,
           "Checks": [r.subs(dict(zip((x,y),pair))) for r in residuals]}


for label, value in results.items():
    print(f"{label}: {value}")
