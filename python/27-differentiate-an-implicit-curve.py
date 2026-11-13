# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x,y = sp.symbols("x y",real=True)
residual = x**2+y**2-25
slope = sp.idiff(residual,y,x)
results = {"Implicit slope": slope, "At (3,4)": slope.subs({x:3,y:4}),
           "At (0,5)": slope.subs({x:0,y:5}),
           "Curve check at (5,0)": residual.subs({x:5,y:0})}


for label, value in results.items():
    print(f"{label}: {value}")
