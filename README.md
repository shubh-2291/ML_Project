# ML_Project

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in the src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

# How to run?

### STEPS:
 Clone the repository

 ```bash
https://github.com/shubh-2291/ML_Project.git
```
### STEP 01- Create a virtual environment after opening the repository

```bash
virtualenv env
```
#### Note: if virtualenv not installed , intalled it.
```bash
pip install virtualenv
```
### step 02- activate virtual environment
```bash
env/Scripts/activate
```
### step 03- install the requirements
```bash
pip install -r requirements.txt
```
```bash
python app.py
```
Now,
``` bash
open up your host and port
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

#### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com)

MLFLOW_TRACKING_URI=[https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow \](https://dagshub.com/shubh-2291/ML_Project.mlflow)

MLFLOW_TRACKING_USERNAME=shubh-2291

MLFLOW_TRACKING_PASSWORD=bda8667039f829190ef0956963cf5992817e71f0
python script.py

Run this to export as env variables:

```bash

set MLFLOW_TRACKING_URI=https://dagshub.com/shubh-2291/ML_Project.mlflow

set MLFLOW_TRACKING_USERNAME=shubh-2291

set MLFLOW_TRACKING_PASSWORD=bda8667039f829190ef0956963cf5992817e71f0

```