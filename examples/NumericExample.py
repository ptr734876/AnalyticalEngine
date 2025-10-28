import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from algorithms.NumericalMethods import NumericalMethods
from math import cos, tan, pi, sin, log, sqrt, exp
import matplotlib.pyplot as plt
from visualization.d2 import plotter2d
import numpy

def numeric_mothods_dz54():
    const = 1
    def f(x):
        return 2 + const*cos(x)
    
    def fxy(x, y):
        return (2 - y) * tan(x)
    
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
    # d.show()
    plotter2d.compareplots([a,b,c,d], title='numeric methods 54')

def numeric_mothods_dz111():
    def f(x):
        n=1
        return (-1 * x * log(log(x)))
    
    def fxy(x, y):
        return (y/x) - exp(y/x)
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
    # print(a, b)
    plotter2d.compareplots([a, b, c ,d], title='numeric methods 111')

def numeric_mothods_dz154():
    const = pi**4
    def f(x):
        n=1
        return (-3 * x**3 + x**3 * const) ** (1/3)
    def fxy(x, y):
        return (x**2 + y**3)/(x*y**2)
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
    # print(a, b)
    plotter2d.compareplots([a, b, c ,d], title='numeric methods 154')

def dz():
    def f(y, y_pred, x, h):
        return ((y-y_pred) / h)**3 + (y - y_pred)/h - x
    s = pi
    e = pi ** 3
    x0 = s
    y0 = 1
    xn = e
    step = 0.01
    a = plotter2d(*NumericalMethods.end_subs_method(f, x0, y0, xn, step), '')
    a.show()

def analit_dz():
    z = numpy.linspace(0,1, 1001)
    a = plotter2d([i**3 + i for i in z], [(3/4) * i**4 + (i**2)/2 + 1 for i in z], '')
    a.show()

if __name__ == '__main__':
    numeric_mothods_dz54()
    # numeric_mothods_dz111()
    # numeric_mothods_dz154()
    # analit_dz()
    # dz()