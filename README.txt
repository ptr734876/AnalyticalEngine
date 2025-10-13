# AnalyticalEngine

AnalyticalEngine is a Python library for mathematical computations, inspired by Charles Babbage's Analytical Engine. It provides tools for numerical analysis, complex arithmetic, data structure management, and data visualization.

## Features

### Core Module
- **Complex Numbers**: Custom implementation of complex numbers in rectangular (real + imaginary) and polar (magnitude + angle) forms.
  - Supports arithmetic operations: addition, subtraction, multiplication, division, exponentiation.
  - Conversions between rectangular and polar representations.
  - Operations with integers and floats.
  - Magnitude (absolute value) calculation and equality checks.

### Algorithms Module
- **Numerical Methods**: Classes for solving ordinary differential equations (ODEs).
  - Euler method
  - 4th-order Runge-Kutta method
  - Analytical solution plotting
  - SciPy-based integration for advanced solving
- **Digits**: Utility for representing π in degree-based fractions.

### Data Structures Module
- **SQtable**: A class for managing SQLite tables.
  - Create tables with auto-incrementing ID.
  - Insert data with parameterized queries.
  - Add columns dynamically.
  - Delete tables and associated files.
  - Basic setup for data storage and retrieval (with notes on future improvements like SELECT methods, error handling, and integration with numpy/pandas).

### Visualization Module
- **2D Plotting**: Simple matplotlib-based class for 2D graphs with interactive display.
  - Plot single or multiple graphs.
  - Customizable figure sizes and labels.

### Tests
- Comprehensive test suite for all modules, including ODE solving examples with visualizations, complex number operations, and data structure management.

## Installation

1. Ensure Python 3.x is installed.
2. Install dependencies: `pip install matplotlib numpy scipy`
3. Clone or download the repository.
4. Add the project root to your Python path or install as a package.

## Usage

### Complex Numbers
```python
from core.complex_numbers import complex, trigcomplex

# Rectangular form
a = complex(1, 2)  # 1 + 2i
b = complex(3, 4)  # 3 + 4i
print(a + b)  # Addition
print(a * b)  # Multiplication

# Polar form
c = trigcomplex(5, 45)  # Magnitude 5, angle 45 degrees
print(c.trig_to_complex())  # Convert to rectangular

# Conversions
print(a.complex_to_trig())  # To polar
```

### Numerical Methods
```python
from algorithms.NumericalMethods import NumericalMethods

def f(x, y):
    return y - x**2  # Example ODE: dy/dx = y - x^2

x_vals, y_vals = NumericalMethods.euler_method(f, 0, 1, 2, step=0.1)
print(x_vals, y_vals)
```

### Data Structures
```python
from data_structures.SQtable import sqtable

# Create a table
table = sqtable('example_table', 'example_db')
table.sqaddcolumn('name', 'TEXT')
table.sqaddcolumn('value', 'REAL')

# Insert data
data = [('Alice', 10.5), ('Bob', 20.0)]
table.sqinsert(['name', 'value'], data)
```

### Visualization
```python
from visualization.d2 import plotter2d
import matplotlib.pyplot as plt

plotter = plotter2d([1, 2, 3], [1, 4, 9], "Quadratic")
plotter.show()
```

## Mathematical Examples

### Complex Number Arithmetic
Complex numbers follow the rules of algebra with i² = -1.

- **Addition**: (a + bi) + (c + di) = (a + c) + (b + d)i
  - Example: (1 + 2i) + (3 + 4i) = 4 + 6i

- **Multiplication**: (a + bi)(c + di) = ac + adi + bci + bdi² = (ac - bd) + (ad + bc)i
  - Example: (1 + 2i)(3 + 4i) = (1*3 - 2*4) + (1*4 + 2*3)i = -5 + 10i

- **Polar Form**: z = r e^(iθ), where r = |z|, θ = arg(z)
  - Multiplication: z1 * z2 = r1 r2 e^(i(θ1 + θ2))
  - Example: trigcomplex(2, 60) * trigcomplex(3, 30) = trigcomplex(6, 90)

### Numerical Methods for ODEs
ODEs like dy/dx = f(x, y) are solved numerically.

- **Euler Method**: y_{n+1} = y_n + h f(x_n, y_n), where h is step size.
  - Simple but less accurate for large h.

- **Runge-Kutta 4th Order**: More accurate approximation using weighted averages of slopes.
  - k1 = f(x_n, y_n)
  - k2 = f(x_n + h/2, y_n + h k1/2)
  - k3 = f(x_n + h/2, y_n + h k2/2)
  - k4 = f(x_n + h, y_n + h k3)
  - y_{n+1} = y_n + (h/6)(k1 + 2k2 + 2k3 + k4)

- **Analytical vs Numerical**: Numerical methods approximate solutions; analytical provides exact if possible.
  - Example in examples/NumericExample.py: Solving dy/dx = (y-2)/cos(x) using Euler, RK4, and analytical.

## Running Tests

Run the test files in the `tests/` directory:
- `python tests/test.py` for general tests (complex numbers, numerical methods, visualization).
- `python tests/test_data_structure.py` for data structure tests.
- `python tests/test_d2.py` for visualization tests.

## Project Structure

- `core/`: Core mathematical classes (complex numbers, constants).
- `algorithms/`: Numerical algorithms and utilities (ODE solvers, digits).
- `data_structures/`: Data structure implementations (SQLite table manager).
- `datasets/`: Sample databases (e.g., first_table.db).
- `visualization/`: Visualization tools (2D plotting).
- `tests/`: Test suites for all modules.
- `examples/`: Example scripts (e.g., NumericExample.py for ODE solving).
- `LICENSE`: MIT license.

## Contributing

Feel free to contribute by adding features, fixing bugs, or improving documentation. Ensure tests pass before submitting.

## License

MIT License - see LICENSE file for details.

## Contact

For questions or suggestions, contact the author: ptr734876.
