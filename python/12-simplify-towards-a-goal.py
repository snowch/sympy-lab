# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
a,b = (x+1)**2,x**2+2*x+1
results = {"Structural equality": a==b,
           "Polynomial identity check": sp.expand(a-b),
           "Trigonometric simplification": sp.trigsimp(sp.sin(x)**2+sp.cos(x)**2)}


for label, value in results.items():
    print(f"{label}: {value}")
