Overview
--------


Installation
------------

### Requirements

To use labnote, you must have a recent version of Python ([Python 3 (3.3+)](https://www.python.org/))
available on your machine.

Additionally, labnote requires the following Python libraries:

- [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/)
- [Jinja2](http://jinja.pocoo.org/docs/dev/)
- [PyYAML](http://pyyaml.org/)

If you are using pip to install labnote, all of the required depedencies should
be automatically installed for you.

### Installing labnote

To install labnote using [pip](https://docs.python.org/3.5/installing/index.html), run:

```
pip install https://github.com/khughitt/labnote/archive/master.zip
```

### Testing installation

To generate the example notebook, cd to the labnote source directory and run:

```
labnote -c example/example.config.yml -i example/research/*/* -o example/
```

### Automating notebook generation

Configuration
-------------

### Notebook configuration


### Customizing individual entries

Development
-----------

### Contributing


### TODO

- Update README.md
- Update example configuration
- Add a working example to examples directory
- Add option to print default config.yml
- Check for git revision and link to repo if on Github
- Add support for customizing display of entries using .entry.yml files for a
  given directory:
    - All specifying one or more entries to include for the directory
    - For each entry, let user specify filename, title, description, etc.
    - Allow for optional thumbnail to be specified.
    - Allow links to external files and URLs to be included (e.g.
      presentations, papers, etc.)


