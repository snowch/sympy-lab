# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

a,b = sp.symbols("a b",positive=True)
z = sp.symbols("z")
results = {"Positive product expanded": sp.expand_log(sp.log(a*b)),
           "Unrestricted square": sp.expand_log(sp.log(z**2)),
           "Log of product (-1)(-1)": sp.log((-1)*(-1)),
           "Sum of principal logs": sp.log(-1)+sp.log(-1)}


for label, value in results.items():
    print(f"{label}: {value}")
