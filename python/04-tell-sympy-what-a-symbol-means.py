# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

z = sp.Symbol("z")
x = sp.Symbol("x",real=True)
p = sp.Symbol("p",positive=True)
results = {"Unrestricted": sp.sqrt(z**2), "Real": sp.sqrt(x**2),
           "Assumed p": sp.sqrt(p**2), "Real at -3": sp.sqrt(x**2).subs(x,-3)}


for label, value in results.items():
    print(f"{label}: {value}")
