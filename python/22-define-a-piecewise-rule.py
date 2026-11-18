# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
rule = sp.Piecewise((-x,x<0),(x,True))
inputs = [-2,0,2]
results = {"Piecewise rule": rule, "Inputs and values": [(v,rule.subs(x,v)) for v in inputs]}


for label, value in results.items():
    print(f"{label}: {value}")
