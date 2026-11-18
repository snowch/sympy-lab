# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
a,b = (x+1)**2,x**2+2*x+1
probes = [0, 1, 2]
results = {"Structural equality": a==b,
           "Polynomial identity check": sp.expand(a-b),
           "Factored difference": sp.factor(a-b),
           "Differences at x=0, 1, 2": [(a-b).subs(x,v) for v in probes],
           "Trigonometric simplification": sp.trigsimp(sp.sin(x)**2+sp.cos(x)**2)}


for label, value in results.items():
    print(f"{label}: {value}")
