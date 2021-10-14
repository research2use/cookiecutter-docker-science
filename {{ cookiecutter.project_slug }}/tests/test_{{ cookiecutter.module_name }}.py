import pytest

from {{ cookiecutter.project_slug }}.{{ cookiecutter.module_name }} import sample

def test_sample():
    assert sample(1) == 43
    