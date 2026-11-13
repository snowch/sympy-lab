# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

A = sp.Matrix([[1,2],[0,1]])
B = sp.Matrix([[2,0],[1,3]])
v = sp.Matrix([3,4])
results = {"A": A, "Input vector": v, "A acting on v": A*v,
           "A then B": B*A*v, "B then A": A*B*v}


for label, value in results.items():
    print(f"{label}: {value}")
