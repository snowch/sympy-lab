# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
f = sp.Lambda(x,x+1)
g = sp.Lambda(x,x**2)
results = {"f after g": f(g(x)), "g after f": g(f(x)),
           "f(g(2))": f(g(2)), "g(f(2))": g(f(2))}


for label, value in results.items():
    print(f"{label}: {value}")
