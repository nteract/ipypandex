# Releasing

## Prerequisites

- First check that the CHANGELOG is up to date for the next release version
- Ensure requirements are installed `pip install .`

## Push to GitHub

Change from patch to minor or major for appropriate version updates.

```bash
bumpversion patch
git push upstream && git push upstream --tags
```

## Push to PyPI

```bash
rm -rf dist/*
rm -rf build/*
# NO bdist_wheel because it's not supported
# See https://github.com/pypa/packaging-problems/issues/64
python setup.py sdist
twine upload dist/*
```
