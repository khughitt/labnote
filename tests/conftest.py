"""
Labnote Notebook Fixture

Note: When running tests in a virtualenv container, be sure to install py.test
      in the virtualenv so that system version isn't used instead.
"""
import os
import pytest
from pkg_resources import resource_filename, Requirement
from labnote import Notebook

@pytest.fixture(scope="module")
def notebook():
    example_conf = 'example/example.config.yml'
    return Notebook(example_conf)
