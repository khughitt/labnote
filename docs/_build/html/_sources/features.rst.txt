.. _features:

Features
--------

Supported file formats
~~~~~~~~~~~~~~~~~~~~~~

While labnote is capable of including arbitrary file types, there are several
file types which Labnote natively recognizes and is able to provide extended
functionality for such as automatic title determination, and (in the future),
real-time conversion. For each of these, Labnote will attempt to automatically choose an appropriate
title.

HTML
''''

For HTML files, the `<title>` element will be used.

Python
''''''

For Python files, the first line of a file docstring will be used as a title.

IPython Notebook
''''''''''''''''

For IPython (Jupyter) notebooks, a custom `metadata` field will be used if
found. This can be added by editing the JSON source for the notebook, and
adding a ``labnote`` section to the ``metadata`` JSON block:

.. code:: json

"metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "labnote": {
   "title": "Notebook title"
  },

Recent versions of Jupyter notebook include an a built-in metadata editor,
although any plain-text editor such as Vim will also work fine.

Customizing categories
~~~~~~~~~~~~~~~~~~~~~~

Categories are used by Labnote to group related notebook entries. Each category
may be assigned an image and description which may be used by Labnote themes to
provide a custom appearance for each section of the notebook. See the
:ref:`configuration` section on categories for more information.

.. figure:: images/category_example.png
   :alt: Example of a notebook category which includes an image. 

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
'''''''''''''

Currently Labnote ships with a single theme, creatively named "default". This
is the theme that is shown in the example screenshot. It uses the `Skeleton
<http://getskeleton.com/>`__ CSS framework to produce a simple three column
layout with notebook entries in the center and, optionally, category images on
either side of the entries.

Additional themes may be included in the future and users are welcome to 
contribute their own themes. See the development guide for more information on
creating new themes.

Customizing themes with CSS/JS
''''''''''''''''''''''''''''''

Lab note provides two configuration option which allow you to specify custom
CSS or JavaScript files which should be included, regardless of which theme
you are using:

* ``user_css``
* ``user_js``

These may be included in your config.yml, or specified at run-time, and will
result in the specified files being included in the outputted HTML.

For example, if you wanted to change the font used for the category headers,
you could create a file named 'custom.css' containing:

.. code:: css

    .category-header {
        font-family: 'helvetica', 'sans-serif';
    }

Edit your config so that `user_css` provides a path to `custom.css`, relative
to where your notebook output is saved, and regenerate the notebook. Your
category headers should now use the Helvetica font instead of the cursive font
currently used.

