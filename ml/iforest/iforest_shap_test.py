from sklearn.ensemble.iforest import IsolationForest
from sklearn.datasets import make_classification

X, y = make_classification(
        n_samples=1000,
        n_features=5,
        n_informative=3,
)

model = IsolationForest(behaviour='new')

model.fit(X)

