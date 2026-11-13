# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x")
expression = x**3-x
roots = [sp.nsolve(expression,x,guess,prec=35) for guess in [-1.2,.1,1.2]]
results = {"Roots from three guesses": roots,
           "Residuals": [expression.evalf(12,subs={x:r}) for r in roots]}


for label, value in results.items():
    print(f"{label}: {value}")
