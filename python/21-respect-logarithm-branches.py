# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

a,b = sp.symbols("a b",positive=True)
z = sp.symbols("z")
power = sp.Rational(1,2)
results = {"Positive product expanded": sp.expand_log(sp.log(a*b)),
           "Power inside logarithm": power,
           "Unrestricted input rule": sp.expand_log(sp.log(z**power)),
           "Positive input rule": sp.expand_log(sp.log(a**power)),
           "Log of product (-1)(-1)": sp.log((-1)*(-1)),
           "Sum of principal logs": sp.log(-1)+sp.log(-1)}


for label, value in results.items():
    print(f"{label}: {value}")
