import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from visualization.d2 import plotter2d
from math import tan, sin, radians, sqrt
import numpy as np
def test_plotter():
    # a = plotter2d([1, 2, 3], [1, 4, 9], "Quadratic")
    # b = plotter2d([1, 2, 3], [1, 2, 3], "Linear")
    # c = plotter2d(['adf', 'asfd'], ['dasd', 'dasjda'], 'dasd')
    # print(c)
    a = plotter2d([i for i in np.linspace(1,100, 100)], [tan(i) * sin(i)*sqrt(abs(i)) for i in np.linspace(1, 100, 100)], '')
    a.show()
    # print("Text", a, "more text")
    # print("Hello world")
if __name__ == '__main__':
    test_plotter()  