# Copyright © 2026 Christopher Snow
# Symbolic calculation with generated C source. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
expression = x**2+sp.Rational(1,3)
derivative = sp.diff(expression,x)
print("GENERATED C ONLY; not compiled or executed:")
print("value:",sp.ccode(expression))
print("derivative:",sp.ccode(derivative))
results = {"Source expression": expression, "Symbolic derivative": derivative,
           "Exact reference at x=2": expression.subs(x,2)}


for label, value in results.items():
    print(f"{label}: {value}")
