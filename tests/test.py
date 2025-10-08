import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from core.complex_numbers import complex, trigcomplex
from algorithms.digits import pinum
from algorithms.NumericalMethods import NumericalMethods

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

def test_numericalmethods():
    from math import pi, exp
    from visualization.d2 import line2d
    const = 2
    def f(x):
        return (x/const - 1) * x
    
    def fxy(x, y):
        return (x + 2 * y) / x
    
    s = -pi*2
    e = exp(1) * 2

    x0 = s
    y0 = f(x0)
    xn = e
    x_values, approximated_y = NumericalMethods.euler_method(fxy, x0, y0, xn, step=0.1)
    line2d(x_values,approximated_y)

if __name__ == '__main__':
    # test_complex()
    # test_trigcomplex()
    # test_complex_and_trig()
    test_numericalmethods()