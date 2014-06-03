"""amsin is a simple command line tool to shortlink an
amazon URL.

"""
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='amsin',
    description="Simple tool for shortlinking amazon pages.",
    long_description=__doc__,
    packages=['amsin'],
    author='Anthony Grimes',
    author_email='i@raynes.me',
    url='https://github.com/Raynes/amsin',
    license='MIT',
    install_requires=requirements,
    entry_points = """
    [console_scripts]
    amsin=amsin.__main__:amsin
    """
)
