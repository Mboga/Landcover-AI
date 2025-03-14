#!/usr/bin/env python3

"""
A script to perform training and testing of deep-learning model using the EuroSAT dataset.

The Script is written using the PyTorch Lightning deep learning framework. A VGG-net style (Link to paper that introduced the VGG architecture https://arxiv.org/pdf/1409.1556) model will be designed
and used as the model architecture. The script performs an image classification task.

I will be refactoring a script from PyTorch (vanilla) to PyTorch Lightning.


The input is the directory containing  RGB images of the EuroSAT dataset.
The sub-directories are the class names of the land cover classes.

Usage:
    To Do

Dependencies:
    To Do

Example:
    To Do

"""

#import libraries
import os
import torch
from PIL import Image
import lightning as L
import torchvision.models as models
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader, random_split
from torchvision import transforms


# DEFINE YOUR LIGHTNING MODULE

class CustomVGG(L.LightningModule):
    def __init__(self, num_classes=10,learning_rate=1e-3):
        super().__init__() # Initialise the parent class
        self.save_hyperparameters() # store hyperparameters for logging

        #1. Load pretrained VGG16 
        self.vgg16 = models.vgg16(weights='DEFAULT')

        #Modify the feature extractor: remive las maxpool layer
        self.features = nn.Sequential(*list(vgg16.features.children())[:-1])

        #2. Freeze convolutional layers/feature extrator (transfer learning standard practice)
        
        for param in self.features.parameters():
                param.requires_grad = False # disable gradient computation

    
        #Modify the classifier fof 64x64 inputs: (original VGG uses 224x224)

        self.classifier=nn.Sequential(
             nn.AdaptiveAvgPool2d((1,1)), # handle variying spatial dimensions
             nn.Flatten, # Convert 3d features to 1d
             nn.Linear(512,256), # First fully connected layer
             nn.ReLU(inplace=True), # Activation function
             nn.Dropout(0.5), # Regularization
             nn.Linear(256, num_classes) # Final classification layer

        )

        # forward pass
        def forward(self,x):
             # feature extract -> classification
             x = self.features(x)  # Pass through modified VGG16 backbone

             return self.classifier(x)  # Pass through the custom classifier
        
        #Training logic
        def training_step(self, batch, batch_idx):
             x,y=batch         # unpacj input/labels
             y_hat = self(x)   #Forward pass
             loss = nn.functional.cross_entropy(y_hat,y) # calculate the loss
             self.log('train_loss', loss)  # Log to monitoring system
             return loss

        #Validation Logic
        def validation_step(self,batch, batch_idx):
             x,y = batch
             y_hat = self(x)
             loss = nn.functional.cross_entropy(y_hat,y)
             acc = (y_hat.argmax(dim=1) == y).float().mean() # Accuracy calculation
             self.log('val_loss',loss)  # Log validation loss
             self.log('val_acc', acc)   # Log validation accuracy

        #OPTIMIZER CONFIGURATION

        def configure_optimizers(self):
             # Only optimze classifier  parameters (features remain frozen)
             return optim.Adam(self.classifier.parameters(),
                               lr = self.hparams.learning_rate)
        

# custom dataset class that inherits from PyTorch' Dataset
class EuroSATDataset(Dataset):
    '''
    This custom dataset class inherits from the PyTorch Dataset class
    '''
    def __init__(self, data_dir, transform=None):
          self.data_dir = self.transform = transform
          self.images = []
          self.labels = []
          self.class_names = os.listdir(data_dir)

          #populate images and labels lists

          for class_idx, class_name in enumerate(self.class_names):
               class_dir = os.path.join(data_dir, class_name)
               for img_name in os.listdir(class_dir):
                    self.images.append(os.path.join(class_dir, img_name))
                    self.labels.append(class_idx)
    # return the total number of images in a dataset
    def __len__(self):
         return len(self.images)
    
    def __getitem__(self, idx):
         '''
         retrieves a single item from the dataset. 
         It 
         - Loads the image from the path
         - applies any specified transformations
         -returns the image and its label
         
         '''
         img_path = self.images(idx)
         image = Image.open(img_path)
         label = self.labelslabels[idx]

         if self.transform:
              image = self.transform(image)

         return image, label
         
     
# Defines a Lighning DataModule for handling the EuroSAT dataset
class EuroSATDataModule(L.LightningDataModule):
     def __init__(self, data_dir, batch_size = 8, num_workers=4):
          super().__init__()
          self.data_dir = data_dir
          self.batch_size = batch_size
          self.num_workers = num_workers
          
          self.transform  = transforms.Compose([
               transforms.ToTensor(),
               transforms.Resize((64,64)),
               transforms.Normalize(mean=[0.485,0.456,0.406], std=[0.229, 0.224,0.225])
               ])
     # create full dataset, calculate thesplits and splits the data

     def setup(self, stage= None):
          '''
          creates the full dataset, computes the splits and splits the datasets into train,test and val
          '''
          full_dataset = EuroSATDataset(self.data_dir, transform=self.transform)
          train_size = int(0.7 * len(full_dataset))
          val_size = int(0.15 * len(full_dataset))
          test_size = len(full_dataset) - train_size - val_size

          self.train_dataset, self.val_dataset, self.test_dataset = random_split(full_dataset, [train_size, val_size, test_size])
     
     def train_dataloader(self):
          return DataLoader(self.train_dataset, batch_size = self.batch_size,shuffle = True, num_workers=self.num_workers)

     def val_dataloader(self):
          return DataLoader(self.val_dataset, batch_size = self.batch_size,shuffle = True, num_workers=self.num_workers)
     
     def test_dataloader(self):
          return DataLoader(self.test_dataset, batch_size = self.batch_size,shuffle = True, num_workers=self.num_workers)

 
# STEP 2: RUN THE TRAINER

if __name__ == "__main__":
     # data dir
     data_dir = './data/EuroSAT_RGB_250'
     # create an instance of the EuroSATDataModule
     data_module = EuroSATDataModule(data_dir)
     #Call the setup method to prepare the Data

     data_module.setup()

     #use with a Lightning Trainer
     model = CustomVGG(num_classes=10) # initialize the model

     trainer = L.Trainer(
          max_epochs = 5,   #Train for 10 passes through the datast
          accelerator = 'auto' #automatically use GPU if available
     )
     trainer.fit(model, datamodule = data_module)







