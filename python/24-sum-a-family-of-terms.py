# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

k = sp.symbols("k",integer=True)
n = sp.symbols("n",integer=True,positive=True)
term = k
check_n = 4
defined_sum = sp.Sum(term,(k,1,n))
closed_form = defined_sum.doit()
results = {"Defined sum": defined_sum, "Closed form": closed_form,
           f"Sum at n={check_n}": closed_form.subs(n,check_n),
           "Finite product at 4": sp.Product(k,(k,1,4)).doit()}


for label, value in results.items():
    print(f"{label}: {value}")
