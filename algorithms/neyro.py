import numpy as np

class BaseNeyro:
    def __init__(self, inx, outy, layers_number, task='classification'):
        np.random.seed(42)  # Set seed for reproducible results
        self.inx = (inx - np.mean(inx, axis=0)) / np.std(inx, axis=0)
        self.TrueY = (outy - np.mean(outy, axis=0)) / np.std(outy, axis=0)
        self.task = task
        if isinstance(layers_number, list):
            self.neurns = layers_number
        elif isinstance(layers_number, int):
            self.neurns = np.linspace(self.inx.shape[1],  self.TrueY.shape[1], layers_number).astype(int)

        lower_digits = 0.1
        self.ws = []
        self.ws.append(np.random.randn(self.inx.shape[1], self.neurns[0]) * np.sqrt(1 / self.inx.shape[1]))
        
        if len(self.neurns) == 0:
            self.ws.append(np.random.randn(self.inx.shape[1], self.TrueY.shape[1]) * np.sqrt(1 / self.inx.shape[1]))

        elif len(self.neurns) == 1:
            self.ws.append(np.random.randn(self.neurns[0], self.TrueY.shape[1]) * np.sqrt(1 / self.neurns[0]))

        else:        
            for i in range(1, len(self.neurns)):
               self.ws.append(np.random.randn(self.neurns[i-1], self.neurns[i]) * np.sqrt(1 / self.neurns[i-1]))
            self.ws.append(np.random.randn(self.neurns[-1], self.TrueY.shape[1]) * np.sqrt(1 / self.neurns[-1]))
    
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

    act_methods = [softmax, sigmoid, tanh, relu, linear]
    act_der_methods = [softmax_der, sigmoid_der, tanh_der, relu_der, lin_der]

    def forward(self, act_layers=sigmoid, end_layer=softmax):
        
        self.activation = [self.inx]
        self.zs = []

        cur = self.inx

        for i, w in enumerate(self.ws):
            z = cur @ w
            self.zs.append(z)

            if i == len(self.ws) - 1:
                cur = end_layer(z)
            else:
                cur = act_layers(z)

            self.activation.append(cur)

        return cur
    
    def mse(y_true, y_pred):
        return np.mean((y_true - y_pred)**2)*(1/2)
    
    def mse_der(y_true, y_pred, batch_size=1):
        return (y_pred - y_true) / batch_size
    
    def backward(self, act_layers=None, end_layer=None, lmd=0.01, error_func=mse, batch_size=1):

        if act_layers is None:
            if self.task == 'classification':
                act_layers = BaseNeyro.sigmoid

                act_der = BaseNeyro.sigmoid_der
            elif self.task == 'regression':
                act_layers = BaseNeyro.relu
                act_der = BaseNeyro.relu_der
            else:
                raise ValueError(f'{self.task} is unknown task type')
        elif act_layers is not None:
            if act_layers in BaseNeyro.act_methods:
                act_der = BaseNeyro.act_der_methods[BaseNeyro.act_methods.index(act_layers)]
            else:
                raise ValueError(f'{act_layers} is unknown name')

        if end_layer is None:
            if self.task == 'classification':
                end_layer = BaseNeyro.softmax
                end_der = BaseNeyro.softmax_der
            elif self.task == 'regression':
                end_layer = BaseNeyro.linear
                end_der = BaseNeyro.lin_der

        out = self.forward(act_layers=act_layers, end_layer=end_layer)
        error = self.TrueY - out

        if self.task == 'classification': # 1 | разделение по типу задачи - классификация

            if end_layer == BaseNeyro.softmax: # проверка на наличие софт макса на слое выхода (только его произваодня прописана в коде)
                delta = out - self.TrueY #cross entropy loss + softamx | out grad | TrueY - one hot encoded метка
            else:
                raise ValueError(f'Not support classification with {act_layers, end_layer}') #ошибка при другом методе активации
            
        elif self.task == 'regression':# 1 | разделение по типу задачи - регрессия

            if error_func == BaseNeyro.mse: # поддерживается только mse поэтому проверяем на его наличие
                delta = BaseNeyro.mse_der(self.TrueY, out, batch_size) * end_der(self.zs[-1]) # вычисление разницы для регрессии это происзведение производной мсе на производную активации выходного слоя
            else:
                raise ValueError(f'{error_func} is not supported type error func')
            
        else:
            raise ValueError(f'{self.task} is unknown name')

        for i in range(len(self.ws)-1, -1, -1):# обратный проход по слоям, от индекса len(self.ws)-1 до -1(тоесть нулевого)
            grad_w = self.activation[i].T @ delta # проход по весам по прямой это imput  @ ws а для обратного направления это транспарированная матрца активаций на дельту тоесть рахницу 
            self.ws[i] -= lmd * grad_w # мы узнали градиент изменения и умножаем его лямбду чтобы уменьшить шаг изменения, а затем вычитаем это из весов чтобы изменить их

            if i > 0:# для последнего слоя нет предыдущего слоя чтобы найти ошибку
                delta = delta @ self.ws[i].T * act_der(self.zs[i])# градиент по входу текущего слоя (delta @ self.ws[i].T) умножается на производную функ активации на текущем слое
        
        return out, error