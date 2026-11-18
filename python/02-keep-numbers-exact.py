# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

exact = sp.Rational(1,3)
early_float = sp.sympify(1/3)
results = {"Exact input": exact, "Approximate Python input": early_float,
           "Exact sum": exact*3,
           "Stored float as a fraction": sp.Rational(early_float),
           "Stored fraction minus exact": sp.Rational(early_float)-exact,
           "Exact decimal on request": exact.evalf(25)}


for label, value in results.items():
    print(f"{label}: {value}")
