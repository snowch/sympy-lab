# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

k = sp.symbols("k",integer=True)
n = sp.symbols("n",integer=True,positive=True)
defined_sum = sp.Sum(k,(k,1,n))
closed_form = defined_sum.doit()
results = {"Defined sum": defined_sum, "Closed form": closed_form,
           "At n=4": closed_form.subs(n,4),
           "Finite product at 4": sp.Product(k,(k,1,4)).doit()}


for label, value in results.items():
    print(f"{label}: {value}")
