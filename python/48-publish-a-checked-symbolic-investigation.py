# Copyright © 2026 Christopher Snow
# Reproducible investigation with authored starter models. Authored teaching example.
import sympy as sp

task = "optimisation"  # optimisation, ode, or integral
if task == "optimisation":
    x = sp.symbols("x",real=True)
    volume = x*(12-2*x)**2
    stationary = sp.solve(sp.diff(volume,x),x)
    feasible = [r for r in stationary if 0<r<6]
    best = max(feasible,key=lambda r:volume.subs(x,r))
    results = {"Open-box volume": volume, "Permitted cut": sp.Interval.open(0,6),
               "Best interior cut": best, "Volume there": volume.subs(x,best),
               "Second derivative there": sp.diff(volume,x,2).subs(x,best),
               "Volume at limiting boundaries": [sp.limit(volume,x,0),sp.limit(volume,x,6)]}
elif task == "ode":
    t = sp.symbols("t",nonnegative=True)
    y = sp.Function("y")
    equation = sp.Eq(sp.diff(y(t),t),-2*y(t))
    solution = sp.dsolve(equation,ics={y(0):3})
    results = {"Solution": solution, "ODE check": sp.checkodesol(equation,solution),
               "Initial value": solution.rhs.subs(t,0)}
elif task == "integral":
    x = sp.symbols("x",real=True)
    density = 2*x  # density is zero outside [0,1]
    results = {"Mass on support": sp.integrate(density,(x,0,1)),
               "Exact mean": sp.integrate(x*density,(x,0,1))}
else:
    raise ValueError("Choose optimisation, ode, or integral")


for label, value in results.items():
    print(f"{label}: {value}")
