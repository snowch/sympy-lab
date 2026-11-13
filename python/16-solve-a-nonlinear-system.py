# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x,y = sp.symbols("x y",real=True)
residuals = [x**2+y**2-5,y-x+1]
solutions = sp.nonlinsolve(residuals,(x,y))
checks = [tuple(sp.simplify(r.subs({x:a,y:b})) for r in residuals) for a,b in sorted(solutions,key=str)]
results = {"Intersection points": solutions, "Original checks": checks}


for label, value in results.items():
    print(f"{label}: {value}")
