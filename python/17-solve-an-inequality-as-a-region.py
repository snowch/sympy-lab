# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
region = sp.reduce_inequalities([x**2<9,x>=1],x)
results = {"Permitted region": region,
           "At 1": region.subs(x,1), "At 3": region.subs(x,3)}


for label, value in results.items():
    print(f"{label}: {value}")
