from setuptools import setup, find_namespace_packages

setup(
    name="{{ cookiecutter.project_slug }}",
    version="0.1",
    packages=find_namespace_packages(include=["{{ cookiecutter.project_slug }}.*"]),
)
