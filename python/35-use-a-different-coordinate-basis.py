# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

A = sp.Matrix([[2,1],[1,2]])
P,D = A.diagonalize()
J = sp.Matrix([[1,1],[0,1]])
power = 5
results = {"Basis matrix P": P, "Diagonal matrix D": D,
           "Reconstruction residual": P*D*P.inv()-A,
           "Power residual": P*D**power*P.inv()-A**power,
           "Is J diagonalizable?": J.is_diagonalizable(), "J eigenspace basis": J.eigenvects()}


for label, value in results.items():
    print(f"{label}: {value}")
