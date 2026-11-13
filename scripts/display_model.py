# Copyright © 2026 Christopher Snow
"""A bounded visual representation of an actual returned symbolic square."""
def area_model(namespace):
    import sympy as sp
    results=namespace.get('results',{})
    if not isinstance(results,dict):return None
    expression=results.get('Original')
    if not isinstance(expression,sp.Expr):return None
    variables=list(expression.free_symbols)
    if len(variables)!=1:return None
    variable=variables[0]
    if variable.is_real is False or variable.is_negative is True:return None
    if len(variable.name)!=1 or not variable.name.isalpha():return None
    if not expression.is_Pow or expression.exp!=2:return None
    offset=sp.simplify(expression.base-variable)
    if not offset.is_Integer or not 1<=offset<=6:return None
    return {'kind':'square-area','variable':variable.name,'offset':int(offset),
            'expression_latex':sp.latex(expression),'expanded_latex':sp.latex(sp.expand(expression)),
            'caption':'Area of the Original expression for nonnegative real inputs. Dimensions are schematic.'}
