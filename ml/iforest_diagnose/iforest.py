import numpy as np

from sklearn.datasets import fetch_kddcup99
from sklearn.ensemble import IsolationForest


split_ratio = 0.8
random_seed = 64

kdd99 = fetch_kddcup99(data_home='.', percent10=False)
from IPython import embed;embed();exit()
data = kdd99['data']
features = kdd99['feature_names']
target = kdkdd99['target']

# Shuffle
idx = np.arange(data.shape[0])
np.random.seed(random_seed)
np.random.shuffle(idx)

split_idx = int(data.shape[0] * split_ratio)

# dataset
X_train, y_train = data[:split_idx], target[:split_idx]
X_test, y_test = data[split_idx:], target[split_idx:]

model = IsolationForest(behaviour='new')
model.fit(X_train)

from IPython import embed;embed()



