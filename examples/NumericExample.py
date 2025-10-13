import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from algorithms.NumericalMethods import NumericalMethods
from math import cos, tan, pi, exp, atan
import matplotlib.pyplot as plt
from visualization.d2 import plotter2d

def numeric_methods_dz54():
    const = 6
    def f(x):
        return 2 - const * (1/tan(x))
    
    def fxy(x, y):
        return (y-2)/cos(x)
    
    s = pi
    e = pi**2

    x0 = s
    y0 = f(x0)
    xn = e
    step = 0.01
    a = plotter2d(*NumericalMethods.euler_method(fxy, x0, y0, xn, step=step), 'Euler')
    b = plotter2d(*NumericalMethods.sci_method(fxy, x0, y0, xn, step=step), 'SCI')
    c = plotter2d(*NumericalMethods.runge_kut_4(fxy, x0, y0, xn, step=step), 'runge')
    d = plotter2d(*NumericalMethods.analytical(f, x0, y0, xn, step=step), 'analyt')
    print(a, b, c, d)

def numeric_methods_dz62():
    const = 1
    def f(x):
        return x + 2 * atan(const * exp(-x))
    
    def fxy(x, y):
        return cos(y - x)
    
    s = -pi
    e = pi**3

    x0 = s
    y0 = f(x0)
    xn = e
    step = 0.01
    
    a = plotter2d(*NumericalMethods.euler_method(fxy, x0, y0, xn, step=step), 'Euler')
    b = plotter2d(*NumericalMethods.sci_method(fxy, x0, y0, xn, step=step), 'SCI')
    c = plotter2d(*NumericalMethods.runge_kut_4(fxy, x0, y0, xn, step=step), 'runge')
    d = plotter2d(*NumericalMethods.analytical(f, x0, y0, xn, step=step), 'analyt')
    print(a, b, c, d)

if __name__ == '__main__':
    # numeric_methods_dz54()
    numeric_methods_dz62()
