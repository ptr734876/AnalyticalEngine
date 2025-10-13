import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_structures.SQtable import sqtable
from core.complex_numbers import complex

def test_sq():
    b = []
    for i in range(10):
        for j in range(10):
            b.append(str(complex(i, j)))
    a = sqtable('first', 'first_table')
    a.sqaddcolumn('EMMO')
    a.sqinsert('EMMO', b) #broken


if __name__ == '__main__':
    test_sq()