# Copyright © 2026 Christopher Snow
# Exact derivation of an authored motion model. Authored teaching example.
import sympy as sp

t,a,v0,s0 = sp.symbols("t a v0 s0",real=True)
velocity = sp.integrate(a,t)+v0
position = sp.integrate(velocity,t)+s0
results = {"Velocity": velocity, "Position": position,
           "Acceleration residual": sp.diff(position,t,2)-a,
           "Initial velocity": velocity.subs(t,0), "Initial position": position.subs(t,0)}


for label, value in results.items():
    print(f"{label}: {value}")
