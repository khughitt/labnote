.. _configuration:

Configuration
=============

Overview
--------

Labnote settings can be specified either via the command-line at run-time (e.g.
``labnote -i /some/path/* -o /output/dir``), or using a `YAML
<http://yaml.org/>`__ config file, or both.

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

If that is not possible or convenient, Labnote also supports manually
specifying a projects categorization using hidden `.labnote` metafiles inside
each project directory.

The ``--print-config`` option can be used to generate an empty config file
which you can then customize to your liking, e.g.:

::

    mkdir -p $HOME/.config/labnote
    labnote --print-config > $HOME/.config/labnote/config.yml

Configuration Options
---------------------

Below is a complete list of Labnote configuration options and how they are
expected to be used.

Except for ``input_dirs`` and ``output_file``, all configuration parameters are
optional.

General options
~~~~~~~~~~~~~~~

- ``author`` Author name (string).
- ``email`` Author contact email address (string).
- ``title`` Lab notebook title (string).

Files to include
~~~~~~~~~~~~~~~~

- ``input_dirs`` List of one or more absolute or relative directory paths which
  should be scanned for files corresponding to notebook entries. Only those
  filenames which match the patterns specified in the ``include_files`` option
  described below will be added.
- ``include_files``: List of filename wildcard expressions specifying the files
  to be included in the notebook.
- ``exclude`` List of strings indicating files which should not be included in
  the notebook. If any part of a file's directory or filename matches a string
  in the ``exclude`` list, it will be skipped.
- ``external``: A dictionary containing one or more external links which should
  be included as notebook entries. Each external entry must include a ``url``
  key indicating where the entry can be accessed, and, optionally, a
  ``category``.

Example:

.. code:: yaml

    external:
    'Interactive network visualization':
        category: 'Shiny'
        url: 'http://user.shinyapps.io/network-viz'
    'Interactive time series viewer':
        category: 'Shiny'
        url: 'http://server.com:3838/time-series-viewer'

Categories
~~~~~~~~~~

- ``categories`` List of dictionaries describing how entries should be grouped.

For each category, a list of one or more patterns should be specified. When
entries are added to the notebook, the entry directory and filenames will be
compared against the category patterns, and the entry will be assigned to
the first category that it matches, or else default to an "Other" category.

In addition to the entry search patterns, each category may also include an
image and description field, which may be used by themes during the notebook
HTML generation.

 Example:

.. code:: yaml

    categories:
      'Network Analysis': ['network', 'edge-betweenness', 'topology']
      'Differential Expression': 
          patterns: ['diffexpr', 'dea']
          image: 'resources/user/img/maplot.jpg'
      'Regulatory Element Detection': 
          patterns: ['motif', 'regulatory-elem', 'random-forest']
          image: '2015/15-random-forest-gene-reg/output/motif_example.png'

In the above example, for the first category, only the search patterns to be
used for notebook entry membership determination are specified. The next two
categories also specify and image to use.

Appearance
~~~~~~~~~~

- ``theme`` String indicating the Labnote theme to be used for the rendered
  notebook. Currently there is only one theme provided: "default".
- ``sort_categories_by_date`` Boolean indicating whether the categories should
  be sorted by the date of the most recent entry within each category.
  (default: true)
- ``sort_entries_by_date``: Boolean indicating whether the entries within each
  category should be sorted by date. If true, entries within each category will
  appear in decreasing order by date last modified, otherwise they will be
  sorted alphanumerically. (default: false).

Output
~~~~~~

- ``output_file``: Filepath where notebook should be written. Notebook resources
(CSS, images, etc.) will also be copied to the directory containing the
indicated output file.
- ``url_prefix``: A string prefix to be prepended to each entry URL. This can be
used, for example, to point to a remotely-hosted version of the notebook.
- ``user_css``: Custom CSS file to include in the output HTML (string).
- ``user_js``: Custom JavaScript file to include in the output HTML (string).

