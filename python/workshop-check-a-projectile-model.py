# Copyright © 2026 Christopher Snow
# Integrated model with invented launch inputs. Authored teaching example.
import sympy as sp

import numpy as np
import matplotlib.pyplot as plt
t = sp.symbols("t",real=True)
v0,g = sp.symbols("v0 g",positive=True)
initial_height = 0  # INVENTED height, metres
height = initial_height+v0*t-g*t**2/2
roots = sp.solve(height,t)
return_time = next(root for root in roots if root.is_positive)
apex_time = sp.solve(sp.diff(height,t),t)[0]
parameters = {v0:12,g:sp.Rational(981,100)}  # INVENTED inputs, SI units
end = float(return_time.subs(parameters))
results = {"Height, metres": height, "Ground roots": roots,
           "Return time, seconds": return_time, "Illustrative return time, seconds": end,
           "Apex time, seconds": apex_time,
           "Apex height, metres": sp.simplify(height.subs(t,apex_time)),
           "Acceleration residual": sp.diff(height,t,2)+g,
           "Initial height": height.subs(t,0), "Initial velocity": sp.diff(height,t).subs(t,0)}
numeric = sp.lambdify(t,height.subs(parameters),"numpy")
grid = np.linspace(0,end,200)
plt.plot(grid,numeric(grid),color="#176b52",linewidth=2)
plt.xlabel("Time after launch (s)"); plt.ylabel("Ideal height (m)")
plt.grid(alpha=.2)


for label, value in results.items():
    print(f"{label}: {value}")
