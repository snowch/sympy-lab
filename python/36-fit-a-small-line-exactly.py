# Copyright © 2026 Christopher Snow
# Exact fit to invented observations. Authored teaching example.
import sympy as sp

A = sp.Matrix([[1,0],[1,1],[1,2]])
b = sp.Matrix([1,2,2])  # INVENTED observations
coefficients = (A.T*A).LUsolve(A.T*b)
residual = b-A*coefficients
results = {"Intercept and slope": coefficients,
           "Observed minus fitted": residual,
           "Orthogonality check": A.T*residual,
           "Squared error": (residual.T*residual)[0]}


for label, value in results.items():
    print(f"{label}: {value}")
