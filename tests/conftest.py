"""
Labnote Notebook Fixture

Note: When running tests in a virtualenv container, be sure to install py.test
      in the virtualenv so that system version isn't used instead.
"""
import os
import pytest
from pkg_resources import resource_filename
from labnote.notebook import Notebook

@pytest.fixture(scope="module")
def notebook():
    #example_conf = resource_filename(__name__,
    #                                 os.path.join('example', 'example.config.yml'))
    example_conf = 'example/example.config.yml'
    print(example_conf)
    return Notebook(example_conf)
