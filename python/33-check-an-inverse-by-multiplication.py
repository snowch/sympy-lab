# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

A = sp.Matrix([[2,1],[1,1]])
inverse = A.inv()
singular = sp.Matrix([[1,2],[2,4]])
results = {"Determinant of A": A.det(), "Inverse": inverse,
           "Inverse check": inverse*A,
           "Dependent-row determinant": singular.det()}


for label, value in results.items():
    print(f"{label}: {value}")
