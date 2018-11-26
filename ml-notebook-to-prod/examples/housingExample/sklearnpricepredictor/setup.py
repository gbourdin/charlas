from setuptools import find_packages, setup


setup(
    name='sklearnpricepredictor',
    version='0.0.1',
    description='sklearnprice Predictor',
    url='https://github.com/gbourdin/awesome_project_api',
    author='German Bourdin',
    author_email='german.bourdin@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'click>=7.0',
        'click-repl>=0.1.6',
        'scikit-learn>=0.20.0',
        'pandas>=0.23.4',
    ],
    extras_require={
        'dev': [
            'flake8>=3.4.1',
            'pycodestyle>=2.3.1',
        ],
    },
    entry_points={
        'console_scripts': [
            'sklearnpricepredictor = sklearnpricepredictor.__main__:cli',
        ]
    },
    zip_safe=False
)
