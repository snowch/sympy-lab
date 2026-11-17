# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
hole = 1
denominator = x - hole
original = (x**2 - hole**2) / denominator
reduced = sp.cancel(original)
results = {"Original denominator": denominator, "Cancelled formula": reduced,
           "Excluded input": sp.solveset(denominator, x, domain=sp.S.Reals),
           f"Original at {hole}": "Undefined",
           f"Cancelled formula at {hole}": reduced.subs(x, hole)}


for label, value in results.items():
    print(f"{label}: {value}")
