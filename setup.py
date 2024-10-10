from setuptools import setup, find_packages

setup(
    name='patternSpeed',
    version='0.6.3',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)