import numpy as np
from dezero import Variable
import dezero.functions as F
import dezero.layers as L

# dataset
np.random.seed(0)
x = np.random.rand(100, 1)
y = np.sin(2 * np.pi * x) + np.random.rand(100, 1)

l1 = L.Linear(10) # output size
l2 = L.Linear(1)

def predict(x):
    y = l1(x)
    y = F.sigmoid_simple(y)
    y = l2(y)
    return y

lr = 0.2
iters = 10000

for i in range(iters):
    y_pred = predict(x)
    loss = F.mean_squared_error(y, y_pred)
    l1.clear_grads()
    l2.clear_grads()
    loss.backward()

    for l in [l1, l2]:
        for p in l.params():
            p.data -= lr * p.grad.data

    if i % 1000 == 0:
        print(loss)

import matplotlib.pyplot as plt

sorted_x = x.copy()
sorted_x.sort(axis=0)
preds = predict(sorted_x)

sorted_x = sorted_x.squeeze()
preds = preds.data.squeeze()
plt.scatter(x, y)
plt.plot(sorted_x, preds, color='red')
plt.show()
