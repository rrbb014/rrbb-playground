import numpy as np
from dezero import Variable
from dezero import optimizers
import dezero.functions as F
from dezero.models import MLP

# dataset
np.random.seed(0)
x = np.random.rand(100, 1)
y = np.sin(2 * np.pi * x) + np.random.rand(100, 1)

# Hyperparameters
lr = 0.2
max_iter = 10000
hidden_size = 10

model = MLP((hidden_size, 1))
#optimizer = optimizers.SGD(lr)
optimizer = optimizers.MomentumSGD(lr)
optimizer.setup(model)

# training
for i in range(max_iter):
    y_pred = model(x)
    loss = F.mean_squared_error(y, y_pred)

    model.clear_grads()
    loss.backward()
    optimizer.update()
    
    if i % 1000 == 0:
        print(loss)

import matplotlib.pyplot as plt

sorted_x = x.copy()
sorted_x.sort(axis=0)
preds = model(sorted_x)

sorted_x = sorted_x.flatten()
preds = preds.data.flatten()

plt.scatter(x, y)
plt.plot(sorted_x, preds, c='r')
plt.show()
