import os
from setuptools import setup

with open(os.path.join(os.path,dirname(__file__),'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name = 'django-menuresolver',
        version = '0.1' ,
        packages = ['menuresolver'],
        include_package_data = True,
        license = 'BSD License',
        description = 'A Django app to create menues',
        long_description = README,
        author = 'Link-B',
        author_email = 'marco@link-b.com',
        url = '',
        classifiers = [
            'Enviroment :: Web Enviroment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            ],
        )
