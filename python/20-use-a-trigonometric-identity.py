# Copyright © 2026 Christopher Snow
# Exact angle conversion and numerical comparison. Authored teaching example.
import sympy as sp

theta = sp.symbols("theta",real=True)
identity = sp.sin(theta)**2+sp.cos(theta)**2
degrees = 30
radians = degrees*sp.pi/180
trig = sp.sin
results = {"Identity simplified": sp.trigsimp(identity),
           "Degree input converted to radians": radians,
           "Exact value at converted angle": trig(radians),
           "Approximate value treating the number as radians": trig(degrees).evalf(8)}


for label, value in results.items():
    print(f"{label}: {value}")
