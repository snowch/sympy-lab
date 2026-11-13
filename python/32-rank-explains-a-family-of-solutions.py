# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x,y = sp.symbols("x y")
A = sp.Matrix([[1,1],[2,2]])
b = sp.Matrix([3,6])
bad_b = sp.Matrix([3,7])
results = {"Coefficient rank": A.rank(), "Compatible augmented rank": A.row_join(b).rank(),
           "Solution family": sp.linsolve((A,b),(x,y)),
           "Conflicting augmented rank": A.row_join(bad_b).rank(),
           "Conflicting solutions": sp.linsolve((A,bad_b),(x,y))}


for label, value in results.items():
    print(f"{label}: {value}")
