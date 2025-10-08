import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from core.complex_numbers import complex

def test_complex():
    a = complex(1, 1)
    b = complex(1, 3)
    c = complex(1, 2)
    print(a > b)
    print(a < b)
    print(a != b)
    print(a+b)
    print(a*b)
    print(a/b)
    print(a == c)
    print(a**10)

if __name__ == '__main__':
    test_complex()