import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from algorithms.neyro import BaseNeyro
import numpy as np
from visualization.d2 import plotter2d


def test_regression():
    def create_data(a, b, n, func):
        f = np.random.uniform(a, b, size=(n, 1))
        f1 = func(f)
        return f, f1
    
    def func(f):
        return np.sin(f) * np.cos(f)

    X_train, y_train = create_data(0, 5, 1000, func)
    
    X_train_norm = BaseNeyro.normalization(X_train)
    y_train_norm = BaseNeyro.normalization(y_train)
    
    X_train_denorm = BaseNeyro.denormalization(X_train_norm, X_train)
    y_train_denorm = BaseNeyro.denormalization(y_train_norm, y_train)
    
    print("Normalization test:")
    print(f"Original X mean: {np.mean(X_train):.4f}, denormalized X mean: {np.mean(X_train_denorm):.4f}")
    print(f"Original Y mean: {np.mean(y_train):.4f}, denormalized Y mean: {np.mean(y_train_denorm):.4f}")
    
    indeces_base = np.argsort(X_train.flatten())

    a = BaseNeyro(X_train, y_train, [25, 30, 15], task='regression')

    first = plotter2d(X_train[indeces_base], y_train[indeces_base], 'base_data')
    error = 1
    print("Training...")
    iteration = 0
    while error > 0.1 and iteration < 10000:
        iteration += 1
        c, error = a.backward(lmd=0.00001)
        if iteration % 300 == 0:
            print(f"Iteration {iteration}, Error: {error:.6f}")
    
    denorm_test = np.random.uniform(0, 5, size=(1000,1))
    
    denorm_pred = a.predict(denorm_test, act_layers=BaseNeyro.relu, end_layer=BaseNeyro.linear)
    indeces_pred = np.argsort(denorm_test.flatten())

    second = plotter2d(denorm_test[indeces_pred], denorm_pred[indeces_pred], 'predict_data')
    
    plotter2d.compareplots([first, second])
    

# def test_classification():
#     np.random.seed(1)
#     def create_data(n, a, b, func):

#         f = np.random.randint(a, b, size=(n, 1))
#         f1 = func(f)
#         return f, f1

#     def func(f):
#         return (f % 2 == 0).astype(int)
    
#     X_train, y_train = create_data(1000, -10, 30, func)

#     a = BaseNeyro(X_train, y_train, [15, 10])
    
#     print("Training...")
#     for i in range(1500):
#         c, error = a.backward(lmd=0.01, act_layers=BaseNeyro.sigmoid, end_layer=BaseNeyro.sigmoid)
#         if i % 1000 == 0:
#             print(f"Iteration {i}, Error: {error:.6f}")

#     test_input = np.array([[2], [3], [5]])

#     predictions = a.predict(test_input, act_layers=BaseNeyro.sigmoid, end_layer=BaseNeyro.sigmoid)

#     print("\nPredictions:")
#     for i in range(len(test_input)):
#         print(f"Input: {test_input[i][0]}, Expected: {func(test_input[i][0]):.1f}, Predicted: {predictions[i][0]:.2f}")

if __name__ == '__main__':
    test_regression()
    # test_classification()