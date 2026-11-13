# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
expansion = sp.series(sp.sin(x),x,0,7)
polynomial = expansion.removeO()
results = {"Series about zero": expansion, "Polynomial only": polynomial,
           "Error at 1/10": (sp.sin(x)-polynomial).evalf(10,subs={x:sp.Rational(1,10)}),
           "Error at 2": (sp.sin(x)-polynomial).evalf(10,subs={x:2})}


for label, value in results.items():
    print(f"{label}: {value}")
