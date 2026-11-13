# Copyright © 2026 Christopher Snow
# Exact solution of an idealised circuit model. Authored teaching example.
import sympy as sp

t = sp.symbols("t",nonnegative=True)
R,C,V = sp.symbols("R C V",positive=True)
v = sp.Function("v")
equation = sp.Eq(R*C*sp.diff(v(t),t)+v(t),V)
solution = sp.dsolve(equation,ics={v(0):0})
results = {"Charging response": solution, "Time constant": R*C,
           "ODE check": sp.checkodesol(equation,solution),
           "Long-time voltage": sp.limit(solution.rhs,t,sp.oo),
           "Fraction at one time constant": sp.simplify(solution.rhs.subs(t,R*C)/V)}


for label, value in results.items():
    print(f"{label}: {value}")
