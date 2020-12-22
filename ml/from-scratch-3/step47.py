import numpy as np
from dezero import Variable, as_variable
import dezero.functions as F
from dezero.models import MLP

def softmax1d(x):
    x = as_variable(x)
    y = F.exp(x)
    sum_y = F.sum(y)
    return y / sum_y

model = MLP((10, 3))

x = np.array([[0.2, -0.4]])
y = model(x)
p = softmax1d(y)

print(y)
print(p)

