# Data Science done right

Data science tips and tricks to enhance data analysis and predictive modeling.

* [Tutorials](#tutorials)
* [Using this repo](#using-this-repo)

## Tutorials:
* [Linear Extrapolation with non-linear algorithms](src/regression/extrapolation.ipynb)
* [Upskilling a no-skill classifier with Conformal Prediction](src/regression/no_skill.ipynb)

## Using this repo
Clone the repository:
```bash
git clone git@github.com:BreytMN/datascience-done-right.git
```

I suggest using VS Code as text editor and IDE for navigating this repository. Open the folder inside VS Code after changing directory with:
```bash
cd datascience-done-right
code .
```

This repository is written using WSL with an Ubuntu distro running Python 3.12. If you do not have Python 3.12 installed, you can run this on terminal (Ubuntu):
```bash
make python
```
This will install Python 3.12 and all dependencies need to run it, in the end it will prompt the user to set the default version for Python.

After that you can run:
```bash
make venv
source .venv/bin/activate
```
The first command will create a virtual environment and install all libraries needed to run any code inside this repository. The second command will activate the environment.