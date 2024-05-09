# Data Science done right

Data science tips and tricks to enhance data analysis and predictive modeling.

Most of the tips shown here aren't directly useful to the day-to-day job, but they'll demistify many concepts around machine learning and data science. This knowledge will hopefully build up to the point it'll help you achieve greater results as the blackbox around many `pip install magic-buttons` used daily are opened.

## Table of Contents
* [Tutorials](#tutorials)
* [Using this repo](#using-this-repo)
* [License](#license)

### About me
#### Links
* [E-mail](mailto:lunde@adobe.com)
* [GitHub](https://github.com/BreytMN)
* [LinkedIn](https://www.linkedin.com/in/breytner-nascimento/)
* [Portfolio](https://portfolio.breytmn.com)

## Tutorials:

### Classification
* [Upskilling a no-skill classifier with Conformal Prediction](notebooks/classification/no_skill.ipynb) - updated 2024-05-09
* ["You can't classify with linear regression"](notebooks/classification/linear_regression_classifier.ipynb) - added 2024-05-09

### Regression
* [Linear Extrapolation with non-linear algorithms](notebooks/regression/extrapolation.ipynb) - updated 2024-05-09

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

## License
[MIT License](LICENSE)