#!/usr/bin/env python3

"""
© 2025, Savanna-AI and Nicholus Mboga, nicholus.mboga@savanna-ai.be
All rights reserved: Software for Teaching purposes only. For any commercial use contact nicholus.mboga@savanna-ai.be

EuroSAT Image Classification with PyTorch Lightning

This script handles both training and inference for RGB EuroSAT land cover classification
using a modified VGG16 architecture. Supports both CPU and GPU execution.

Features:
- Training mode with automatic checkpointing
- Inference mode with prediction generation
- ONNX export capability
- Progress bar control
- Mixed precision training

Usage:
    Training:   python script.py --mode train [--batch_size 8] [--precision 32]
    Inference:  python script.py --mode inference --checkpoint path/to/checkpoint.ckpt
    Export:     python script.py --mode train --export_onnx --onnx_path model.onnx

Dependencies:
    torch torchvision lightning Pillow pandas

Example:
    # Train with mixed precision
    python script.py --mode train --precision 16
    
    # Run inference
    python script.py --mode inference --checkpoint lightning_logs/version_0/checkpoints/best-checkpoint.ckpt

"""

#import libraries
import os
import sys
import torch
from PIL import Image
import lightning as L
import torchvision.models as models
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader, random_split
from torchvision import transforms
import argparse
from typing import Optional, Dict, List


# DEFINE YOUR LIGHTNING MODULE

class CustomVGG(L.LightningModule):
    """
    Modified VGG16 for 64x6 RGB EuroSAT images

    Args:
        num_classes: Number of output classes (10 for EuroSAT)
        learning_rate: Intitial learning rate
    """
    def __init__(self, num_classes=10,learning_rate=1e-3):
        super().__init__() # Initialise the parent class
        self.save_hyperparameters() # store hyperparameters for logging

        #1. Load pretrained VGG16 
        self.vgg16 = models.vgg16(weights='DEFAULT')

        #Modify the feature extractor: remive las maxpool layer
        self.features = nn.Sequential(*list(self.vgg16.features.children())[:-1])

        #2. Freeze convolutional layers/feature extrator (transfer learning standard practice)
        
        for param in self.features.parameters():
                param.requires_grad = False # disable gradient computation

    
        #Modify the classifier fof 64x64 inputs: (original VGG uses 224x224)

        self.classifier=nn.Sequential(
             nn.AdaptiveAvgPool2d((1,1)), # handle variying spatial dimensions
             nn.Flatten(), # Convert 3d features to 1d
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
            """ Training step with loss calculation and logging"""
            x,y=batch         # unpack input/labels
            y_hat = self(x)   #Forward pass
            loss = nn.functional.cross_entropy(y_hat,y) # calculate the loss
            self.log('train_loss', loss)  # Log to monitoring system
            return loss

    #Validation Logic
    def validation_step(self,batch, batch_idx):
            """Validation step with accuracy calculation"""
            x,y = batch
            y_hat = self(x)
            loss = nn.functional.cross_entropy(y_hat,y)
            acc = (y_hat.argmax(dim=1) == y).float().mean() # Accuracy calculation
            self.log('val_loss',loss)  # Log validation loss
            self.log('val_acc', acc)   # Log validation accuracy
    
    def predict_step(self,batch:tuple, batch_idx:int) -> Dict[str,torch.Tensor]:
          """
          prediction step for inference mode
          """
          x,y = batch
          y_hat = self(x)
          return {
                'predictions':y_hat.argmax(dim=1),
                'probabilities':nn.functional.softmax(y_hat, dim=1),
                'true_labels':y
          }
          

    #OPTIMIZER CONFIGURATION

    def configure_optimizers(self):
            # Only optimze classifier  parameters (features remain frozen)
            return optim.Adam(self.classifier.parameters(),
                            lr = self.hparams.learning_rate)
    
    @staticmethod

    #method operate independently of the class instances
    def get_class_map() -> Dict[int, str]:
          """
          EuroSAT class index to name mapping 
          """
          return{
                0: 'AnnualCrop',
                1: 'Forest',
                2: 'HerbaceousVegetation',
                3: 'Highway',
                4: 'Industrial',
                5: 'Pasture',
                6: 'PermanentCrop',
                7: 'Residential',
                8: 'River',
                9: 'SeaLake'
          }

# define custom dataset class that inherits from PyTorch' Dataset
class EuroSATDataset(Dataset):
    '''
    This custom dataset class inherits from the PyTorch Dataset class
    EuroSAT RGB Dataset Loader
    Args:
        data_dir: Path to dataset root directory
        transform: Torchvision transforms to apply
    '''
    def __init__(self, data_dir, transform=None):
          self.data_dir = self.transform = transform
          self.images = []
          self.labels = []
          self.class_names = [f for f in os.listdir(data_dir) if f != '.DS_Store']

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
         img_path = self.images[idx]
         image = Image.open(img_path)
         label = self.labels[idx]

         if self.transform:
              image = self.transform(image)

         return image, label
         
     
# Defines a Lighning DataModule for handling the EuroSAT dataset
class EuroSATDataModule(L.LightningDataModule):
     """
     Data handling module for EuroSAT with train/val/test splits

     Args:
        data_dir: Path to dataset root directory
        batch_size: Samples per batch
        num_workers: CPU workers for data loading
     """
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
          return DataLoader(self.train_dataset, batch_size = self.batch_size,shuffle = False, num_workers=self.num_workers)

     def val_dataloader(self):
          return DataLoader(self.val_dataset, batch_size = self.batch_size,shuffle = False, num_workers=self.num_workers,persistent_workers=True)
     
     def test_dataloader(self):
          return DataLoader(self.test_dataset, batch_size = self.batch_size,shuffle = False, num_workers=self.num_workers,persistent_workers=True)

 
# STEP 2: RUN THE TRAINER

if __name__ == "__main__":
     # Argument Parsing
     parser=argparse.ArgumentParser(description='EuroSAT Land Cover Classification')

     parser.add_argument('-mode',choices=['train','inference'],required=True)
     parser.add_argument('--checkpoint',type=str,help='Model checkpoint path')
     parser.add_argument('--data_dir',default='./data/EuroSAT_RGB_250')
     parser.add_argument('--batch_size', default=8,type=int)
     parser.add_argument('--precision',choices=['16','32'], default='32')
     parser.add_argument('--export_onnx',action='store_true')
     parser.add_argument('--onnx_path',default='eurosat_vgg.onnx', type=str)
     parser.add_argument('--disable_progress',action='store_true')
     args = parser.parse_args()


     #Data Module
     data_module = EuroSATDataModule(
           data_dir=args.data_dir,
           batch_size=args.batch_size,
           num_workers=4
     )
     data_module.setup()

     # Training mode

     if args.mode == 'train':
           model = CustomVGG(num_classes=10)

           trainer= L.Trainer(
                 max_epochs=5,
                 accelerator='auto',
                 precision=args.precision,
                 callbacks=[
                       L.pytorch.callbacks.ModelCheckpoint(
                             monitor='val_acc',
                             mode='max',
                             save_top_k=1,
                             filename='best-{epoch:02d}-{val_acc:.2f}'
        
                       )
                       
                 ],
                 enable_progress_bar=not args.disable_progress

           )

           trainer.fit(model, datamodule=data_module)

           # Export to ONNX if specified 
           # Export failed:'NoneType' object has no attribute 'flush'
           if sys.stdout is not None:
                 sys.stdout.flush()
           if args.export_onnx:
                 model.eval()

                 # create input sample matching actual dimensions
                 input_sample = torch.randn(1,3,64,64)

                 #export with error handling

                 try:
                       torch.onnx.export(
                             model,
                             input_sample,
                             export_params=True,
                             input_names=['input'],
                             output_names=['output'],
                             dynamic_axes={
                                   'input':{0: 'batch_size'},
                                   'output':{0: 'batch_size'}
                       }

                       )
                       print(f'success: Model exported to {args.onnx_path}')

                 except Exception as e:
                       print(f'Export failed:{str(e)}')

            # Inference Mode

     elif args.mode == 'inference':
           if not args.checkpoint:
                 raise ValueError ('Checkpoint path required for inference')
           
           model = CustomVGG.load_from_checkpoint(args.checkpoint)
           model.eval()

           trainer = L.Trainer(
                 accelerator = 'auto', # use gpu if available
                 inference_mode=True,
                 enable_progress_bar=not args.disable_progress,
                 logger = False
           )

           # Generate predictions
           predictions = trainer.predict(model, dataloaders=data_module.test_dataloader())
           preds = torch.cat([p['predictions'] for p in predictions])
           probs = torch.cat([p['probabilities'] for p in predictions])
           labels = torch.cat([p['true_labels'] for p in predictions])

           #Calculate accuracy 
           #print(len(preds))
           print("done processing")

           acc = (preds == labels).float().mean()
           print(f'accuracy is: {acc}')
      
