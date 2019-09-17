import numpy as np

X = np.array([0, 0])
W = np.array([1, -1])


def activation(X, W):
    S = sum(X*W)
    return 0 if S == 0 else 1


class Neuron:
    """Simple neoron for XOR"""
    def __init__(self, X, W, act_func):
        self.X = X
        self.W = W
        self.act_func = act_func

    def activate(self):
        return self.act_func(self.X, self.W)


class ConcNeuron:
    def __init__(self, x_1, x_2):
        self.x_1 = x_1
        self.x_2 = x_2

    def compare(self):
        return self.x_1 == self.x_2


if __name__ == '__main__':
    neuron_1 = Neuron(X, W, activation)
    neuron_2 = Neuron(X, W, activation)
    neuron_3 = ConcNeuron(neuron_1.activate(), neuron_2.activate())
    print(neuron_3.compare())
