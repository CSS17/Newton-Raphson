import sympy as sym
from sympy import Symbol, Derivative

def derivative(root,derivated1,function):
    epsilon=0.00000001#10^-8
    x=sym.Symbol("x")
    top=round(float(function.doit().subs({x:root})),8)
    bottom=round(float(derivated1.doit().subs({x:root})),8)
    formula=round(float(root-(float(top/bottom))),8)
    difference=formula-root
    if difference<0:
        print("İteration Result:",formula)
        difference=float(difference)*-1
        print("Difference:",difference)
    if difference>epsilon:
        derivative(formula, derivated1, function)
    else:
        print("Difference:",difference)
        print("Result:",formula)
        
    
def choose_root(a,b):
    x=sym.Symbol("x")
    function=x**3-2*x**2-5
    #You can try this examples too
    #x**3 -7*x**2 +14*x-6 between 0 and 1
    #x**3-2*x**2-5 between 2 and 3
    #x**2 -2 between 1 and 2
    derivated1= Derivative(function, x)
    derivated2= Derivative(derivated1, x)
    
    if (derivated2.doit().subs({x:a})*function.doit().subs({x:a}))>0:
        return derivative(a,derivated1,function)
    else:
        return derivative(b,derivated1,function)
        

choose_root(2, 3)
    
    
