# Copyright © 2026 Christopher Snow
# Integrated ideal circuit with invented components. Authored teaching example.
import sympy as sp

import numpy as np
import matplotlib.pyplot as plt
t = sp.symbols("t",real=True)
R,C,V = sp.symbols("R C V",positive=True)
response = V*(1-sp.exp(-t/(R*C)))
crossing = sp.solve(sp.Eq(response,V/2),t)[0]
parameters = {R:1000,C:sp.Rational(1,10000),V:5}  # INVENTED SI inputs
results = {"Charging response": response, "Half-voltage time": crossing,
           "Threshold residual": sp.simplify(response.subs(t,crossing)-V/2),
           "Illustrative crossing, seconds": crossing.subs(parameters).evalf(8),
           "Sensitivity to R": sp.diff(crossing,R)}
numeric = sp.lambdify(t,response.subs(parameters),"numpy")
grid = np.linspace(0,.5,200)
plt.plot(grid,numeric(grid),color="#176b52",linewidth=2)
plt.axhline(2.5,linestyle="--",color="#9b5b2f",label="Half the final voltage")
plt.xlabel("Time (s)"); plt.ylabel("Ideal capacitor voltage (V)")
plt.legend(fontsize=10)


for label, value in results.items():
    print(f"{label}: {value}")
