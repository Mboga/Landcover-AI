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

# Test Project: Testing

Software testing is needed in the development process to ensure that the application mets the requirements and functions as intended.

They include:
1. Unit testing: Validates individual components /functions in isolation
2. Integration testiing: Checks hos different modules/components work together
3. Functional testing: Ensures the software meets specified functional requirements
4. System Testing: Evaluates the complete, integrated system against specified requirements
5. Acceptance testing: verifies if the software meets user/business requirements
6. Performance Testing: Assesses speed, responsivity and stability under various conditions
7. Security Testing: Identifies vulnerabilities and ensures data protection
8. Usability Testing:Evaluates user-friendliness and overall usr experience
9. Compatibility testing: checks functionality acoss different environments, devices and browsers
10. Regression Testing: Ensures existing features will still work after changes or updates

These tests are done in a commbination of manual and automated approaches with the goal of improving software quality, reliability and user satisfaction. 


# Test project: Unit Tests

Summary of the blog found in the link (https://www.accelq.com/blog/unit-testing/) 


Unit testing is a type of software testing where individual units/components of a software are tested

- Focus on testing small isolated units of code
- Conducted during the development phase
- manual/automated
- aims to catch defects early before system integration

Importance:

- Early bug detection
- Improved code quality - enforces modular programming => Clean, structured codebase
- Facilitate refactoring
- Act as documentation : reference point for new developers, helping them understand the expected behaviour of different components
- automation enhances speed of development

How to write Effective Unit Tests:

- Determine the smallest testatble part of your application =>function/method
- Write test cases => normal cases, edge/boundary cases, error conditions
- Isolate the unit =>use mocks and stubs to simulate the dependencises, ensuring the unit functions independently
- Run the tests=> utilize the testing frameworks : ( JUnit for Java, NUnit for .NET or PyTest for Python) to execute the test cases
- Review the results: Analyze the  tests results to identify and resolve any failures
- Refactor and Retest: After making the changes, rerun the tests to validate code integrity


Best practices for Unit Testing:
- **Write Reliable and clear Unit Tests**: Should be provide clear, reproducible results. Use assertions and meaningful test case descriptions
- **Automate Unit Testing**: Automate unit tests to gain fast feedback and improve test coverage
- **Focus on use cases**: prioritize how to write unit tests based on real-world uses cases, ensureing the code is easily maintainable and understandable
- **Integrate Unit Testing into CI/CD pipelines** Run unit tests in CI/CD to detect issues early on
- **Follow consistent Naming Conventions** Use a standard test naming convention to improve readability and defect tracking 

An example of unit testing in python using PyTest

```
# code to be tested
def add_numbers(a,b):
    retunr  a + B

#Unit test
import pytest

def test_add_numbers():
    assert add_numbers(2,3) == 5
    assert add_numbers(-1,1) == 0
    assert add_numbers(0,0) == 0

```




