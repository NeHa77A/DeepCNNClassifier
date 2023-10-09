# Deep Classifer Project

## Workflow

![workflow](https://raw.githubusercontent.com/NeHa77A/DeepCNNClassifier/master/images/Project%20flow.png)


1. for Creating environment and download install package run
```bash
bash init_setup.py
```
it will activate env and install package

2. For testing 
```
pytest -v
```

## Testing
1. tox aims to automate and standardize testing in Python.
```
tox
```
if error occur then again run
```
tox --recreate
```

### tensorboard 
```bash
tensorboard --logdir=artifacts/prepare_callbacks/tensorboard_log_dir/
```

### dvc run
```
dvc init
```
```
dvc repro
```
diagram show
```
dvc dag
```

### check which python is in your system
```bash
which python
```
if there is any other python rather then anaconda or miniconda remove the python package path from your environment veriable edit in window sysytem

if error occur like "no such file or directory in bash"
```bash
conda init bash
```
```bash
echo '. ${HOME}/.bash_profile' >> ~/.bashrc
```
then close bash and open agian 
