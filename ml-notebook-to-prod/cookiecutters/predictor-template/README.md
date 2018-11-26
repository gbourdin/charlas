# Machine Learning Model Template

Creates a minimal template to create re-usable machine learning models
___
## Repository structure

* **{{cookiecutter.project_name}}predictor:**
  * **{{cookiecutter.project_name}}predictor:**
Basic python package designed to mimic sklearns interface and provide a cli
command to run training tasks
    * **setup.cfg:**
Some standard configurations for this template.
    * **setup.py:**
Setup script file.
  * **cookiecutter.json:**
Configuration file with default values for this template.
  * **README.md:**
This file.


## How it works
* Install [cookiecutter](https://github.com/audreyr/cookiecutter#a-pantry-full-of-cookiecutters)
```
$ pip install cookiecutter
$ cookiecutter predictor-template
```
