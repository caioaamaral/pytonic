from setuptools import setup
from setuptools import find_packages

setup(
    name='pytonic',
    version='0.1a1',
    python_requires='>=3.5',
    install_requires=['PyYaml', 'singledispatch', 'update_wrapper'],
    packages=find_packages(include=['pytonic']),
    author='Caio Amaral',
    author_email='caioaamaral@gmail.com',
    maintainer='Caio Amaral',
    maintainer_email='caioaamaral@gmail.com',
    url='https://github.com/caioaamaral/pytonic',
    entry_points={
        'console_scripts' : [
            'pytonic=pytonic.console:main'
        ],
        'pytonic.verbs':[
            'create = pytonic.verbs.pytonic_create',
            'workspace = pytonic.verbs.pytonic_workspace'
        ]
    }
)
