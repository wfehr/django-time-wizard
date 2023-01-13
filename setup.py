from setuptools import find_packages, setup
from time_wizard import __version__


setup(
    name='django-time-wizard',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'django>=2.0,<5.0',
        'django-polymorphic>=2.1.2,<3.2',
        # fixed version: different versions may result in migrations because
        # of field-choices for countries!
        'holidays==0.18',
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
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
