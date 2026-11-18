# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

python_input = 0.1
decimal_text = "0.1"
from_python = sp.Float(python_input,50)
from_text = sp.Float(decimal_text,50)
exact = sp.Rational(decimal_text)
results = {"From Python float": from_python, "From decimal text": from_text,
           "Python-input error": (from_python-exact).evalf(12),
           "Text-input error": (from_text-exact).evalf(12),
           "Exact decimal fraction": exact}


for label, value in results.items():
    print(f"{label}: {value}")
