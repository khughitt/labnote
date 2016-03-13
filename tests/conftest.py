"""
Labnote Notebook Fixture

Note: When running tests in a virtualenv container, be sure to install py.test
      in the virtualenv so that system version isn't used instead.
"""
import os
import pytest
import time
from labnote import Notebook

@pytest.fixture(scope="session")
def nb1(tmpdir_factory):
    conf = 'tests/notebooks/nb1/config.yml'
    outfile = str(tmpdir_factory.mktemp('output').join('index.html'))

    # touch files to update timestamp:
    # since the entry 'date' fields are set at the time of notebook
    # construction, it's easier to start with the entries date-sorted, and
    # then resort by title to test both sort types.
    base_dir = 'tests/notebooks/nb1/foo'
    for x in sorted(os.listdir(base_dir)):
        # Python 3.4+
        #pathlib.Path(os.path.join(base_dir, x)).touch()
        os.utime(os.path.join(base_dir, x), None)
        time.sleep(1)

    base_dir = 'tests/notebooks/nb1/bar'
    for x in sorted(os.listdir(base_dir)):
        os.utime(os.path.join(base_dir, x), None)
        time.sleep(1)

    return Notebook(conf, output_file=outfile)

@pytest.fixture(scope="session")
def nb1_alphanum(tmpdir_factory):
    conf = 'tests/notebooks/nb1/config.yml'
    outfile = str(tmpdir_factory.mktemp('output').join('index.html'))

    return Notebook(conf, output_file=outfile, 
                    sort_entries_by_date=False, sort_categories_by_date=False)
