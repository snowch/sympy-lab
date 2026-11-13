# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x")
equation = sp.Eq(3*x+2,11)
roots = sp.solve(equation,x)
results = {"Equation": equation, "Candidates": roots,
           "Original residuals": [sp.simplify((equation.lhs-equation.rhs).subs(x,r)) for r in roots]}


for label, value in results.items():
    print(f"{label}: {value}")
