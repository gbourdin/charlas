from setuptools import find_packages, setup


setup(
    name='housepriceapi',
    version='0.0.1',
    description='houseprice Web API',
    url='https://github.com/gbourdin/awesome_project_api',
    author='German Bourdin',
    author_email='german.bourdin@gmail.com',
    packages=find_packages(),
    install_requires=[
        'flask-cors>=3.0.7',
        'flask-restplus>=0.10.0',
        'uWSGI>=2.0.0',
        'xgbpricepredictor==0.0.1',
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
            'housepriceapi = housepriceapi.__main__:cli'
        ]
    },
)
