# Copyright © 2026 Christopher Snow
# Exact solution of an authored decay model. Authored teaching example.
import sympy as sp

t = sp.symbols("t",nonnegative=True)
k,N0 = sp.symbols("k N0",positive=True)
N = sp.Function("N")
equation = sp.Eq(sp.diff(N(t),t),-k*N(t))
solution = sp.dsolve(equation,ics={N(0):N0})
results = {"ODE": equation, "Initial-value solution": solution,
           "ODE check": sp.checkodesol(equation,solution),
           "Initial value": solution.rhs.subs(t,0), "Half-life": sp.log(2)/k}


for label, value in results.items():
    print(f"{label}: {value}")
