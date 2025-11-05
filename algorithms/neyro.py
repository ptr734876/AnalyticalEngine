import numpy as np

class BaseNeyro:
    def __init__(self, inx, outy, layers_number, task='classification'):
        self.inx_mean = np.mean(inx)
        self.inx_std = np.std(inx) + 1e-8
        self.outy_mean = np.mean(outy)
        self.outy_std = np.std(outy) + 1e-8

        self.inx = (inx - self.inx_mean) / self.inx_std
        self.TrueY = (outy - self.outy_mean) / self.outy_std
        self.task = task
        if isinstance(layers_number, list):
            self.neurns = layers_number
        elif isinstance(layers_number, int):
            self.neurns = np.linspace(self.inx.shape[1],  self.TrueY.shape[1], layers_number).astype(int)
        
        lower_digits = 0.1
        self.ws = []
        self.bs = []

        if len(self.neurns) == 0:
            self.ws.append(np.random.randn(self.inx.shape[1], self.TrueY.shape[1]) * lower_digits)
            self.bs.append(np.zeros((1, self.TrueY.shape[1])))

        elif len(self.neurns) == 1:
            self.ws.append(np.random.randn(self.inx.shape[1], self.neurns[0]) * lower_digits)
            self.bs.append(np.zeros((1, self.neurns[0])))            
            self.ws.append(np.random.randn(self.neurns[0], self.TrueY.shape[1]) * lower_digits)
            self.bs.append(np.zeros((1, self.TrueY.shape[1]))) 
        else:
            self.ws.append(np.random.randn(self.inx.shape[1], self.neurns[0]) * lower_digits)   
            self.bs.append(np.zeros((1, self.neurns[0])))
            for i in range(1, len(self.neurns)):
               self.ws.append(np.random.randn(self.neurns[i-1], self.neurns[i]) * lower_digits)
               self.bs.append(np.zeros((1, self.neurns[i])))

            self.ws.append(np.random.randn(self.neurns[-1], self.TrueY.shape[1]) * lower_digits)
            self.bs.append(np.zeros((1, self.TrueY.shape[1])))

    @staticmethod
    def softmax(x):
        e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return e_x / np.sum(e_x, axis=1, keepdims=True)  

    @staticmethod
    def softmax_der(x):
        batch_size, num_classes = x.shape
        jacobian = np.zeros((batch_size, num_classes, num_classes))
        
        for i in range(batch_size):
            x_i = x[i]
            jacobian[i] = np.diagflat(x_i) - np.outer(x_i, x_i)
        
        return jacobian
    
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-np.clip(x, -250, 250))) 
    
    @staticmethod
    def sigmoid_der(x):
        sig = BaseNeyro.sigmoid(x)
        return sig*(1-sig)
    
    @staticmethod
    def tanh(x):
        return np.tanh(x)
    
    @staticmethod
    def tanh_der(x):
        return 1 - np.tanh(x)**2
    
    @staticmethod
    def relu(x):
        return np.maximum(0, x)

    @staticmethod
    def relu_der(x):    
        return (x > 0).astype(float)
    
    @staticmethod
    def linear(x): 
        return x
    
    @staticmethod
    def lin_der(x):
        return 1

    @staticmethod
    def normalization(X):
        inx_mean = np.mean(X)
        inx_std = np.std(X) + 1e-8
        inx = (X - inx_mean) / inx_std
        return inx

    @staticmethod
    def denormalization(X, orig_X):
        inx_mean = np.mean(orig_X)
        inx_std = np.std(orig_X) + 1e-8
        return X * inx_std + inx_mean

    act_methods = [softmax, sigmoid, tanh, relu, linear]
    act_der_methods = [softmax_der, sigmoid_der, tanh_der, relu_der, lin_der]

    def forward(self, act_layers=sigmoid, end_layer=softmax, input_data=None):
        self.activation = []
        if input_data is not None:
            cur = input_data
        else:
            cur = self.inx        
        self.zs = []

        self.activation.append(cur)

        for i in range(len(self.ws) - 1):
            z = cur @ self.ws[i] + self.bs[i]
            self.zs.append(z)
            cur = act_layers(z)
            self.activation.append(cur)

        z = cur @ self.ws[-1] + self.bs[-1]
        self.zs.append(z)
        cur = end_layer(z)
        self.activation.append(cur)

        return cur
    
    def predict(self, X, act_layers=relu, end_layer=linear):
        norm_X = (X - self.inx_mean) / self.inx_std
        norm_out = self.forward(act_layers=act_layers, end_layer=end_layer, input_data=norm_X)
        denorm_out = norm_out * self.outy_std + self.outy_mean
        return denorm_out
    
    def mse(y_true, y_pred):
        return np.mean((y_true - y_pred)**2)*(1/2)
    
    def mse_der(y_true, y_pred, batch_size=1):
        return (y_pred - y_true) / batch_size
    
    def backward(self, act_layers=None, end_layer=None, lmd=0.01, error_func=None, batch_size=1):
        if act_layers is None:
            act_layers = BaseNeyro.relu if self.task == 'regression' else BaseNeyro.sigmoid
        if end_layer is None:
            end_layer = BaseNeyro.linear if self.task == 'regression' else BaseNeyro.softmax
        if error_func is None:
            error_func = BaseNeyro.mse
        
        if act_layers == BaseNeyro.sigmoid:
            act_der = BaseNeyro.sigmoid_der
        elif act_layers == BaseNeyro.relu:
            act_der = BaseNeyro.relu_der
        elif act_layers == BaseNeyro.tanh:
            act_der = BaseNeyro.tanh_der
        else:
            act_der = BaseNeyro.lin_der
        
        if end_layer == BaseNeyro.softmax:
            end_der = BaseNeyro.softmax_der
        else:
            end_der = BaseNeyro.lin_der

        out = self.forward(act_layers=act_layers, end_layer=end_layer)
        
        if self.task == 'classification': # 1 | разделение по типу задачи - классификация

            if end_layer == BaseNeyro.softmax: # проверка на наличие софт макса на слое выхода (только его произваодня прописана в коде)
                delta = (out - self.TrueY) / self.TrueY.shape[0] #cross entropy loss + softamx | out grad | TrueY - one hot encoded метка / ниже то что мне дала нейронка, я не понимаю почему так
                # delta = (out - self.TrueY)
            else:
                raise ValueError(f'Not support classification with {act_layers, end_layer}') #ошибка при другом методе активации
            
        elif self.task == 'regression':# 1 | разделение по типу задачи - регрессия

            if error_func == BaseNeyro.mse: # поддерживается только mse поэтому проверяем на его наличие
                delta = BaseNeyro.mse_der(self.TrueY, out, batch_size) * end_der(self.zs[-1]) # вычисление разницы для регрессии это происзведение производной мсе на производную активации выходного слоя
            else:
                raise ValueError(f'{error_func} is not supported type error func')
            
        else:
            raise ValueError(f'{self.task} is unknown name')

        for i in range(len(self.ws)-1, -1, -1):# обратный проход по слоям, от индекса len(self.ws)-1 до нулевого
            grad_w = self.activation[i].T @ delta # проход по весам по прямой это input  @ ws а для обратного направления это транспарированная матрца активаций на дельту тоесть рахницу
            grad_b = np.sum(delta, axis=0, keepdims=True)

            self.ws[i] -= lmd * grad_w # мы узнали градиент изменения и умножаем его лямбду чтобы уменьшить шаг изменения, а затем вычитаем это из весов чтобы изменить их
            self.bs[i] -= lmd * grad_b

            if i > 0:# для последнего слоя нет предыдущего слоя чтобы найти ошибку
                delta = delta @ self.ws[i].T * act_der(self.zs[i-1])# градиент по входу текущего слоя (delta @ self.ws[i].T) умножается на производную функ активации на текущем слое
        return out, (BaseNeyro.mse(self.TrueY * self.outy_std + self.outy_mean, out * self.outy_std + self.outy_mean))**(1/2)