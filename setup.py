from setuptools import setup

setup(
    name='LindyListTools',
    version='1.0',
    py_modules=['bands', 'dance'],
    install_requires=[
        'click', 'sqlalchemy', "requests",
    ],
    entry_points='''
        [console_scripts]
        bands=bands:cli
        dance=dance:cli
    ''',
)