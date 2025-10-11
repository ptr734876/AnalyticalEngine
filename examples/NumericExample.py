import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from algorithms.NumericalMethods import NumericalMethods
from math import cos, tan, pi, exp, sqrt, atan
import matplotlib.pyplot as plt
import numpy as np

def numeric_methods_dz54():
    const = -3
    def f(x):
        return 2 - const * (1/tan(x))
    
    def fxy(x, y):
        return (y-2)/cos(x)
    
    s = -exp(1)
    e = -sqrt(2)

    x0 = s
    y0 = f(x0)
    xn = e
    step = 0.01
    x, y = NumericalMethods.euler_method(fxy, x0, y0, xn, step=step)
    plt.plot(x, y, label='Euler')
    x, y = NumericalMethods.sci_method(fxy, x0, y0, xn, step=step)
    plt.plot(x, y, label='SCI')
    x, y = NumericalMethods.runge_kut_4(fxy, x0, y0, xn, step=step)
    plt.plot(x, y, label='runge')
    x, y = NumericalMethods.analytical(f, x0, y0, xn, step=step)
    plt.plot(x, y, label='analyt')
    plt.title('Numbers')
    plt.legend()
    plt.show()

def numeric_methods_dz52():
    y0_analytical = -20
    x0_analytical = 20
    
    A = x0_analytical / exp(sqrt(y0_analytical**2 + 1))
    
    def f(y):
        """Аналитическое решение: x как функция от y"""
        return A * exp(sqrt(y**2 + 1))
    
    def fxy(x, y):
        """Правая часть ДУ: dx/dy = x*y/sqrt(y^2 + 1)"""
        if abs(y) < 1e-10:  # избегаем деления на ноль
            return 0
        return x * y / sqrt(y**2 + 1)
    
    # Диапазон для y (поскольку у нас dx/dy)
    s = 0.1  # начальное y
    e = 3.0  # конечное y
    
    x0 = f(s)  # начальное x из аналитического решения
    y0 = s
    yn = e
    step = 0.01
    
    # Численные методы (используем y как независимую переменную)
    y_vals, x_vals = NumericalMethods.euler_method(fxy, y0, x0, yn, step=step)
    plt.plot(x_vals, y_vals, label='Euler')
    
    y_vals, x_vals = NumericalMethods.sci_method(fxy, y0, x0, yn, step=step)
    plt.plot(x_vals, y_vals, label='SCI')
    
    y_vals, x_vals = NumericalMethods.runge_kut_4(fxy, y0, x0, yn, step=step)
    plt.plot(x_vals, y_vals, label='runge')
    
    # Аналитическое решение
    y_analytical = np.linspace(s, e, 1000)
    x_analytical = [f(y) for y in y_analytical]
    plt.plot(x_analytical, y_analytical, label='analyt')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Решение: √(y² + 1) dx = xy dy')
    plt.legend()
    plt.grid(True)
    plt.show()

def numeric_methods_dz62():
    const = 1
    def f(x):
        return x + 2 * atan(const * exp(-x))
    
    def fxy(x, y):
        return cos(y - x)
    
    s = pi
    e = pi*pi

    x0 = s
    y0 = f(x0)
    xn = e
    step = 0.01
    
    x, y = NumericalMethods.euler_method(fxy, x0, y0, xn, step=step)
    plt.plot(x, y, label='Euler')
    x, y = NumericalMethods.sci_method(fxy, x0, y0, xn, step=step)
    plt.plot(x, y, label='SCI')
    x, y = NumericalMethods.runge_kut_4(fxy, x0, y0, xn, step=step)
    plt.plot(x, y, label='runge')
    x, y = NumericalMethods.analytical(f, x0, y0, xn, step=step)
    plt.plot(x, y, label='analyt')
    plt.title('Numbers')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    numeric_methods_dz54()
    numeric_methods_dz52()
    numeric_methods_dz62()
