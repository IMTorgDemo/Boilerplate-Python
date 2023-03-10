Sample Module Repository
========================

_References_


* [using pyenv with pipenv](https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c)
* [repo of original file structure](https://github.com/navdeep-G/samplemod)
* [kennethreitz blog post](<http://www.kennethreitz.org/essays/repository-structure-and-python>)
* [learn more about ``setup.py`` files](https://github.com/kennethreitz/setup.py)
* [python docs for packaging](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* [use pyproject.toml, setup.cfg inplace of setup.py](https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/)


This repo is a template for creating various python distributions to be used with specific python versions.




Functionality
========================

_Configuration and execution_

* ~~pyenv~~
* ~~pipenv~~
* ~~vscode setup~~
* ~~config.json~~
* ~~.env file~~
* ~~logging~~
* ~~testing~~
* documentation / sphinx?
* ~~use globally~~
* ~~use in pipenv~~
* ~~use as import~~
* ~~install and via cmdln~~
* ~~run directly at cmdln~~

_Deployment_

* ~~wheel distribution~~
* ~~binary distribution~~
* obfuscated distribution
* dockerfile
* ~~upload to pypi~~





Workflow
========================

### Setup environment

Install correct python version

```
#ensure correct python version is available
$ pyenv install 3.7.0
#install version to specific local directory
$ pyenv local 3.7.0
```

Configure environment

```
#env variables
$ cp .env_example .env
#review config.json
$ vi config.json
#check versions
$ vi pipfile
#ensure included
$ vi MANIFEST.in
$ vi setup.py
```

Use one of two venv approaches

* Makefile
  - requirements.txt
  - MANIFEST.in

(or)

* pipenv
  - Pipfile
  - Pipfile.lock

Prepare requirements globally 

```
$ make -f Makefile
```

Prepare within virtual pipenv

```
$ pipenv --three
$ pipenv install
$ pipenv install flask
$ pipenv install --dev yapf
$ pipenv shell
```

Run tests

```
(venv)$ pytest
(venv)$ python bundler    #TODO:what is this?
```

Use as import

```
(venv)$ python
>>> import sample
```


### Distributing with PyPI

* add pyproject.toml and setup.cfg
```
$ pipenv install build
$ pipenv requirements > requirements.txt
```

Copy requirements.txt to setup.cfg

```
$ pipenv run python -m build --wheel    
#creates .build/ .dist/
#the primary package is: .dist/sample-0.1.0-py3-none-any.whl
$ pip install dist/sample-0.1.0-py3-none-any.whl --force-reinstall
$ python
>>> import sample
>>> sample.hmm()
   #hmmm... nice username, name@domain.com
   #200
>>> exit()
$ sample
   #ModuleNotFoundError: No module named 'sample.common'
$ rm .env
#clean-up, only .env_example should remain
```


### Uploading the distribution archives

Prepare file: `$HOME/.pypirc` with

```
[testpypi]
  username = __token__
  password = pypi-<PASS>
```

PyPI will check your `setup.cfg` file for correctness and uniqueness of name and version.   PyPI does not allow for a filename to be reused, even once a project has been deleted and recreated.  A distribution filename on PyPI consists of the combination of project name, version number, and distribution type. 

```
$ pipenv run python -m build --wheel    
#creates .build/ .dist/
#the primary package is: .dist/IMTorg_Sample-0.1.2-py3-none-any.whl
pipenv run python -m twine upload --repository testpypi dist/*
```

View the upload, here: https://test.pypi.org/project/IMTorg-Sample/0.1.0/

Install and test with:

```
$ pip install -i https://test.pypi.org/simple/ --no-deps IMTorg-Sample
# python
>>> import sample
>>> sample.hmm()
   #hmmm... nice username, First.Last@Domain.com
   #200
```















Install commandline utility

```
(venv)$ pip3 install .
```

Run commandline

```
(venv)$ python sample/core.py    # TODO:ImportError: attempted relative import with no known parent package
```




Deploying
========================

Build with

```
(venv)$ pip wheel -w dist --verbose .
```

Build for linux

```
#create dockcross manylinux bash driver script
docker run --rm dockcross/manylinux-x64 > ./dockcross-manylinux-x64
chmod +x ./dockcross-manylinux-x64
#build a distributable Python 2.7 Python wheel
./dockcross-manylinux-x64 /opt/python/cp27-cp27m/bin/pip wheel -w dist .
```

Use on linux

```
$ unzip sample-0.1.0-py2-none-any.whl
$ pwd
$ python
python>>> import sys
python>>> sys.path.append(<pwd>)
python>>> import sample
```