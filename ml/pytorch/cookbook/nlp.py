import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchtext import data, datasets


BATCH_SIZE = 64
lr         = 0.001
EPOCHS     = 40
USE_CUDA   = torch.cuda.is_available()
DEVICE     = torch.device("cuda" if USE_CUDA else "cpu")

TEXT  = data.Field(sequential=True, batch_first=True, lower=True)
LABEL = data.Field(sequential=False, batch_first=True)
