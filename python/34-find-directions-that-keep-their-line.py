# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

A = sp.Matrix([[2,1],[1,2]])
v = sp.Matrix([1,1])
eigenvalue = 3
results = {"Eigenvalues and multiplicities": A.eigenvals(),
           "Eigenspace bases": A.eigenvects(),
           "Chosen direction": v, "Eigen residual": A*v-eigenvalue*v}


for label, value in results.items():
    print(f"{label}: {value}")
