# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

x,a,b = sp.symbols("x a b",real=True)
expression = a*x**2+b
numeric = sp.lambdify((x,a,b),expression,modules="math")
inputs = (3,2,1)
x_value,a_value,b_value = inputs
results = {"Symbolic formula": expression, "Inputs in order (x,a,b)": inputs,
           "Numerical result": numeric(x_value,a_value,b_value),
           "Exact substitution": expression.subs({x:x_value,a:a_value,b:b_value}),
           "Swapped x and a": numeric(a_value,x_value,b_value)}


for label, value in results.items():
    print(f"{label}: {value}")
