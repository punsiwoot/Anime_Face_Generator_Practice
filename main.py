import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
from generator import gen
import torchvision.utils as vutils

model = gen()
model.load_state_dict(torch.load("model.pt",map_location=torch.device('cpu')))
model.eval()
def generated_anime(num_pic=10,seed=19):
  torch.manual_seed(seed)
  sample = torch.randn(num_pic,100,1,1)
  result = model(sample)
  plt.imshow(np.transpose(vutils.make_grid(result.cpu(), padding=2, normalize=True),(1,2,0)))
  plt.show()


if __name__ == "__main__" :
    generated_anime(30,326)  #number of picture and seed