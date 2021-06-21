import torch
import torch.nn as nn
from torch.nn import functional as F

input_size = 4
output_size = 3
hidden_size = 30

class IrisNet(nn.Module):
    def __init__(self):
        super(IrisNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)

    def forward(self, X):
        X = torch.sigmoid((self.fc1(X)))
        X = torch.sigmoid(self.fc2(X))
        X = self.fc3(X)

        return F.log_softmax(X, dim=-1)