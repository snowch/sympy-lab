# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x")
original = 1/(x*(x+1))
decomposed = sp.apart(original,x)
results = {"Original": original, "Partial fractions": decomposed,
           "Difference check": sp.cancel(decomposed-original)}


for label, value in results.items():
    print(f"{label}: {value}")
