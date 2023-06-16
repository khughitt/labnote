Development
-----------

Contributing
~~~~~~~~~~~~

There are a few different ways you can contribute to the development of
Labnote. The easiest way is to simply fork the Labnote repo, add whatever
fixes or functionality you would like, and submit a pull request with the
changes.

If you are adding new functionality, please be sure to write unit tests where
relevant.

If you have ideas or suggestions, but aren't able to implement them yourself,
feel free to `contact me <mailto:khughitt@umd.edu>`__, or open up an issue with
your idea or suggestion on the `Labnote Github repo
<https://github.com/khughitt/labnote/issues>`__.

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

Creating new themes
~~~~~~~~~~~~~~~~~~~

More on this later...


