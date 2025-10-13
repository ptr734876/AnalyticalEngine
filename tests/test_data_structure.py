import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data_structures.SQtable import sqtable

def test_sq():
    a = sqtable('first', 'first_table')
    a.sqaddcolumn('EMMO')


if __name__ == '__main__':
    test_sq()