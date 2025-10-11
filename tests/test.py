import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from core.complex_numbers import complex, trigcomplex
from algorithms.digits import pinum
from algorithms.NumericalMethods import NumericalMethods
from visualization.d2 import plotter2d

def test_complex():
    print('-----test_complex-----')
    # creating complex numbers
    a = complex(1, 1)
    print('a = complex(1, 1) -> ', a)
    b = complex(1, 3)
    print('b = complex(1, 3) -> ', b)
    c = complex(1, 1)
    print('c = complex(1, 1) -> ', c)
    # operations with complex numbers
    print('sum a+b -> ', a+b)
    print('multy a*b -> ', a * b)
    print('truediv a / b -> ', a/b)
    print('c==a then a==b -> ', a == c, a ==b)
    print('a > b -> ', a > b)
    print('abs(b) module -> ', abs(b))
    print('pow b**4 -> ', b**4)
    # from complex to triginometrical complex number
    print('from complex a -> ', a, 'to trigonometrical a -> ', a.complex_to_trig())
    #test with int\float
    print('a * 5 -> ', a * 5)
    print('a * 2.4 -> ', a * 2.4)
    print('a / 2 -> ', a / 2)
    print('a / 2.4 -> ', a / 2.4)
    print('a - 5 -> ',a-5 )
    print('a - 2.4 -> ',a - 2.4)
    print('a + 5 -> ', a + 5)
    print('a + 2.4 -> ', a + 2.4)

def test_trigcomplex():
    print('-----test_trigcomplex-----')
    # creating trigonometrical complex number
    a = trigcomplex(2, 60) # pfi in grages
    print('a = trigcomplex(2, 60) -> ', a)
    b = trigcomplex(5, 30)
    print('b = trigcomplex(5, 30) -> ', b)
    # operation on trigonometrical number form
    print('a + b -> ', a + b)
    print('a - b -> ', a - b)
    print('a * b -> ', a * b)
    print('a / b -> ', a / b)
    print('a ** 3 -> ', a**3)
    print('abs(b) module -> ', abs(b))
    #transfer trigonometrical form to complex
    print(f'trigonometrical a:{a} to complex -> ', a.trig_to_complex())
    #test with int\float
    print('a * 5 -> ', a * 5)
    print('a * 2.4 -> ', a * 2.4)
    print('a / 2 -> ', a / 2)
    print('a / 2.4 -> ', a / 2.4)
    print('a - 5 -> ',a-5 )
    print('a - 2.4 -> ',a - 2.4)
    print('a + 5 -> ', a + 5)
    print('a + 2.4 -> ', a + 2.4)

def test_complex_and_trig():
    print('-----test_complex_and_trig-----')
    #creating complex and trig complex numbers
    a = complex(12, 14)
    print('a = complex(12, 14) -> ', a)
    b = trigcomplex(5, 45)
    print('b = trigcomplex(5, 45) -> ', b)
    print('a + b -> ', a + b)
    print('a - b -> ', a - b)
    print('a * b -> ', a * b)
    print('a / b -> ', a / b)
    #replace a with b
    b = complex(12, 14)
    print('b = complex(12, 14) -> ', b)
    a = trigcomplex(5, 45)
    print('a = trigcomplex(5, 45) -> ', a)
    print('a + b -> ', a + b)
    print('a - b -> ', a - b)
    print('a * b -> ', a * b)
    print('a / b -> ', a / b)

def test_pinum():
    print(pinum(60))
    import math
    print(math.degrees(math.radians(60)))

def numeric_methods_dz54():
    from math import cos, tan, pi, exp, sqrt
    import matplotlib.pyplot as plt
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
    from math import exp, sqrt
    import matplotlib.pyplot as plt
    import numpy as np
    
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
    from math import atan, cos, exp, pi
    import matplotlib.pyplot as plt
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


def test_2d():
    a = plotter2d()
    b = plotter2d(figsize=(1, 2))
    a.show()
    b.show()

    

# test_complex()
#test_trigcomplex()
# test_complex_and_trig()
numeric_methods_dz54()
numeric_methods_dz52()
numeric_methods_dz62()
# test_2d()