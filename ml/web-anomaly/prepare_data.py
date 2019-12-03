import os
import time
import pickle
import shutil

import numpy as np
import pandas as pd

raw_data = pd.read_csv('./groupware_data/wareattack.csv')
raw_data['url'] = raw_data['http_url'] + '?' + raw_data['http_query']
raw_data.url = raw_data.url.apply(lambda x : x[:-2] if x.endswith('-') else x)

data = raw_data[['url', 'label', 'attack']]
X = data.url.drop_duplicates().to_list()
f = lambda x : [ord(i) for i in x]
X1 = list(map(f, X))
flatten_X1 = np.array([j for i in X1 for j in i]).reshape(-1, 1)

filename = 'train_data'

if os.path.exists(filename+'.pkl'):
    replace_filename = filename + '-' + time.strftime('%y-%m-%d_%H:%M')
    shutil.copyfile(filename+'.pkl', replace_filename+'.pkl')

with open(filename+'.pkl', 'wb') as f:
    pickle.dump(flatten_X1, f)

print("Data preparation done. Load %s file in experiment script using pickle" % filename+'.pkl')