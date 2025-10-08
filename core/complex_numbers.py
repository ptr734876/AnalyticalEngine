from algorithms.digits import pinum
class complex:
    def __init__(self, r=0, im=0):
        self.r = r
        self.im = im
    
    def __add__(self,other):
        return complex(self.r + other.r, self.im + other.im)
    
    def __sub__(self, other):
        return complex(self.r - other.r, self.im - other.im)
    
    def __eq__(self, other):
        return self.r == other.r and self.im == other.im
    
    def __lt__(self, other):
        return TypeError("Complex numbers cannot be compared")
    
    def __abs__(self):
        return (self.r**2 + self.im**2)**(1/2)
        
    def __str__(self):
        return f'{self.r:.3g} + i{self.im:.3g}' if self.im >= 0 else f'{self.r:.3g} - i{abs(self.im):.3g}'
    
    def __mul__(self, other):
        return complex(self.r * other.r - self.im * other.im, self.r * other.im + self.im * other.r)
    
    def __truediv__(self, other):
        return complex((self.r * other.r + self.im * other.im)/(other.r ** 2 + other.im ** 2), (self.im * other.r - self.r * other.im)/(other.r ** 2 + other.im ** 2)) if other.r**2 + other.im**2 != 0 else TypeError('Complex_TrueDiv: Division by Zero')
    
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
        from math import atan, pi
        a = self.r
        b = self.im
        r = abs(self)
        if a > 0:
                pfi = atan(b / a)
        elif a < 0 and b >= 0:
            pfi = atan(b / a) + pi
        elif a < 0 and b < 0:
            pfi = atan(b / a) - pi
        elif a == 0 and b > 0:
            pfi = pi/2
        elif a == 0 and b < 0:
            pfi = -pi/2
        elif a == 0 and b == 0:
            return TypeError('For r = 0 and im = 0 pfi is not defined')
        return trigcomplex(pfi, r)
    
class trigcomplex:
    def __init__(self, pfi=0, r=0):
        self.pfi = pfi
        self.r = r

    def __str__(self):
        return f'{self.r:.3g}*( cos({pinum(self.pfi)}) + sin({pinum(self.pfi)}) )'
    
    def trig_to_complex(self):
        from math import cos, sin, radians
        return complex(self.r * cos(radians(self.pfi)), self.r * sin(radians(self.pfi)))
    
    def __mul__(self, other):
        return trigcomplex(self.r * other.r, self.pfi + other.pfi)
    
    def __truediv__(self, other):
        return trigcomplex(self.r / other.r, self.pfi - other.pfi)
    
    def __pow__(self, n):
        return trigcomplex(self.pfi * n, self.r * n)
    
    def __add__(self, other):
        return (self.trig_to_complex() + other.trig_to_complex()).complex_to_trig()
    
    def __sub__(self, other):
        return (self.trig_to_complex() - other.trig_to_complex()).complex_to_trig()
    