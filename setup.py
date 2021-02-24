from setuptools import find_packages, setup

setup(
    name='nyuad-matchmaker',
    packages=find_packages(include=['nyuad-matchmaker']),
    version='0.0.0',
    description='Matchmaking algorithm for NYUAD students',
    author='NYUAD Soulmates Team',
    license='MIT',
    install_requires=['numpy', 'matching'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
