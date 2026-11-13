# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x = sp.symbols("x",positive=True)
direct = sp.sqrt(x+1)-sp.sqrt(x)
stable = 1/(sp.sqrt(x+1)+sp.sqrt(x))
direct_fn = sp.lambdify(x,direct,"math")
stable_fn = sp.lambdify(x,stable,"math")
exact_input = sp.Integer(10)**16
results = {"Stable form": stable, "Symbolic difference check": sp.simplify(direct-stable),
           "Direct float evaluation": direct_fn(float(exact_input)),
           "Rewritten float evaluation": stable_fn(float(exact_input)),
           "40-digit reference": direct.evalf(40,subs={x:exact_input})}


for label, value in results.items():
    print(f"{label}: {value}")
