import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from algorithms.NumericalMethods import NumericalMethods
from math import cos, tan, pi, sin, log, sqrt, exp
import matplotlib.pyplot as plt
from visualization.d2 import plotter2d
import numpy
numpy.array_equal()

def numeric_mothods_dz54():
    const = 1
    def f(x):
        return const*(sin(x)+1)/cos(x) + 2
    
    def fxy(x, y):
        return (y-2)/cos(x)
    
    s = -pi
    e = pi*2

    x0 = s
    y0 = f(x0)
    xn = e
    step = 0.001
    a = plotter2d(*NumericalMethods.euler_method(fxy, x0, y0, xn, step=step), 'Euler')
    b = plotter2d(*NumericalMethods.sci_method(fxy, x0, y0, xn, step=step), 'SCI')
    c = plotter2d(*NumericalMethods.runge_kut_4(fxy, x0, y0, xn, step=step), 'runge')
    d = plotter2d(*NumericalMethods.analytical(f, x0, y0, xn, step=step), 'analyt')
    # a.show()
    # b.show()
    # c.show()
    d.show()
    # plotter2d.compareplots([a,b,c,d], title='numeric methods 54')

def numeric_mothods_dz111():
    const = -3
    def f(x):
        n=1
        return (-1 * x * log(log(x)))
    
    def fxy(x, y):
        return (y/x) - exp(y/x)
    # dz 262-266 and 268-272 parametrs
    s = pi
    e = pi ** 3
    x0 = s
    y0 = f(x0)
    xn = e
    step = 0.01 
    a = plotter2d(*NumericalMethods.euler_method(fxy, x0, y0, xn, step=step), 'Euler')
    b = plotter2d(*NumericalMethods.sci_method(fxy, x0, y0, xn, step=step), 'SCI')
    c = plotter2d(*NumericalMethods.runge_kut_4(fxy, x0, y0, xn, step=step), 'runge')
    d = plotter2d(*NumericalMethods.analytical(f, x0, y0, xn, step=step), 'analyt')
    # a.show()
    # b.show()
    # c.show()
    # d.show()
    print(a, b)
    plotter2d.compareplots([a, b, c ,d])

def numeric_mothods_dz112():
    const = -3
    def f(x):
        n=1
        return x*sin(log(x)+const)
    
    def fxy(x, y):
        if x * x - y * y < 0:
            return y/x
        return (sqrt(x*x - y*y)+ y)/x
    # dz 262-266 and 268-272 parametrs
    s = -pi**4
    e = pi ** 4
    x0 = s
    y0 = f(x0)
    xn = e
    step = 0.01 
    a = plotter2d(*NumericalMethods.euler_method(fxy, x0, y0, xn, step=step), 'Euler')
    b = plotter2d(*NumericalMethods.sci_method(fxy, x0, y0, xn, step=step), 'SCI')
    c = plotter2d(*NumericalMethods.runge_kut_4(fxy, x0, y0, xn, step=step), 'runge')
    d = plotter2d(*NumericalMethods.analytical(f, x0, y0, xn, step=step), 'analyt')
    # a.show()
    # b.show()
    # c.show()
    # d.show()
    plotter2d.compareplots([a, b, c ,d])

if __name__ == '__main__':
    # numeric_mothods_dz54()
    numeric_mothods_dz112()
