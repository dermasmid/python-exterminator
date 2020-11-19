from setuptools import setup
import re


with open('README.md', encoding='utf-8') as f:
    readme = f.read()

with open('exterminator.py', encoding= 'utf-8') as f:
    version = re.findall("__version__ = '(.+)'", f.read())[0]





setup(
    name = 'exterminator',
    version = version,
    py_modules=['exterminator'],
    url = 'https://github.com/dermasmid/python-exterminator',
    license = 'MIT',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    author = 'Cheskel Twersky',
    author_email= 'yoursn21@gmail.com',
    description = 'Log the important data when a exception occurs.',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
    )
