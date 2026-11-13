# Copyright © 2026 Christopher Snow
# Exact calculation for an authored density. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
density = 2*x
mass = sp.integrate(density,(x,0,1))
mean = sp.integrate(x*density,(x,0,1))
variance = sp.integrate(x**2*density,(x,0,1))-mean**2
results = {"Mass on [0,1]": mass, "Mean": mean, "Variance": variance,
           "P(X > 3/4)": sp.integrate(density,(x,sp.Rational(3,4),1))}


for label, value in results.items():
    print(f"{label}: {value}")
