# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
original = (x**2-1)/(x-1)
reduced = sp.cancel(original)
results = {"Original": original, "Cancelled": reduced,
           "Excluded input": sp.FiniteSet(1),
           "Original at 1": original.subs(x,1), "Reduced at 1": reduced.subs(x,1)}


for label, value in results.items():
    print(f"{label}: {value}")
