import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-time-wizard',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'django-polymorphic',
        'django<2.0',
        'holidays',
    ],
    include_package_data=True,
    description='Date and time dependend content manipulation',
    long_description=README,
    url='https://github.com/wfehr/django-time-wizard',
    download_url='https://github.com/wfehr/django-time-wizard/tarball/master',
    author='Wolfgang Fehr',
    author_email='wolfgangfehr@fotopuzzle.de',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
