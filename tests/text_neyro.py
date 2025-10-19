import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from algorithms.neyro import BaseNeyro
import numpy as np


def test2():
    np.random.seed(1)
    def create_data(n, a, b, func):

        f = np.random.uniform(a, b, size=(n, 1))
        f1 = func(f)
        return f, f1
    def func(f):
        return f * 2
    X_train, y_train = create_data(100, -100, 100, func)

    a = BaseNeyro(X_train, y_train, [5, 1], task='regression')
    
    print("Training...")
    for i in range(10010):
        c, error = a.backward(lmd=0.001)
        if i % 1000 == 0:
            print(f"Iteration {i}, Error: {error:.6f}")
    
    test_input = np.array([[1.5], [3.5], [5.5]])
    
    predictions = a.predict(test_input, act_layers=BaseNeyro.relu, end_layer=BaseNeyro.linear)  

    print("\nPredictions:")
    for i in range(len(test_input)):
        print(f"Input: {test_input[i][0]}, Expected: {test_input[i][0]*2:.1f}, Predicted: {predictions[i][0]:.2f}")

if __name__ == '__main__':
    test2()