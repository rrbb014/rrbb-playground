from mxnet import nd
from mxnet.gluon import nn

net = nn.Sequential()
net.add(
    nn.Conv2D(
        channels=6,
        kernel_size=5,
        activation='relu'),
    nn.MaxPool2D(pool_size=2, strides=2),
    nn.Conv2D(
        channels=16,
        kernel_size=3,
        activation='relu'),
    nn.MaxPool2D(pool_size=2, strides=2),
    nn.Dense(120, activation='relu'),
    nn.Dense(84, activation='relu'),
    nn.Dense(10))

net.initialize()

x = nd.random.uniform(
        shape=(4, 1, 28, 28))
y = net(x)
print(y.shape)

class MixMLP(nn.Block):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.blk = nn.Sequential()
        self.blk.add(
                nn.Dense(3, activation='relu'),
                nn.Dense(4, activation='relu'))
        self.dense= nn.Dense(5)

    def forward(self, x):
        y = nd.relu(self.blk(x))
        print(y)
        return self.dense(y)

net = MixMLP()
print(net)

net.initialize()
x = nd.random.uniform(shape=(2,2))
print(net(x))

print(net.blk[1].weight.data())
