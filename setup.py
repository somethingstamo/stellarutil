from setuptools import setup, find_packages

setup(
    name='stellarutil',
    version='0.0.1',
    author='Cameron Ross',
    author_email='ceross@cpp.edu',
    description= 'A utility package for CPP Fire Squad',
    license='MIT',
    url='https://github.com/CPP-FIRE-Squad/stellarutil',
    py_modules=['cross2'],
    entry_points={
        'console_scripts': [
            'stellarutil = cross2:help',
        ],
    },
    
)
