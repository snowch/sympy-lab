# Copyright © 2026 Christopher Snow
# Exact model reference and seeded teaching simulation. Authored teaching example.
import sympy as sp

import numpy as np
import matplotlib.pyplot as plt
r = sp.symbols("r",real=True)
area = sp.pi*r**2
exact_mean = sp.integrate(area,(r,1,2))
exact_variance = sp.simplify(sp.integrate(area**2,(r,1,2))-exact_mean**2)
rng = np.random.default_rng(2026)
radius = rng.uniform(1,2,20000)  # AUTHORED probability model, not measured data
simulated = np.pi*radius**2
estimate = simulated.mean()
mcse = simulated.std(ddof=1)/np.sqrt(len(simulated))
results = {"Exact mean area": exact_mean, "Exact outcome variance": exact_variance,
           "Simulated mean": float(estimate), "Estimated MCSE": float(mcse),
           "Difference in estimated SE units": float((estimate-float(exact_mean))/mcse)}
plt.hist(simulated,bins=35,color="#176b52",alpha=.85)
plt.axvline(float(exact_mean),color="#9b5b2f",linestyle="--",label="Exact model mean")
plt.xlabel("Area (squared length units)"); plt.ylabel("Simulated outcomes")
plt.legend(fontsize=10)


for label, value in results.items():
    print(f"{label}: {value}")
