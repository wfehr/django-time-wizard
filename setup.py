from setuptools import find_packages, setup
from time_wizard import __version__


setup(
    name='django-time-wizard',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'django>=3.0,<5.1',
        'django-polymorphic>=2.1.2,<5.0',
        'holidays>=0.23',
    ],
    include_package_data=True,
    description='Date and time dependend content manipulation',
    long_description=open('README.rst').read(),
    url='https://github.com/wfehr/django-time-wizard',
    download_url='https://github.com/wfehr/django-time-wizard/tarball/master',
    author='Wolfgang Fehr',
    author_email='dev@wfehr.de',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
