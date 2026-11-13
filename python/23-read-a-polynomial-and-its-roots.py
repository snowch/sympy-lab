# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x")
expression = (x-1)**2*(x+2)
polynomial = sp.Poly(expression,x)
results = {"Expanded polynomial": polynomial.as_expr(), "Degree": polynomial.degree(),
           "Coefficients, descending powers": polynomial.all_coeffs(),
           "Roots with multiplicities": sp.roots(expression,x)}


for label, value in results.items():
    print(f"{label}: {value}")
