Development
-----------

Contributing
~~~~~~~~~~~~

The project is just getting started and is changing rapidly.
`Let me know<mailto:khughitt@umd.edu>`__ if you have suggestions or
would like to contribute.

Running tests
~~~~~~~~~~~~~

The easiest way to run the unit tests for labnote is to create a
virtualenv container and run the tests from within there. For example,
if you have
`virtualenvwrapper <https://virtualenvwrapper.readthedocs.org/en/latest/>`__,
you can run:

::

    git clone https://github.com/khughitt/labnote && cd labnote
    mkvirtualenv labnote
    pip install -e .
    pip install pytest
    hash -r
    py.test

If you already cloned the labnote repo, you can skip the first step
above and simply ``cd`` to the repo directory.

The ``hash -r`` command in the above is needed after installing py.test
to ensure that the virtualenv version of py.test is used, and not a
system version.

To run the tests for a different version of Python, you can simply
create a second virtualenv for that version of Python and repeat the
process:

::

    mkvirtualenv --python=python3.3 labnote33

Note that virtualenvwrapper is not needed to run the tests, and the
commands for using the base version of virtualenv are pretty similar.

TODO
~~~~

Things to be added...

- Should entries be added via .labnote files, even if they aren't detected in
  the search paths? If so, may want to first add entries as-is, and then in a
  second round, scan for .labnote files and update affected entries / add new
  ones.
- Switch to regexes for search path? (more flexible, but less simple...)
- Add option to automatically generate README.html files for each README.md
  found (check last modified date to determine whether file should be
  regenerated.)
- Check for git revision and link to repo if on Github
- Add option to show short git commit hashes next to entries which associated
  with repos.
- Allow sorting of categories by order in settings (default), name, or
  date-modified.
- Add option to show entries in a "journal mode" with all entries displayed
  together, sorted from most recent to oldest. Category divisions can either be
  hidden entirely, or displayed as (colored) tags to the right side of the
  entry titles.
- Validate config file before running; print out warning messages for missing
  images.

