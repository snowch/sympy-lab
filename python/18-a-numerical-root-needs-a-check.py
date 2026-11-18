# Copyright © 2026 Christopher Snow
# Numerical roots with original residual checks. Authored teaching example.
import sympy as sp

x = sp.symbols("x")
expression = x**3-x
guesses = [-1.2,.1,1.2]
roots = [sp.nsolve(expression,x,guess,prec=35) for guess in guesses]
results = {"Starting guesses": guesses, "Numerical roots": roots,
           "Residuals": [expression.evalf(12,subs={x:r}) for r in roots]}


for label, value in results.items():
    print(f"{label}: {value}")
