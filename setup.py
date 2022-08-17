from inspect import classify_class_attrs
from setuptools import find_packages, setup
setup(
    name='bazzellpy',
    packages=find_packages(include=['bazzellpy']),
    version='1.0.0',
    description='IntelTechniques OSINT tools as callable functions in Python!',
    readme='README.md'
    author='dmw94',
    license={ file = 'LICENSE' },
    classifiers= [
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
    keywords= ['osint', 'searching', 'scraping']
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)