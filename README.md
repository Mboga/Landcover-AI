# CI_CD_Tutorial
A repository to demonstrate CI and CD in GitHub

# Project Summary

The aim of the repository is to provide a tutorial on CICD in github. CICD stands for Continuous Integration and Continuous Development.
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

We will use the MNIST dataset. It is a handwritten digitized dataset of numbers. The objective is to train a model that can predict a digit from the handwritten number. 

I select this dataset because it is a light dataset, and the aim of this tutorial is to explore CICD actions using github actions.

# Test Project: Deep learning Framework

We will use the Pytorch Lightning deep learning Framework. It is based on pytorch and has the following advantages of vanilla pytorch.
[x] Simplified code structure: organise code into logical setions (training, validation testing) within the lightningmodule. standardized interface for defining models, data loading and training routines
[x] Enhanced Productivity: Automated common tasks like data loading, checkpointing and logging, Easy integration with experiment tracking tools ( tensorboard, WandB)
[x] Scalability and performance: mixed precision training, simplfied multi-GPU and distributed training setups
[x] Best practices and Reproducibility: Modular and organosed code structure, built-in supprot for reproducibility such as deterministic traning, automatics checkpointing
[x] Flexibility and Customisation: specific methods can be overriden for custom logic when needed. Multiple domains support




