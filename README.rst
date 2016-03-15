Labnote
=======

.. image:: https://travis-ci.org/khughitt/labnote.svg?branch=master
    :target: https://travis-ci.org/khughitt/labnote
    :alt: Build Status
.. image:: https://readthedocs.org/projects/labnote/badge/?version=latest
    :target: http://labnote.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

Overview
--------

Labnote is a flexible and lightweight tool for generating
HTML-based `electronic lab
notebooks <https://en.wikipedia.org/wiki/Electronic_lab_notebook>`__.

Rather than attempting to provide a unified tool for creating and sharing lab
notebook entries, Labnote simply ties together existing documents and analyses
outputs and builds and creates an HTML index of these resources.

In short, it helps you go from something like this:

::

    ├── animal_behavior
    │   └── molothrus
    │       └── README.html
    ├── barnacles
    │   ├── cirripede-morphology
    │   │   └── README.html
    │   └── cirripede-taxonomy
    │       └── README.html
    └── finches
        ├── finch-beak-size-comparison
        │   └── beak_size.py
        ├── finch-foraging-strategies
        │   └── foraging-strategies.py
        └── natural-selection
            └── thoughts.txt

To something like this:

.. figure:: docs/images/example_screenshot.png
   :alt: A simple lab notebook

Labnote works by scanning a set of one or more directories for files
matching a pattern that you specify as pertaining to notebook entries
(e.g. a single log, script, or document describing some particular
project or analysis.) It then constructs an HTML table of contents
pointing to each of the matching files. By default, results are sorted
by last-modified date. Categories can be defined and used to separate 
entries relating to different topics.

In order to support as many different work styles as possible, labnote
tries and make as few assumptions as possible about how your files are
organized, and provides configuration options allowing for a wide range of
directory structures and file types.

Finally, labnote is designed to be extensible. While currently there is
only a single no-frills theme, the
`jinga2 <http://jinja.pocoo.org/docs/dev/>`__ templating system used by
Labnote makes it trivial to create themes.

Installation
------------

Requirements
~~~~~~~~~~~~

To use labnote, you must have a recent version of 
`Python (>=3.3) <https://www.python.org/>`__) available on your machine.

Additionally, labnote requires the following Python libraries:

-  `Beautiful Soup 4 <http://www.crummy.com/software/BeautifulSoup/>`__
-  `Jinja2 <http://jinja.pocoo.org/docs/dev/>`__
-  `PyYAML <http://pyyaml.org/>`__

If you are using pip to install labnote, all of the required
dependencies should be automatically installed for you.

Labnote is currently aimed at supporting Windows, Linux, and OS X setups.

Installing labnote
~~~~~~~~~~~~~~~~~~

To install labnote using
`pip <https://docs.python.org/3.5/installing/index.html>`__, run:

::

    pip install labnote

Testing installation
~~~~~~~~~~~~~~~~~~~~

To generate the example notebook, cd to the labnote source directory and
run:

::

    labnote -c example/example.config.yml \
        -i example/research/*/*           \
        -o example/research/index.html

A file named ``index.html`` should be outputted to the ``example/``
directory and should look something like what is shown in the screenshot
above.

Automating notebook generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Labnote can be easily automated using 
`Cron <https://en.wikipedia.org/wiki/Cron>`__. For example, to have labnote
regenerate your lab notebook once a day, run ``crontab -e`` to edit your
user-level cron jobs, and add:

::

    @daily labnote

If you have created a user configuration for labnote in
``$HOME/.config/labnote/config.yml``, then you are all set. Otherwise simply
add whatever options you would use when calling Labnote from the command-line
to the cronjob, e.g.:

::

    @daily labnote -c /path/to/config.yml

For more information on how to create and customize cron jobs on your system,
see the `Ubuntu Cron Tutorial <https://help.ubuntu.com/community/CronHowto>`__.

Configuration
-------------

Notebook configuration
~~~~~~~~~~~~~~~~~~~~~~

Labnote settings can be specified either via the
command-line at run-time (e.g.
``labnote -i /some/path/* -o /output/dir``), or using a
`YAML <http://yaml.org/>`__ config file, or both.

By default, Labnote looks for a file named ``config.yml`` located in
``$HOME/.config/labnote/``. If this file exists, then it will be used
used to configure Labnote's behavior.

The configuration file should look something like:

.. code:: yaml

    ---
    # General information
    title: Lab Notebook
    author: Your Name
    email: email@address.com

    # Notebook contents
    input_dirs:
      - /home/user/Dropbox/research/201[2-5]/*
      - /home/user/Dropbox/research/2016/*/*
      
    output_file: /home/user/Dropbox/research/index.html

    include_files: ['*.html', '*.py', '*.ipynb', 'README.*']

    # Research categories
    categories:
      'Sequence Analysis': ['seq', 'dna', 'rna']
      'Differential Expression': ['dea', 'differential-expression']
      'Network Analysis': ['network']
      'Visualization': ['viz']

The main settings that are important to define are:

1. ``input_dirs`` - One or more
   `wildcard <http://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm>`__
   filepath expressions
2. ``output_file`` - Path to save resulting HTML and its associated files
   to. Most often, this will be located some parent directory of the input
   directories, possibly in a web-accessible location (e.g.
   ``/var/www/index.html`` or ``~/public_html/notebook.html``).
3. ``include_files`` - Files to link to in your notebook.
4. ``categories`` - A set of categories you would like to use to
   organise your notebook, along with some search strings which can be
   used to find project directories that should be placed under those
   categories.\*

You can also point to a config file located in a different location
using the ``-c`` option, e.g. ``labnote -c /path/to/config.yml``. If a
setting is specified both in a configuration file and using a
command-line switch, the option specified on the command-line will take
precedence.

\*Depending on how you have organized your files, this may be difficult
to setup. It works best if you can normalize your directory names such
that related analyses all include a similar component (e.g.
'xx-network-analysis').

If that is not possible or convenient, Labnote also supports
manually specifying a projects categorization using hidden `.labnote` metafiles
inside each project directory.

Customizing individual entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the automatic processing of entries that labnote normally uses
to render notebook entries, directory-specific `.labnote` files can also be
used to control the behavior and appearance of entries. These are YAML files,
and should follow the format:

.. code:: yaml

    ---
    README.html:
      title: Custom Title
    pipeline.sh:
      title: My Interesting Analysis Pipeline

Furthermore, `.labnote` files can be used to specify additional entry metadata
that can't be automatically detected such as a description of the notebook
entry and links to external resources such as web-pages, presentation slides, 
etc:

.. code:: yaml

    ---
    README.html:
      title: Custom Title
      description: Description of the notebook entry
      links:
        - http://www.google.com
        - research/extra/presentation.ppt

(NOTE 2016/03/02: the description and external link support haven't been implemented yet,
but should be shortly...)

Development
-----------

Contributing
~~~~~~~~~~~~

The project is just getting started and is changing rapidly.
`Let me know <mailto:khughitt@umd.edu>`__ if you have suggestions or
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
- Add option to automatically convert ipynb files to HTML (use runipy)
- Add option to use icons for entry links.
- Check for git revision and link to repo if on Github
- Add option to show short git commit hashes next to entries which associated
  with repos.
- Allow sorting of categories by order in settings (default), name, or
  date-modified.
- Add option to show entries in a "journal mode" with all entries displayed
  together, sorted from most recent to oldest. Category divisions can either be
  hidden entirely, or displayed as (colored) tags to the right side of the
  entry titles.
- Color output.
- Add verbose option (default on?)
    - Print out warning messages for missing images.
    - Print out warning messages for missing titles.
    - Print out message about excluded files


.. |Build Status| image:: https://travis-ci.org/khughitt/labnote.svg?branch=master
   :target: https://travis-ci.org/khughitt/labnote

