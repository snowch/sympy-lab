# Copyright © 2026 Christopher Snow
# Integrated design with invented dimensions. Authored teaching example.
import sympy as sp

import numpy as np
import matplotlib.pyplot as plt
x = sp.symbols("x",real=True)
volume = x*(12-2*x)*(8-2*x)  # INVENTED sheet, centimetres
stationary = sp.solve(sp.diff(volume,x),x)
feasible = [r for r in stationary if 0<r<4]
best = max(feasible,key=lambda r:volume.subs(x,r))
results = {"Volume in cm cubed": volume, "Feasible cut interval, cm": sp.Interval.open(0,4),
           "All stationary candidates": stationary, "Best cut, exact cm": best,
           "Best cut, approximate cm": best.evalf(8),
           "Second derivative at best": sp.simplify(sp.diff(volume,x,2).subs(x,best)),
           "Limiting boundary volumes": [sp.limit(volume,x,0),sp.limit(volume,x,4)]}
numeric = sp.lambdify(x,volume,"numpy")
grid = np.linspace(0,4,200)
plt.plot(grid,numeric(grid),color="#176b52",linewidth=2)
plt.axvline(float(best),linestyle="--",color="#9b5b2f",label="Exact optimum, plotted numerically")
plt.xlabel("Cut size (cm)"); plt.ylabel("Ideal box volume (cm³)")
plt.legend(fontsize=10)


for label, value in results.items():
    print(f"{label}: {value}")
