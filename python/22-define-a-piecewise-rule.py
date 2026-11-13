# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
rule = sp.Piecewise((-x,x<0),(x,True))
results = {"Piecewise rule": rule, "At -2, 0, 2": [rule.subs(x,v) for v in [-2,0,2]],
           "Equivalent absolute-value notation": sp.Abs(x)}


for label, value in results.items():
    print(f"{label}: {value}")
