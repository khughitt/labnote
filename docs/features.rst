Features
--------

Supported file formats
~~~~~~~~~~~~~~~~~~~~~~

@TODO

Customizing categories
~~~~~~~~~~~~~~~~~~~~~~

@TODO

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


Themes
~~~~~~

Default theme
^^^^^^^^^^^^^

Currently Labnote ships with a single theme, creatively named "default". This
is the theme that is shown in the example screenshot. It uses the `Skeleton
<http://getskeleton.com/>`__ CSS framework to produce a simple three column
layout with notebook entries in the center and, optionally, category images on
either side of the entries.

Additional themes may be included in the future and users are welcome to 
contribute their own themes. See the development guide for more information on
creating new themes.

Customizing themes with CSS/JS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lab note provides two configuration option which allow you to specify custom
CSS or JavaScript files which should be included, regardless of which theme
you are using:

* ``user_css``
* ``user_js``

These may be included in your config.yml, or specified at run-time, and will
result in the specified files being included in the outputted HTML.

