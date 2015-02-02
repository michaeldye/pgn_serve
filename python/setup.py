import sys
from setuptools import setup, find_packages

setup(
    name='pgn_serve',
    version='0.1.0',
    description='PGN-formatted random historic chess game server',
    author='michaeldye',
    author_email='m-github@divisive.info',
    license='GPL v3',
    packages=find_packages(),
    include_package_data=True,
    requires=(
        'python27',
    ),
    setup_requires=(
        'setuptools>=0.9.8',
    ),
    install_requires=(
        'pgnparser==1.0',
        'flask==0.10.1',
        'requests==2.5.1',
        'tornado==3.2',
    ),
)

# vim: set ts=4 sw=4 expandtab:
