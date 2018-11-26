from setuptools import find_packages, setup


setup(
    name='mnistapi',
    version='0.0.1',
    description='mnist Web API',
    url='https://github.com/gbourdin/awesome_project_api',
    author='German Bourdin',
    author_email='german.bourdin@gmail.com',
    packages=find_packages(),
    install_requires=[
        'flask-restplus>=0.10.0',
        'mnistpredictor==0.0.1',
        'uWSGI>=2.0.0',
    ],
    setup_requires=[
        'pytest-runner>=2.11.0',
    ],
    tests_require=[
        'pytest>=3.2.0',
        'pytest-flask>=0.10.0'
    ],
    extras_require={
        'dev': [
            'pycodestyle>=2.3.0',
            'flake8>=3.5.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'mnistapi = mnistapi.__main__:cli'
        ]
    },
)
