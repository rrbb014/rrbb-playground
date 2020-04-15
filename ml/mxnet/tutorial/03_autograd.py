from mxnet import nd
from mxnet import autograd

x = nd.array(
        [
            [1, 2],
            [3, 4],
        ])

x.attach_grad()

with autograd.record():
    y = 2* x * x

y.backward()

def f(a):
    b = a * 2
    while b.norm().asscalar() < 1000:
        b = b * 2
    if b.sum().asscalar() >= 0:
        c = b[0]
    else:
        c = b[1]
    return c

a = nd.random.uniform(shape=2)
a.attach_grad()
with autograd.record():
    c = f(a)
c.backward()
print([ a.grad, c/a])
