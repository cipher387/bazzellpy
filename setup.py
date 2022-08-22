from inspect import classify_class_attrs
from setuptools import find_packages, setup
setup(
    name='bazzellpy',
    packages=find_packages(include=['bazzellpy']),
    version='1.0.0',
    description='IntelTechniques OSINT tools as callable functions in Python!',
    long_description='bazzellpy allows you to call IntelTechniques Search Tools as functions in your Python program. This useful suite of OSINT tools are a great start for any investigation. I wanted to be able to call on these tools without having to re-paste code when working on more complex projects. I have made this library available so you can too.',
    readme='README.md',
    author='dmw94',
    license='GPLv3',
    classifiers= [
        'License :: OSI Approved',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords=['osint', 'searching', 'scraping'],
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)