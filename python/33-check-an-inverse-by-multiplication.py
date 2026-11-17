# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

A = sp.Matrix([[2,1],[1,1]])
determinant = A.det()
results = {"Determinant of A": determinant}
if determinant == 0:
    results["Inverse"] = "No inverse"
else:
    inverse = A.inv()
    results["Inverse"] = inverse
    results["Inverse check"] = inverse * A


for label, value in results.items():
    print(f"{label}: {value}")
