from setuptools import find_packages, setup


setup(
    name='{{cookiecutter.project_name}}api',
    version='0.0.1',
    description='{{cookiecutter.project_name}} Web API',
    url='{{cookiecutter.project_git_url}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    packages=find_packages(),
    install_requires=[
        'flask-restplus>=0.10.0',
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
            '{{cookiecutter.project_name}}api = {{cookiecutter.project_name}}api.__main__:cli'
        ]
    },
)
