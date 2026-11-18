# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x")
expression = x**2+1
results = {"Real solutions": sp.solveset(expression,x,domain=sp.S.Reals),
           "Complex solutions": sp.solveset(expression,x,domain=sp.S.Complexes),
           "Complex candidate residuals": [expression.subs(x,r) for r in sp.solveset(expression,x,domain=sp.S.Complexes)]}


for label, value in results.items():
    print(f"{label}: {value}")
