# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
C = sp.symbols("C")
rate = 2*x
antiderivative = sp.integrate(rate,x)
defined = sp.Integral(rate,(x,0,3))
results = {"Antiderivative family": antiderivative+C,
           "Derivative residual": sp.diff(antiderivative,x)-rate,
           "Defined accumulation": defined, "Definite value": defined.doit()}


for label, value in results.items():
    print(f"{label}: {value}")
