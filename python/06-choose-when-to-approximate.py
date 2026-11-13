# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",positive=True)
expression = sp.sqrt(x)+sp.pi
results = {"Exact at x=2": expression.subs(x,2),
           "12 significant digits": expression.evalf(12,subs={x:2}),
           "40 significant digits": expression.evalf(40,subs={x:2}),
           "Exact root check": sp.sqrt(2)**2-2}


for label, value in results.items():
    print(f"{label}: {value}")
