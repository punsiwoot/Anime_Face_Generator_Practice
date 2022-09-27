import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
import torchvision.utils as vutils

torch.manual_seed(19)

class gen(nn.Module):
  def __init__(self):
    super().__init__()
    self.model =  nn.Sequential(
        nn.ConvTranspose2d(100, 1024, 4, 1, 0, bias=False),
        nn.BatchNorm2d(1024),
        nn.ConvTranspose2d(1024, 512, 4, 2, 1, bias=False),
        nn.BatchNorm2d(512),
        nn.ReLU(True),
        nn.ConvTranspose2d( 512, 256 , 4, 2, 1, bias=False),
        nn.BatchNorm2d(256),
        nn.ReLU(True),
        nn.ConvTranspose2d( 256, 128, 4, 2, 1, bias=False),
        nn.BatchNorm2d(128),
        nn.ReLU(True),
        nn.ConvTranspose2d( 128, 64, 4, 2, 1, bias=False),
        nn.BatchNorm2d(64),
        nn.ReLU(True),
        nn.ConvTranspose2d( 64, 3, 6, 4, 1, bias=False),
        nn.Tanh()
    )
  def forward(self,x):
        return self.model(x)