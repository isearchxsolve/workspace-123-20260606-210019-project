from setuptools import setup

setup(
    name='tsp',
    version='1.0',
    packages=['tsp'],
    install_requires=['numpy', 'scipy'],
    entry_points={'console_scripts': ['tsp = tsp:main']}
)
