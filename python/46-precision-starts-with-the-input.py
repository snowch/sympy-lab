# Copyright © 2026 Christopher Snow
# Exact symbolic investigation. Authored teaching example.
import sympy as sp

from_python = sp.Float(0.1,50)
from_text = sp.Float("0.1",50)
exact = sp.Rational(1,10)
results = {"From Python float": from_python, "From decimal text": from_text,
           "Python-input error": (from_python-exact).evalf(12),
           "Text-input error": (from_text-exact).evalf(12),
           "Exact tenth": exact}


for label, value in results.items():
    print(f"{label}: {value}")
