class NumericalMethods:

    @staticmethod
    def euler_method(f, x0, y0, xn, step=0.1):

        x_values = [x0]
        y_values = [y0]

        x = x0
        y = y0

        while x < xn:
            
            y = y + step * f(x, y)
            x = x + step

            x_values.append(x)
            y_values.append(y)

        return x_values, y_values

    
    @staticmethod
    def runge_kut_4():
        pass