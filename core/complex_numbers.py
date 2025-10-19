from algorithms.digits import pinum

class trigcomplex:
    pass

class complex:
    def __init__(self, r: int| float=0, im:int|float=0):
        self.r = r
        self.im = im

    def complex_type_check(self: int | float | complex | trigcomplex, other: int | float | complex | trigcomplex) -> tuple[complex, complex]:
        if isinstance(self, int | float):
            self = complex.num_to_complex(self)
        if isinstance(other, int | float):
            other = complex.num_to_complex(other)
        return self, other
        
    def __add__(self: complex | int | float, other: trigcomplex | complex | int | float) -> complex:
        self, other = complex.complex_type_check(self, other)
        if isinstance(other, complex):
            return complex(self.r + other.r, self.im + other.im)
        elif isinstance(other, trigcomplex):
            other = other.trig_to_complex()
            return complex(self.r + other.r, self.im + other.im)
        raise TypeError(f'Cant add {type(other)} to {type(self)}')
    
    def __sub__(self: complex | int | float, other: complex | trigcomplex | int | float) -> complex:
        self, other = complex.complex_type_check(self, other)
        if isinstance(other, complex):
            return complex(self.r - other.r, self.im - other.im)
        elif isinstance(other, trigcomplex):
            other = other.trig_to_complex()
            return complex(self.r - other.r, self.im - other.im)
        raise TypeError(f'Cant sub {type(other)} from {type(self)}')
    
    def __eq__(self: complex | int | float, other: trigcomplex | complex | int | float) -> bool:
        self, other = complex.complex_type_check(self, other)
        if isinstance(other, complex):
            return self.r == other.r and self.im == other.im
        elif isinstance(other, trigcomplex):
            other = other.trig_to_complex()
            return self.r == other.r and self.im == other.im
        raise TypeError(f'Cant compare {type(other)} with {type(self)}')
    
    def __lt__(self: complex | int | float, other: complex | trigcomplex | int | float) -> complex:
        self, other = complex.complex_type_check(self, other)
        if self.im == 0 and other.im == 0:
            return self.r > other.r
        elif self.r == 0 and other.r == 0:
            return self.im > other.im
        if isinstance(self, complex | trigcomplex) and isinstance(other, complex | trigcomplex):
            raise TypeError("Complex numbers cannot be compared")
        raise TypeError('Cant compare this types')
    
    def __abs__(self: complex) -> float:
        return (self.r**2 + self.im**2)**(1/2)
        
    def __str__(self: complex) -> str:
        return f'{self.r:.3g} + i{self.im:.3g}' if self.im >= 0 else f'{self.r:.3g} - i{abs(self.im):.3g}'
    
    def __mul__(self: complex | int | float, other: complex | trigcomplex | int | float) -> complex:
        self, other = complex.complex_type_check(self, other)
        if isinstance(other, complex):
            return complex(self.r * other.r - self.im * other.im, self.r * other.im + self.im * other.r)
        elif isinstance(other, trigcomplex):
            other = other.trig_to_complex()
            return complex(self.r * other.r - self.im * other.im, self.r * other.im + self.im * other.r)
        raise TypeError(f'Cant multy {type(self)} on {type(other)}')
    
    def __truediv__(self: complex | int | float, other: complex | trigcomplex | int | float) -> complex:
        self, other = complex.complex_type_check(self, other)
        if isinstance(other, complex):
            return complex((self.r * other.r + self.im * other.im)/(other.r ** 2 + other.im ** 2), (self.im * other.r - self.r * other.im)/(other.r ** 2 + other.im ** 2)) if other.r**2 + other.im**2 != 0 else TypeError('Complex_TrueDiv: Division by Zero')
        elif isinstance(other, trigcomplex):
            other = other.trig_to_complex()
            if other.r**2 + other.im**2 != 0:
                return complex((self.r * other.r + self.im * other.im)/(other.r ** 2 + other.im ** 2), (self.im * other.r - self.r * other.im)/(other.r ** 2 + other.im ** 2)) 
            else:
                raise TypeError('Complex_TrueDiv: Division by Zero')
        raise TypeError(f'Cant div {type(self)} on {type(other)}')
    
    def __pow__(self: complex, n: int | float) -> complex:
        if n == 0:
            return complex(1, 0)
        if n == 1:
            return self
        res = complex(1, 0)
        base = self
        while n > 0:
            if n % 2 == 1:
                res = res * base
            base = base * base
            n = n // 2
        return res        

    @staticmethod
    def num_to_complex(num: int | float) -> complex:
        return complex(num, 0)

    def complex_to_trig(self: complex | int | float) -> trigcomplex:
        from math import atan2, degrees
        r = abs(self)

        if isinstance(self, int | float):
            complex.num_to_complex(self)

        pfi = degrees(atan2(self.im, self.r)) 
        return trigcomplex(r, pfi)
    
class trigcomplex:
    def __init__(self, r:int|float=0, pfi:int|float=0):
        self.pfi = pfi
        self.r = r

    def num_to_trigcomplex(self: int | float) -> complex:
        return complex.complex_to_trig(complex.num_to_complex(self))

    def trig_complex_type_check(self: int | float | complex | trigcomplex, other: int | float | complex | trigcomplex) -> tuple[trigcomplex, trigcomplex]:
        if isinstance(self, int | float):
            self = trigcomplex.num_to_trigcomplex(self)
        if isinstance(other, int | float):
            other = trigcomplex.num_to_trigcomplex(other)
        return self, other
    
    def __str__(self: trigcomplex) -> str:
        return f'{self.r:.3g}*( cos({pinum(self.pfi)}) + sin({pinum(self.pfi)}) )'
    
    def trig_to_complex(self: trigcomplex) -> complex:
        from math import cos, sin, radians
        return complex(self.r * cos(radians(self.pfi)), self.r * sin(radians(self.pfi)))
    
    def __mul__(self: trigcomplex | int | float, other: complex | trigcomplex | int | float) -> trigcomplex:
        self, other = trigcomplex.trig_complex_type_check(self, other)
        if isinstance(other, trigcomplex):
            return trigcomplex(self.r * other.r, self.pfi + other.pfi)
        elif isinstance(other, complex):
            other = other.complex_to_trig()
            return trigcomplex(self.r * other.r, self.pfi + other.pfi)
        raise TypeError(f'Cant add {type(other)} to {type(self)}')
    
    def __abs__(self: trigcomplex) -> int | float:
        return self.r
    
    def __truediv__(self: trigcomplex | int | float, other: complex | trigcomplex | int | float) -> trigcomplex:
        self, other = trigcomplex.trig_complex_type_check(self, other)
        if isinstance(other, trigcomplex):
            return trigcomplex(self.r / other.r, self.pfi - other.pfi)
        elif isinstance(other, complex):
            other = other.complex_to_trig()
            return trigcomplex(self.r / other.r, self.pfi - other.pfi)
        raise TypeError(f'Cant add {type(other)} to {type(self)}')
    
    def __pow__(self: trigcomplex, n: int | float) -> trigcomplex:
        return trigcomplex(self.r ** n, self.pfi * n)
    
    def __add__(self: trigcomplex | int | float, other: complex | trigcomplex | int | float) -> trigcomplex:
        self, other = trigcomplex.trig_complex_type_check(self, other)
        if isinstance(other, trigcomplex):
            return (self.trig_to_complex() + other.trig_to_complex()).complex_to_trig()
        elif isinstance(other, complex):
            return (self.trig_to_complex() + other).complex_to_trig()
        raise TypeError(f'Cant add {type(other)} to {type(self)}')
    
    def __sub__(self: trigcomplex | int | float, other: complex | trigcomplex | int | float) -> trigcomplex:
        self, other = trigcomplex.trig_complex_type_check(self, other)
        if isinstance(other, trigcomplex):
            return (self.trig_to_complex() - other.trig_to_complex()).complex_to_trig()
        elif isinstance(other, complex):
            return (self.trig_to_complex() - other).complex_to_trig()
        raise TypeError(f'Cant add {type(other)} to {type(self)}')