import matplotlib.pyplot as plt
def line2d(x, y, xname='x', yname='y', label='', title=''):
    plt.plot(x, y, label)

    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.title(title)
    plt.legend()
    plt.show()