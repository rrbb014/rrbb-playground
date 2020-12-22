import numpy as np
import dezero
from dezero import Variable

if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

x = Variable(np.random.randn(2, 3))
y = x.transpose()
y = x.T
