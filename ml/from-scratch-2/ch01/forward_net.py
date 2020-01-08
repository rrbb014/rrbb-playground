import numpy as np

class Sigmoid:
    def __init__(self):
        self.params = []

    def forward(self, x):
        return 1 / (1 + np.exp(-x))


class Affine:
    def __init__(self, W, b):
        self.params = [W, b]

    def forward(self, x):
        W, b = self.params
        out = np.matmul(x, W) + b
        return out


class TwoLayerNet:
    """ 
    Model Structure 
    input -> FC -> Sigmoid -> FC -> output
    """
    def __init__(self, input_size, hidden_size, output_size, debug=False):
        I, H, O = input_size, hidden_size, output_size
        self.debug = debug

        # Initialize weights and bias
        W1 = np.random.randn(I, H)
        b1 = np.random.randn(H)

        W2 = np.random.randn(H, O)
        b2 = np.random.randn(O)

        self.layers = [
                Affine(W1, b1),
                Sigmoid(),
                Affine(W2, b2),
        ]

        # Collect all weights
        self.params = []
        for layer in self.layers:
            self.params += layer.params

    def predict(self, x):
        for layer in self.layers:
            if self.debug:
                print(""
            x = layer.forward(x)

        return x


if __name__ == "__main__":

    input_size = 2
    hidden_size = 4
    output_size = 3

    x = np.random.randn(10, 2) # 10 rows 2 cols

    model = TwoLayerNet(input_size, hidden_size, output_size)

    y = model.predict(x)
    print(y)



