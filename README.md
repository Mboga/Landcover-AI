# LANDCOVER CLASSIFICATION USING DEEP LEARNING
A repository demonstrating landcover classification using deeplearning. The use of software development tools in machine learning such as CICD, DVC, MLflow.model development in using PyTorch Lightning.

# Project Summary

The aim of the repository is to showcase the use of several software development tools in a machine learning project. Tutorials of various tools are provided. Where possible, extra information on the tools is provided.

One of such tools is CICD using Github actions. CICD stands for Continuous Integration and Continuous Development.
In Software development, software development is often fast-paced. CICD can helps to assure the product quality while enhancing development efficiency.

In brief, benefits of CICD are:
1. Faster delivery: through automation of many manual processes
2. Improved code quality: Automated testing in CI cateches bugs earluy. Each code merge triggers tests, to detect issues before reaching production
3. Reduced Risk: Frequent smaller deployments make it easier to detect and fix issues early, minimizing the chance of major disruptions. CICD pipelines have rollback mechanisms for quicl recovery if problems arise
4. Increased efficiency: Automation of integration and testing and deployment processes allow developers to focus on writing code other than manual tasks.
5. Better Collaboration: With CICD, teams are smaller and can work on specific items without conflicting with others
6. Continuous Feedback: The automated deployment process in CD allows for swift observation of software performance in production, enabliing faster/quick response to problems and issues when they arise.

# Test Project

The test project will be a simple machine learning project. The basic workflows will comprise of data preparation, model training, and model testing. 

# Test Project: Data

We will use the EuroSAT dataset. This is a dataset that is generated from Sentinel 2 imagery. It contains 10 landcover classes. For the demonstration, we will use a reduced dataset size of 1000 images sampled from 35000 imagery.

The EuroSAT dataset can be accessed from the url: https://zenodo.org/records/7711810#.ZAm3k-zMKEA 
I select this dataset because it is a well curated benchmark datasset that is publicly available. Further, the aim of this repo is to explore CICD actions using github actions.

# Test Project: Deep learning Framework

We will use the Pytorch Lightning deep learning Framework. It is based on pytorch and has the following advantages of vanilla pytorch.
- [x] Simplified code structure: organise code into logical setions (training, validation testing) within the lightningmodule. standardized interface for defining models, data loading and training routines
- [x] Enhanced Productivity: Automated common tasks like data loading, checkpointing and logging, Easy integration with experiment tracking tools ( tensorboard, WandB)
- [x] Scalability and performance: mixed precision training, simplfied multi-GPU and distributed training setups
- [x] Best practices and Reproducibility: Modular and organosed code structure, built-in supprot for reproducibility such as deterministic traning, automatics checkpointing
- [x] Flexibility and Customisation: specific methods can be overriden for custom logic when needed. Multiple domains support


# Test Project: Installation

I provide the installation set up in a mac OS with M3 Chips.

1. Create a virtual environment using the venv module. We have Python 3.9.6 installed in the PC.

``` python3 -m venv earth_vision```

2. Activate the virtual environment named earth_vision.

``` source earth_vision/bin/activate```

3. The terminal prompt will then change to indicate that you are working inside the virtual environment. Verify the python version that you are working on

``` python --version```

4. To deactivate the virtual environment, remember to simply run deactivate.

``` deactivate```

- Virtual environments are project specific, allowing you to manage dependencies independently for each project.


5. For a mac environment, the following environment variables need to be set (https://pytorch-lighting.readthedocs.io/en/latest/starter/installation_mac.html). This is because we are not using an nvidia chip, but instead an apple silicon based chip.

``` export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1```
``` export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1 ```

6. Install the packages contained in the requirements.txt file:

``` pip install -r requirements.txt```

# Test Project: CICD framework

Github actions will be used to implement the Continuous Integration and Continuous Deployment framework

