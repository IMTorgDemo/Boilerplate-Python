Sample Module Repository
========================

This simple project is an example repo for Python projects.

`Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.




ToDo
========================

* ~~pipenv~~
* ~~vscode setup~~
* ~~config.json~~
* ~~.env file~~
* ~~logging~~
* testing
* dockerfile
* load to pypi



Getting Started
========================

Prepare environment

```
#env variables
cp .env_example .env
#review config.json
vi config.json
```

Run commandline

```
$ pipenv --three
$ pipenv install
$ pipenv shell
(venv)$ python sample/core.py
```

Run tests

```
(venv)$ pytest
(venv)$ python bundler
```