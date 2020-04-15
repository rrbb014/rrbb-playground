import torch
import torchvision
import torch.nn.functional as F
from torch import nn, optim
from torch.autograd import Variable
from torchvision import transforms, datasets

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

# 하이퍼 파라미터 설정
EPOCH = 10
BATCH_SIZE = 64
USE_CUDA = torch.cuda.is_available()
DEVICE = torch.device("cuda" if USE_CUDA else "cpu")
print("Using Device: ", DEVICE)

# Fashion MNIST
trainset = datasets.FashionMNIST(
        root     ='../data/',
        train    =True,
        download =True,
        transform=transforms.ToTensor())
train_loader = torch.utils.data.DataLoader(
        dataset    =trainset,
        batch_size =BATCH_SIZE,
        shuffle    =True,
        num_workers=2)


# AE
class AutoEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self._initialize()

    def _initialize(self):
        self.encoder = nn.Sequential(
                nn.Linear(28*28, 128),
                nn.ReLU(),
                nn.Linear(128, 64),
                nn.ReLU(),
                nn.Linear(64, 12),
                nn.ReLU(),
                nn.Linear(12, 3),  # 입력feature를 3차원으로 압축
        )
        self.decoder = nn.Sequential(
                nn.Linear(3, 12),
                nn.ReLU(),
                nn.Linear(12, 64),
                nn.ReLU(),
                nn.Linear(64, 128),
                nn.ReLU(),
                nn.Linear(128, 28*28),
                nn.Sigmoid(),       # 픽셀 당 0과 1사이로 값을 출력
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded


if __name__ == "__main__":
    
    model = AutoEncoder().to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.005)
    criterion = nn.MSELoss()

    # 원본 이미지 시각화(1st col)
    view_data = trainset.data[:5].view(-1, 28*28)
    view_data = view_data.type(torch.FloatTensor) / 255.

    def train(model, train_loader):
        model.train()
        for step, (x, label) in enumerate(train_loader):
            x = x.view(-1, 28*28).to(DEVICE)
            y = x.view(-1, 28*28).to(DEVICE)
            label = label.to(DEVICE)

            encoded, decoded = model(x)

            loss = criterion(decoded, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    for epoch in range(1, EPOCH+1):
        train(model, train_loader)

        # 디코더 에서 나온 이미지 시각화( 2nd col)
        test_x = view_data.to(DEVICE)
        _, decoded_data = model(test_x)

        # 원본과 디코딩 결과 비교
        f, a = plt.subplots(2, 5, figsize=(5, 2))
        print("[Epoch {}] ".format(epoch))
        for i in range(5):
            img = np.reshape(view_data.data.numpy()[i], (28, 28))
            a[0][i].imshow(img, cmap='gray')
            a[0][i].set_xticks(()); a[0][i].set_yticks(())


        for i in range(5):
            img = np.reshape(decoded_data.to('cpu').data.numpy()[i], (28, 28))
            a[1][i].imshow(img, cmap='gray')
            a[1][i].set_xticks(()); a[1][i].set_yticks(())

        plt.show()
