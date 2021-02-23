from setuptools import find_packages, setup

setup(
    name='nyuad-matchmaker',
    packages=find_packages(include=['nyuad-matchmaker']),
    version='0.0.0',
    description='Matchmaking algorithm for NYUAD students',
    author='NYUAD Soulmates Team',
    license='MIT',
    install_requires=['matching'],
    setup_requires=[],
    tests_require=[],
    test_suite='tests',
)
