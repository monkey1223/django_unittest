import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='simple_blog_app',
    version='1.0',

    packages=[
	     'article',
	     'account', 
	     'django_test', 
	     'test',
	     'verify_pack'
	],

    package_dir={
	    'article':'blog_project/article',
	    'account':'blog_project/account',
	    'django_test':'blog_project/django_test',
	    'test':'blog_project/test',
	    'verify_pack':'blog_project/verify_pack'
	},
#    scripts=['manage.py'],
    data_files=[('.', ['blog_project/manage.py'])],

    
    include_package_data=True,
    license='BSD License', 
    description='A simple Blog app for testing',
    long_description=README,

    test_suite="tests",
    tests_require=["nose"],


    author="DevSKiller.com",
    author_email="support@devskiller.com",

    install_requires=[
	'Django==1.8.9',
	'defusedxml==0.4.1',
	'django-bootstrap-toolkit==2.15.0',
	'django-tastypie==0.13.1',
	'lxml==3.5.0',
	'nose==1.3.7',
    ],

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
	'Framework :: Django :: 1.8.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3.4',
    ],
)
