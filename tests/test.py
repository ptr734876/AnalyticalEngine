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
    # print('a > b -> ', a > b)
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

def test_2d():
    a = plotter2d()
    b = plotter2d(figsize=(1, 2))
    a.show()
    b.show()

    
if __name__ == "__main__":
    import math
    # test_complex()
    # test_trigcomplex()
    # test_complex_and_trig()
    # test_2d() #broken
    print(math.log(math.exp(1)**(2* math.sin(math.pi/2))))