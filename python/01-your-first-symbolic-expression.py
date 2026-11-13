# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x")
expression = (x+1)**2
results = {"Original": expression, "Expanded": sp.expand(expression)}


for label, value in results.items():
    print(f"{label}: {value}")
