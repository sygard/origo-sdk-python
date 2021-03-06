# Development

## Getting started

Setup
```
git clone git@github.oslo.kommune.no:origo-dataplatform/origo-sdk-python.git
cd origo-sdk-python
python3.7 -m venv .venv
. .venv/bin/activate
make init
```

Run all tests:
```
$ make test
```

Reformat files:
```
make format
```

## Releasing a new sdk version
* Checkout the master branch
* Either run `make` 

or manually run the make targets:
1. Test
```
make clean test
```
2. Bump version and Build
```
make bump-patch build 
```
3. Publish the module to pypi
```
make publish-module
```
* Finally push the version bump changes to git. Either make a new PR or push to master