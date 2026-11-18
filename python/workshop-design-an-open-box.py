# Copyright © 2026 Christopher Snow
# Integrated design with invented dimensions. Authored teaching example.
import sympy as sp

import numpy as np
import matplotlib.pyplot as plt
x = sp.symbols("x",real=True)
length,width = 12,8  # INVENTED sheet, centimetres
max_cut = sp.Rational(min(length,width),2)
volume = x*(length-2*x)*(width-2*x)
stationary = sp.solve(sp.diff(volume,x),x)
feasible = [r for r in stationary if 0<r<max_cut]
best = max(feasible,key=lambda r:volume.subs(x,r))
results = {"Volume in cm cubed": volume, "Feasible cut interval, cm": sp.Interval.open(0,max_cut),
           "All stationary candidates": stationary, "Best cut, exact cm": best,
           "Best cut, approximate cm": best.evalf(8),
           "Second derivative at best": sp.simplify(sp.diff(volume,x,2).subs(x,best)),
           "Limiting boundary volumes": [sp.limit(volume,x,0),sp.limit(volume,x,max_cut)]}
numeric = sp.lambdify(x,volume,"numpy")
grid = np.linspace(0,float(max_cut),200)
plt.plot(grid,numeric(grid),color="#176b52",linewidth=2)
plt.axvline(float(best),linestyle="--",color="#9b5b2f",label="Exact optimum, plotted numerically")
plt.xlabel("Cut size (cm)"); plt.ylabel("Ideal box volume (cm³)")
plt.legend(fontsize=10)


for label, value in results.items():
    print(f"{label}: {value}")
