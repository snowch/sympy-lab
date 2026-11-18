# Copyright © 2026 Christopher Snow
# Symbolic curve and sampled numerical values. Authored teaching example.
import sympy as sp

import numpy as np
import matplotlib.pyplot as plt
x = sp.symbols("x",nonnegative=True)
expression = sp.exp(-x)
numeric = sp.lambdify(x,expression,modules="numpy")
end = 4
points = 200
grid = np.linspace(0,float(end),points)
values = numeric(grid)
results = {"Symbolic curve": expression, "Exact starting value": expression.subs(x,0),
           "Sampled endpoint": float(values[-1]), "Grid points": len(grid)}
plt.plot(grid,values,color="#176b52",linewidth=2)
plt.xlabel("x, dimensionless")
plt.ylabel(str(expression))
plt.grid(alpha=.2)


for label, value in results.items():
    print(f"{label}: {value}")
