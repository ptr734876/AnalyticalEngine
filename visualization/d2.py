import matplotlib.pyplot as plt
import builtins

class plotter2d:
    origpr = builtins.print
    
    def __init__(self, x_val: list[int | float], y_val: list[int | float], label: str):
        self.x_val = x_val
        self.y_val = y_val
        self.label = label
        self.size = (8, 6)

    def __repr__(self) -> str:
        plt.legend()
        plt.show()
        return f'Graphic "{self.label}" was created'

    def resize(self, size: tuple) -> None:
        self.size = size
        return None
        
    @staticmethod
    def compareplots(listofplotters: list, title: str=''):
        plt.figure(figsize=(8, 6))
        for a in listofplotters:
            plt.plot(a.x_val, a.y_val, label=a.label)
        plt.title(title)
        plt.legend()
        plt.show()
        return f'Graphics are ready'
    
    def show(self):
        plt.figure(figsize=self.size)
        plt.plot(self.x_val, self.y_val, label=self.label)
        plt.legend()
        plt.title(self.label)
        plt.show()

def mempr(*args, **kwargs):
    plots = [arg for arg in args if isinstance(arg, plotter2d)]
    other = [arg for arg in args if not isinstance(arg, plotter2d)]
    
    if len(plots) > 1:
        plotter2d.compareplots(plots)
        if other:
            plotter2d.origpr(*other, **kwargs)
    elif len(plots) == 1:
        result = plotter2d.origpr(plots[0])  
        if other:
            plotter2d.origpr(*other, **kwargs)  
        return result
    else:
        plotter2d.origpr(*args, **kwargs) 

builtins.print = mempr