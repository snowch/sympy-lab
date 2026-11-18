# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x")
original = 1/x+1/(x+1)
combined = sp.together(original)
numerator,denominator = sp.fraction(combined)
results = {"Combined": combined, "Numerator": numerator,
           "Denominator": denominator, "Identity check": sp.cancel(combined-original),
           "Excluded real inputs": sp.solveset(denominator, x, domain=sp.S.Reals)}


for label, value in results.items():
    print(f"{label}: {value}")
