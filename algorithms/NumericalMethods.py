class NumericalMethods:

    @staticmethod
    def analytical(f, x0, y0, xn, step=0.1):

        x = x0
        y = y0

        x_values = [x0]
        y_values = [y0]

        while x < xn:
            y = f(x)
            x = x + step

            x_values.append(x)
            y_values.append(y)

        return x_values, y_values

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
    def runge_kut_4(f, x0, y0, xn, step=0.1):
        x = x0
        y = y0
        x_values = [x0]
        y_values = [y0]

        while x < xn:
            k1 = f(x, y)
            k2 = f(x + step/2, y + step*k1/2)
            k3 = f(x + step/2, y + step*k2/2)
            k4 = f(x + step, y + step*k3)

            y = y + (step/6)*(k1 + 2*k2 + 2*k3 + k4)
            x = x + step
            x_values.append(x)
            y_values.append(y)

        return x_values, y_values
    

    @staticmethod
    def sci_method(f, x0, y0, xn, step=0.1):
        from scipy.integrate import solve_ivp
        import numpy as np


        t_eval = np.arange(x0, xn + step, step)
        t_eval = t_eval[t_eval <= xn]

        solution = solve_ivp(f,
                           [x0, xn],
                           [y0],
                           t_eval=t_eval,
                           method='LSODA',
                           max_step=step)

        x_values = solution.t.tolist()
        y_values = solution.y[0].tolist()

        return x_values, y_values
