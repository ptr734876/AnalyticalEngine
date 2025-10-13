import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from visualization.d2 import plotter2d

def test_plotter():
    a = plotter2d([1, 2, 3], [1, 4, 9], "Quadratic")
    b = plotter2d([1, 2, 3], [1, 2, 3], "Linear")
    
    print(a, b) 
    print(a)
    print("Text", a, "more text")
    print("Hello world")
if __name__ == '__main__':
    test_plotter()  