from setuptools import setup

setup(
    name = 'adaptive',
    version = '0.1.1',
    packages = ['adaptive'],
    entry_points  = {
        'console_scipts': [
            'adaptive = adaptive.__main__:main'
        ]
    }
)