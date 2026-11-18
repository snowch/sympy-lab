# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x,y = sp.symbols("x y",real=True)
residual = x**2+y**2-25
slope = sp.idiff(residual,y,x)
top = {x:0,y:5}
right = {x:5,y:0}
results = {"Implicit slope": slope, "Top point on curve": residual.subs(top)==0,
           "Slope at top point": slope.subs(top), "Right point on curve": residual.subs(right)==0}


for label, value in results.items():
    print(f"{label}: {value}")
