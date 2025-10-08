import matplotlib.pyplot as plt
def line2d(x, y, xname='x', yname='y', label=''):
    plt.plot(x, y, label)

    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.legend()
    plt.show()