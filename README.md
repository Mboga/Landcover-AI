# LANDCOVER CLASSIFICATION USING DEEP LEARNING
A repository demonstrating landcover classification using deeplearning. We use PyTorch Lightning deep learning framework. 


# Test Project: Data

- We will use the EuroSAT dataset. This is a dataset that is generated from Sentinel 2 imagery. It contains 10 landcover classes. For the demonstration, we will use a reduced dataset size of 1000 images sampled from 35000 imagery.

- The EuroSAT dataset can be accessed from the url: https://zenodo.org/records/7711810#.ZAm3k-zMKEA 

- I select this dataset because it is a well curated benchmark datasset that is publicly available. 

# Test Project: Deep learning Framework

We will use the Pytorch Lightning deep learning Framework. It is based on pytorch and has the following advantages of vanilla pytorch.

- [x] Simplified code structure: organise code into logical setions (training, validation testing) within the lightningmodule. standardized interface for defining models, data loading and training routines
- [x] Enhanced Productivity: Automated common tasks like data loading, checkpointing and logging, Easy integration with experiment tracking tools ( tensorboard, WandB)
- [x] Scalability and performance: mixed precision training, simplfied multi-GPU and distributed training setups
- [x] Best practices and Reproducibility: Modular and organised code structure, built-in supprot for reproducibility such as deterministic traning, automatics checkpointing
- [x] Flexibility and Customisation: specific methods can be overriden for custom logic when needed. Multiple domains support


# Test Project: Installation

I provide the installation set up in a mac OS with M3 Chips using python virtual environment. Virtual environments are project specific, allowing you to manage dependencies independently for each project.

1. Create a virtual environment using the venv module. We have Python 3.9.6 installed in the PC.

``` python3 -m venv earth_vision```

2. Activate the virtual environment named earth_vision.

``` source earth_vision/bin/activate```

3. The terminal prompt will then change to indicate that you are working inside the virtual environment. Verify the python version that you are working on

``` python --version```

4. To deactivate the virtual environment, remember to simply run deactivate.

``` deactivate```

5. For a mac environment, the following environment variables need to be set (https://pytorch-lighting.readthedocs.io/en/latest/starter/installation_mac.html). This is because we are not using an nvidia chip, but instead an apple silicon based chip.

``` export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1```
``` export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1 ```

6. Install the packages contained in the requirements.txt file:

``` pip install -r requirements.txt```

# Script Usage 

on the command line: 

```
usage: main.py [-h] -mode {train,inference} [--checkpoint CHECKPOINT] [--data_dir DATA_DIR] [--batch_size BATCH_SIZE] [--precision {16,32}] [--export_onnx] [--onnx_path ONNX_PATH] [--disable_progress]

EuroSAT Land Cover Classification

optional arguments:
  -h, --help            show this help message and exit
  -mode {train,inference}
  --checkpoint CHECKPOINT
                        Model checkpoint path
  --data_dir DATA_DIR
  --batch_size BATCH_SIZE
  --precision {16,32}
  --export_onnx
  --onnx_path ONNX_PATH
  --disable_progress

```

- for default parameters
training

```
python src/main.py -mode train
```
testing 
```
python src/main.py -mode inference --checkpoint lightning_logs/version_8/checkpoints/best-epoch=04-val_acc=0.76.ckpt
```

- jupyter notebook to perform inference on a folder of images

```
src/notebooks/test_inference.ipynb
```

- Reach out for any questions, comments or requests: nicholus.mboga@savanna-ai.be
- Course material created by Savanna AI (https://savanna-ai.be)