import pytest

from {{ cookiecutter.project_slug }}.{{ cookiecutter.module_name }} import sample

class test_sample():
    assert sample(1) == 43
    