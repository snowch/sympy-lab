# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

theta = sp.symbols("theta",real=True)
identity = sp.sin(theta)**2+sp.cos(theta)**2
radians = 30*sp.pi/180
results = {"Identity simplified": sp.trigsimp(identity),
           "Thirty degrees in radians": radians,
           "Exact sine of thirty degrees": sp.sin(radians),
           "Thirty radians, approximate": sp.sin(30).evalf(8)}


for label, value in results.items():
    print(f"{label}: {value}")
