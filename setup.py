from setuptools import find_packages, setup
setup(
    name='bazzellpy',
    packages=find_packages(include=['bazzellpy']),
    version='0.1.0',
    description='IntelTechniques OSINT tools as callable functions in Python!',
    author='dmw94',
    license='GPL-3.0',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)