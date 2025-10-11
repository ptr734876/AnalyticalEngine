import matplotlib.pyplot as plt

class plotter2d:
    def __init__(self, figsize: tuple = (6, 8)):
        self.fig, self.ax = plt.subplots(figsize=figsize)

    def show(self):
        plt.figure(self.fig.number)
        # Блокируем выполнение до закрытия этой фигуры
        self.fig.show()
        # Ждем пока фигура существует
        while plt.fignum_exists(self.fig.number):
            plt.pause(0.1)