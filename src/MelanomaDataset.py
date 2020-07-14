import pandas as pd
import numpy as np
import torch
from PIL import Image

from torch.utils.data import Dataset

class MelanomaDataset(Dataset):
    
    def __init__(self, train_or_test, tfms):
        if train_or_test == 'train':
            self.df = pd.read_csv('data/train.csv')
        elif train_or_test == 'test':
            self.df = pd.read_csv('data/test.csv')
        
        self.train_or_test = train_or_test
        self.tfms = tfms
        
    
    def __len__(self):
        return len(self.df)
        
    def __getitem__(self, idx):
        img_fn = self.df.iloc[idx]['image_name']
        img = Image.open(f'data/jpeg/{self.train_or_test}/{img_fn}.jpg')
        if self.tfms:  # transformation
            img = self.tfms(img)
        if self.train_or_test=='train':
            target = np.array([self.df.iloc[idx]['target']])
            target = torch.tensor(target, dtype=torch.float32)
            return {'image':img, 'class' : target}

        elif self.train_or_test=='test':
            return {'image':img}