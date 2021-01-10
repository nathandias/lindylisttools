from setuptools import setup

setup(
    name='LindyListTools',
    version='1.0',
    py_modules=['bands'],
    install_requires=[
        'Click', 'SqlAlchemy'
    ],
    entry_points='''
        [console_scripts]
        bands=bands:cli
    ''',
)