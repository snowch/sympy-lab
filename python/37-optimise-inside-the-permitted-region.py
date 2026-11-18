# Copyright © 2026 Christopher Snow
# Exact optimisation of an authored model. Authored teaching example.
import sympy as sp

x = sp.symbols("x",real=True)
objective = x*(10-x)
stationary = sp.solve(sp.diff(objective,x),x)
upper = 4
candidates = [sp.Integer(0),sp.Integer(upper)]+[r for r in stationary if 0<=r<=upper]
best = max(candidates,key=lambda r:objective.subs(x,r))
results = {"Objective": objective, "Unconstrained stationary points": stationary,
           "Feasible candidates": candidates, "Best feasible x": best,
           "Best value": objective.subs(x,best)}


for label, value in results.items():
    print(f"{label}: {value}")
