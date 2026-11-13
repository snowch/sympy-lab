# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

A = sp.Matrix([[2,1],[1,2]])
P,D = A.diagonalize()
J = sp.Matrix([[1,1],[0,1]])
results = {"Basis matrix P": P, "Diagonal matrix D": D,
           "Reconstruction residual": P*D*P.inv()-A,
           "Power residual": P*D**5*P.inv()-A**5,
           "Is J diagonalizable?": J.is_diagonalizable()}


for label, value in results.items():
    print(f"{label}: {value}")
