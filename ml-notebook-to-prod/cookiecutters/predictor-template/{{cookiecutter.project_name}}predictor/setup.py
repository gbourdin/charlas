from setuptools import find_packages, setup


setup(
    name='{{cookiecutter.project_name}}predictor',
    version='0.0.1',
    description='{{cookiecutter.project_name}} Predictor',
    url='{{cookiecutter.project_git_url}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
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
            '{{cookiecutter.project_name}}predictor = {{cookiecutter.project_name}}predictor.__main__:cli',
        ]
    },
    zip_safe=False
)
