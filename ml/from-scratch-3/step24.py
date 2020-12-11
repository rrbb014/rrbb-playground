if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__)))

import numpy as np
from dezero import Variable

def sphere(x, y):
    z = x ** 2 + y ** 2
    return z

def matyas(x, y):
    z = 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y
    return z

def goldenstein(x, y):
    z = (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) * \
        (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))
    return z

x = Variable(np.array(1.0))
y = Variable(np.array(1.0))
z = sphere(x, y)
z.backward()

print("sphere function(z=x^2+y^2) differentiation: ", x.grad, y.grad)

x.clear_grad()
y.clear_grad()
z = matyas(x, y)
z.backward()

print("matyas function(z=0.26(x^2+y^2)-0.48xy) differentiation: ", x.grad, y.grad)

x.clear_grad()
y.clear_grad()
z = goldenstein(x, y)
z.backward()

print("goldenstein function differentiation: ", x.grad, y.grad)
