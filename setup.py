from setuptools import setup, find_packages

setup(
    name='stellarutil',
    version='0.0.29',
    author='Cameron Ross',
    author_email='ceross@cpp.edu',
    description= 'A utility package for CPP Fire Squad',
    packages=find_packages(),
    license='MIT',
    url='https://github.com/CPP-FIRE-Squad/stellarutil',
    # py_modules=['console', 'graph', 'simulation', 'calculations'],
    entry_points={
        'console_scripts': [
            'stellarutil = stellarutil.console:entry',
        ],
    },   
)