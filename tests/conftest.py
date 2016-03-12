"""
Labnote Notebook Fixture

Note: When running tests in a virtualenv container, be sure to install py.test
      in the virtualenv so that system version isn't used instead.
"""
import os
import pytest
from pkg_resources import resource_filename, Requirement
from labnote import Notebook

@pytest.fixture(scope="session")
def nb1(tmpdir_factory):
    conf = 'tests/notebooks/nb1/config.yml'
    outfile = str(tmpdir_factory.mktemp('output').join('index.html'))
    return Notebook(conf, output_file=outfile)
