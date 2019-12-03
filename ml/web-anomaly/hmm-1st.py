import pickle

from hmmlearn.hmm import GaussianHMM

# Load data
with open('train_data.pkl', 'rb') as f:
    X = pickle.load(f)

# Initialize model
hmm_model = GaussianHMM(n_components=128, covariance_type='full')

# Fit 
hmm_model.fit(X)

# TODO: result evaluation  