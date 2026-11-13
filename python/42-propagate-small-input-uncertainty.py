# Copyright © 2026 Christopher Snow
# First-order propagation of invented input uncertainty. Authored teaching example.
import sympy as sp

length,width = sp.symbols("length width",positive=True)
outputs = sp.Matrix([length*width,2*(length+width)])
J = outputs.jacobian([length,width])
nominal_J = J.subs({length:2,width:3})
input_covariance = sp.diag(sp.Rational(1,100),sp.Rational(1,25))
output_covariance = nominal_J*input_covariance*nominal_J.T
results = {"Jacobian, input order (length,width)": J,
           "Jacobian at (2,3)": nominal_J,
           "Approximate output covariance, order (area,perimeter)": output_covariance}


for label, value in results.items():
    print(f"{label}: {value}")
