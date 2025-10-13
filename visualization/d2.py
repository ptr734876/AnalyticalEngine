import matplotlib.pyplot as plt

class plotter2d:

    def __init__(self,x_val, y_val, label):
        self.x_val = x_val
        self.y_val = y_val
        self.label = label
    
    def __repr__(self):
        plt.plot(self.x_val, self.y_val, label=self.label)
        plt.legend()
        plt.show()

    @staticmethod
    def compareplots(listofplotters):
        for a in listofplotters:
            plt.plot(a.x_val, a.y_val, label=a.label)
        
        plt.legend()
        plt.show()
        return f'Graphics are ready'