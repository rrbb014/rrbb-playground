import torch
import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import torch.nn.functional as F

n_dim = 2
x_train, y_train = make_blobs(
    n_samples=80,
    n_features=n_dim,
    centers = [[1,1], [-1,-1], [1, -1], [-1,1]],
    shuffle=True,
    cluster_std=0.3
)

x_test, y_test = make_blobs(
    n_samples=20,
    n_features=n_dim,
    centers=[[1,1], [-1,-1], [1,-1], [-1,1]],
    shuffle=True,
    cluster_std=0.3
)

