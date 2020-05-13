# -*- coding: utf-8 -*-

import json
import numpy as np
from typing import Tuple, List

# TODO: PREPROCESSING

def read_json(filepath: str) -> dict:
    with open(filepath, encoding='utf8') as f:
        content = json.load(f)
    
    return content

def write_json(data, filepath: str):
    with open(filepath, encoding='utf8', mode='r') as f:
        json.dump(data, f)

def split_train_valid(data, ratio: float=0.8, random_seed=7014) -> Tuple[List, List]:

    print("Total length: %i" % len(data))
    print("Shuffling with seed: %i" % random_seed)
    np.random.seed(random_seed)
    np.random.shuffle(data)

    total = len(data)
    partition_idx = int(total * ratio)
    train = data[:partition]
    valid = data[partition:]

    print("Training set length: %i" % len(train))
    print("Validation set length: %i" % len(valid))

    return train, valid