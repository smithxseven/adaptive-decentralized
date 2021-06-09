from setuptools import setup

setup(
    name = 'adaptive',
    version = '0.1.0',
    packages = ['adaptive'],
    entry_points  = {
        'console_scipts': [
            'adaptive = adaptive.__main__:main'
        ]
    }
)