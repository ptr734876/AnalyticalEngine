import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from algorithms.neyro import BaseNeyro
import numpy as np

def test2():
    f = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
    f1 = np.array([[6], [7], [8], [9], [10], [11], [12], [13], [14]])
    
    a = BaseNeyro(f, f1, [4], task='regression')
    for i in range(30001):
        c, d = a.backward(lmd=0.01)
        if i % 1000 == 0:
            print(np.mean(c), np.mean(d))
if __name__ == '__main__':
    test2()