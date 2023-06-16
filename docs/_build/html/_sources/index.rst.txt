:tocdepth: 3

Welcome to Labnote's documentation!
===================================

Overview
========

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

.. figure:: images/example_screenshot.png
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

Documentation
=============

.. toctree::
   :maxdepth: 2

   installation.rst
   configuration.rst
   features.rst
   development.rst

