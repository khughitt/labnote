Configuration
-------------

Labnote settings are controlled can be specified either via the
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
