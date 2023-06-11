import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import os
import cv2
import numpy as np

torch.manual_seed(1234)


class CustomDataset(Dataset):
    def __init__(self, transform=None):
        self.imgs_path = "test/images/"
        file_list = sorted(
            [x for x in os.listdir("test/images/")], key=lambda x: int(x.split(".")[0])
        )
        self.data = []
        for img_path in file_list:
            self.data.append([self.imgs_path + img_path, "a"])
        self.img_dim = (28, 28)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_path, class_name = self.data[idx]
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, self.img_dim)
        class_id = 0
        img_tensor = torch.from_numpy(img)
        img_tensor = img_tensor.resize(1, 28, 28)
        img_tensor = img_tensor.float()
        class_id = torch.tensor([class_id])
        if self.transform:
            img_tensor = self.transform(img_tensor)
        return img_tensor, class_id


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 4 * 4, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = self.pool(nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 16 * 4 * 4)
        x = nn.functional.relu(self.fc1(x))
        x = nn.functional.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# Prendre une clef aléatoire -> bien penser à la sauvegarder !
X = torch.randn(144, 150).numpy()
# Créer un modèle
model = Net()
weight_matrix = torch.load("404_model.pth", weights_only=True)
model.load_state_dict(weight_matrix)

for layer in model.children():
    if isinstance(layer, nn.Conv2d):
        weight_matrix: np = layer.weight.detach().numpy()
        # flatten the weight matrix
        weight_matrix: np = weight_matrix.mean(axis=0)
        weight_matrix = weight_matrix.flatten()
        if weight_matrix.shape[0] != 150:
            continue
        for i in range(144):
            X[i] = np.multiply(X[i], weight_matrix)

        X = X.sum(axis=1)
X[X >= 0] = 1
X[X < 0] = 0
sol = ""
j = 0
for i in X:
    print(int(i), end="")
    sol += str(int(i))
    j += 1
    if j % 8 == 0:
        sol += " "
print()
ascii_string = ""
binary_values = sol.split()
for binary_value in binary_values:
    an_integer = int(binary_value, 2)
    ascii_character = chr(an_integer)
    ascii_string += ascii_character
print(ascii_string)
