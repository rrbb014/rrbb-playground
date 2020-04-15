from mxnet import nd, gpu, gluon, autograd
from mxnet.gluon import nn
from mxnet.gluon.data.vision import datasets, transforms
import time

net = nn.Sequential()
net.add(
    nn.Conv2D(channels=6, kernel_size=5, activation='relu'),
    nn.MaxPool2D(pool_size=2, strides=2),
    nn.Conv2D(channels=16, kernel_size=3, activation='relu'),
    nn.MaxPool2D(pool_size=2, strides=2),
    nn.Flatten(),
    nn.Dense(120, activation="relu"),
    nn.Dense(84, activation="relu"),
    nn.Dense(10))

net.load_parameters('net.params', ctx=gpu())

x = nd.random.uniform(shape=(1, 1, 28, 28), ctx=gpu())
net(x)

batch_size = 256
transformer = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(0.13, 0.31)])

train_data = gluon.data.DataLoader(
    datasets.FashionMNIST(train=True).transform_first(transformer),
        batch_size, shuffle=True, num_workers=4)

valid_data = gluon.data.DataLoader(
    datasets.FashionMNIST(train=False).transform_first(transformer),
        batch_size, shuffle=False, num_workers=4)

devices = [gpu()]
net.collect_params().initialize(force_reinit=True, ctx=devices)

softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss()
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.1})

for epoch in range(10):
    train_loss = 0.
    tic = time.time()
    for data, label in train_data:
        data_list = gluon.utils.split_and_load(data, devices)
        label_list = gluon.utils.split_and_load(label,devices)
        with autograd.record():
            losses = [softmax_cross_entropy(net(X), y)
                    for X, y in zip(data_list, label_list)]

        for l in losses:
            l.backward()

        trainer.step(batch_size)

        train_loss += sum([l.sum().asscalar() for l in losses])

    print("Epoch %d: loss %.3f, in %.1f sec" %
            ( epoch, train_loss/len(train_data)/batch_size, time.time()-tic))
