from setuptools import setup, find_packages

setup(
    name='The Fast Neutron',
    version='0.2.0',
    description='Code for The Fast Neutron videos',
    url='https://github.com/isaac-dabkowski/the-fast-neutron',
    author='Isaac Dabkowski',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "selenium"
    ],
)
