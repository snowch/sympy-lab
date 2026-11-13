# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x")
polynomial = x**2+x-6
factored = sp.factor(polynomial)
results = {"Polynomial": polynomial, "Factored": factored,
           "Expanded again": sp.expand(factored),
           "Identity check": sp.expand(factored-polynomial)}


for label, value in results.items():
    print(f"{label}: {value}")
