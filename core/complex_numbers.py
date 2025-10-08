from algorithms.digits import pinum
class complex:
    def __init__(self, r=0, im=0):
        self.r = r
        self.im = im
    
    def __add__(self,other):
        if isinstance(other, complex):
            return complex(self.r + other.r, self.im + other.im)
        elif isinstance(other, trigcomplex):
            other = other.trig_to_complex()
            return complex(self.r + other.r, self.im + other.im)
        return TypeError(f'Cant add {type(other)} to {type(self)}')
    
    def __sub__(self, other):
        if isinstance(other, complex):
            return complex(self.r - other.r, self.im - other.im)
        elif isinstance(other, trigcomplex):
            other = other.trig_to_complex()
            return complex(self.r - other.r, self.im - other.im)
        return TypeError(f'Cant sub {type(other)} from {type(self)}')
    
    def __eq__(self, other):
        if isinstance(other, complex):
            return self.r == other.r and self.im == other.im
        elif isinstance(other, trigcomplex):
            other = other.trig_to_complex()
            return self.r == other.r and self.im == other.im
        return TypeError(f'Cant compare {type(other)} with {type(self)}')
    
    def __lt__(self):
        return TypeError("Complex numbers cannot be compared")
    
    def __abs__(self):
        return (self.r**2 + self.im**2)**(1/2)
        
    def __str__(self):
        return f'{self.r:.3g} + i{self.im:.3g}' if self.im >= 0 else f'{self.r:.3g} - i{abs(self.im):.3g}'
    
    def __mul__(self, other):
        if isinstance(other, complex):
            return complex(self.r * other.r - self.im * other.im, self.r * other.im + self.im * other.r)
        elif isinstance(other, trigcomplex):
            other = other.trig_to_complex()
            return complex(self.r * other.r - self.im * other.im, self.r * other.im + self.im * other.r)
        return TypeError(f'Cant multy {type(self)} on {type(other)}')
    
    def __truediv__(self, other):
        if isinstance(other, complex):
            return complex((self.r * other.r + self.im * other.im)/(other.r ** 2 + other.im ** 2), (self.im * other.r - self.r * other.im)/(other.r ** 2 + other.im ** 2)) if other.r**2 + other.im**2 != 0 else TypeError('Complex_TrueDiv: Division by Zero')
        elif isinstance(other, trigcomplex):
            other = other.trig_to_complex()
            return complex((self.r * other.r + self.im * other.im)/(other.r ** 2 + other.im ** 2), (self.im * other.r - self.r * other.im)/(other.r ** 2 + other.im ** 2)) if other.r**2 + other.im**2 != 0 else TypeError('Complex_TrueDiv: Division by Zero')
        return TypeError(f'Cant div {type(self)} on {type(other)}')
    
    def __pow__(self, n):
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

    def complex_to_trig(self):
        from math import atan2, degrees
        r = abs(self)
        pfi_rad = atan2(self.im, self.r) 
        pfi_deg = degrees(pfi_rad)
        return trigcomplex(r, pfi_deg)
    
class trigcomplex:
    def __init__(self, r=0, pfi=0):
        self.pfi = pfi
        self.r = r

    def __str__(self):
        return f'{self.r:.3g}*( cos({pinum(self.pfi)}) + sin({pinum(self.pfi)}) )'
    
    def trig_to_complex(self):
        from math import cos, sin, radians
        return complex(self.r * cos(radians(self.pfi)), self.r * sin(radians(self.pfi)))
    
    def __mul__(self, other):
        if isinstance(other, trigcomplex):
            return trigcomplex(self.r * other.r, self.pfi + other.pfi)
        elif isinstance(other, complex):
            other = other.complex_to_trig()
            return trigcomplex(self.r * other.r, self.pfi + other.pfi)
        return TypeError(f'Cant add {type(other)} to {type(self)}')
    
    def __truediv__(self, other):
        if isinstance(other, trigcomplex):
            return trigcomplex(self.r / other.r, self.pfi - other.pfi)
        elif isinstance(other, complex):
            other = other.complex_to_trig()
            return trigcomplex(self.r / other.r, self.pfi - other.pfi)
        return TypeError(f'Cant add {type(other)} to {type(self)}')
    
    def __pow__(self, n):
        return trigcomplex(self.r ** n, self.pfi * n)
    
    def __add__(self, other):
        if isinstance(other, trigcomplex):
            return (self.trig_to_complex() + other.trig_to_complex()).complex_to_trig()
        elif isinstance(other, complex):
            return (self.trig_to_complex() + other).complex_to_trig()
        return TypeError(f'Cant add {type(other)} to {type(self)}')
    
    def __sub__(self, other):
        if isinstance(other, trigcomplex):
            return (self.trig_to_complex() - other.trig_to_complex()).complex_to_trig()
        elif isinstance(other, complex):
            return (self.trig_to_complex() - other).complex_to_trig()
        return TypeError(f'Cant add {type(other)} to {type(self)}')
