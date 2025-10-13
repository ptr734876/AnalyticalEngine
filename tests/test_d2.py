import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from visualization.d2 import plotter2d

def test_plotter():
    a = plotter2d([1,2,3,4,5,6,7], [1,2,3,4,5,6,7], 'first')
    b = plotter2d([9,4,1,2,3,5,8], [0,1,5,2,8,4,5], 'second')
    # plotter2d.compareplots([a,b])
    

if __name__ == '__main__':
    test_plotter()