# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
function = sp.sin(x)
center = 0
expansion = sp.series(function,x,center,7)
polynomial = expansion.removeO()
results = {"Series": expansion, "Polynomial only": polynomial,
           "Error at center + 1/10": (function-polynomial).evalf(10,subs={x:center+sp.Rational(1,10)}),
           "Error at center + 2": (function-polynomial).evalf(10,subs={x:center+2})}


for label, value in results.items():
    print(f"{label}: {value}")
