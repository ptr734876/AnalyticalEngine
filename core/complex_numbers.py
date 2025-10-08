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
        return (self.r**2 + self.im**2)**1/2
        
    def __str__(self):
        return f'{self.r}+i{self.im}' if self.im >= 0 else f'{self.r}-i{abs(self.im)}'
    
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

    class trigcomplex(complex):
        def __init__(self, pfi=0, r=0):
            self.pfi = pfi
            self.r = r

        def __str__(self):
            from math import radians
            return f'{self.r}(cos({radians(self.pfi)}+sin({radians(self.pfi)})))'
        
        def trig_to_complex(self):
            pass
        
        def __pow__(self, n):
            from math import atan, pi, radians, cos, sin
            b = self.im
            a = self.r
            if a > 0:
                pfi = radians(atan(b / a))
            elif a < 0 and b >= 0:
                pfi = radians(atan(b / a) + pi)
            elif a < 0 and b < 0:
                pfi = radians(atan(b / a) - pi)
            elif a == 0 and b > 0:
                pfi = radians(pi/2)
            elif a == 0 and b < 0:
                pfi = radians(-pi/2)
            elif a == 0 and b == 0:
                TypeError('For r = 0 and im = 0 pfi is not defined')

            a = abs(self)**n * cos(pfi*n)
            b = abs(self)**n * sin(pfi*n) 
            
            return complex(a, b)

    def complex_to_trig(self):
        from math import radians, atan, pi
        b = self.im
        a = self.r
        if a > 0:
                pfi = radians(atan(b / a))
        elif a < 0 and b >= 0:
            pfi = radians(atan(b / a) + pi)
        elif a < 0 and b < 0:
            pfi = radians(atan(b / a) - pi)
        elif a == 0 and b > 0:
            pfi = radians(pi/2)
        elif a == 0 and b < 0:
            pfi = radians(-pi/2)
        elif a == 0 and b == 0:
            TypeError('For r = 0 and im = 0 pfi is not defined')