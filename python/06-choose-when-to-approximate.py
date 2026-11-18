# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",positive=True)
expression = sp.sqrt(x)+sp.pi
value = 2
results = {"Exact substitution": expression.subs(x,value),
           "12 significant digits": expression.evalf(12,subs={x:value}),
           "40 significant digits": expression.evalf(40,subs={x:value}),
           "Exact root check": sp.sqrt(2)**2-2}


for label, value in results.items():
    print(f"{label}: {value}")
