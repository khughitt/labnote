"""
Labnote Entry class definitions.
"""
import os
from datetime import datetime
from urllib.parse import urljoin
from urllib.request import pathname2url

class Entry(object):
    """Base notebook Entry class"""
    def __init__(self, **kwargs):
        """Creates a lab notebook Entry object instance.
    
        Parses the relevant file corresponding to the notebook entry and
        attempts to determine an appropriate title to use for the entry, the
        date the analysis was last modified, etc. and stores all of the
        relevant information as a Entry instance.
        
        Args:
            filepath: Path to the file for which the lab notebook entry is
                being created.
            output_dir: The notebook HTML output directory. This will be
                removed from the final path in order to generate a relative URL.
            url_prefix: An optional URL prefix to be preprended to the entry.
        """
        self.filepath = kwargs['filepath']
        self.filename = os.path.basename(self.filepath)
        self.dir_name = os.path.basename(os.path.dirname(self.filepath))
        self.date = datetime.fromtimestamp(os.path.getmtime(self.filepath))
        self.url = pathname2url(urljoin(kwargs['url_prefix'], 
                                                self.filepath.replace(kwargs['output_dir'] + "/", '')))

        # set title
        if 'title' in kwargs:
            self.title = kwargs['title']
        else:
            self.title = self._get_entry_title()

    def __lt__(self, other):
        """Allow entries to be sorted by date"""
        return self.date < other.date

    @staticmethod
    def factory(**kwargs):
        """Static method used to create specific entry instances"""
        # Local entry
        if 'filepath' in kwargs:
            print(" * Adding %s" % kwargs['filepath'])

            # Determine file extension
            ext = os.path.splitext(kwargs['filepath'])[-1].lower()

            # HTML files
            if ext == '.html':
                return HTMLEntry(**kwargs)
            elif ext == '.py':
                # Python scripts
                return PythonEntry(**kwargs)
            elif ext == '.ipynb':
                # IPython notebook
                return JupyterEntry(**kwargs)
            else:
                # Everything else
                return GenericEntry(**kwargs)
        elif 'url' in kwargs:
            # External entry
            return ExternalEntry(**kwargs)

class HTMLEntry(Entry):
    """HTML lab notebook entry"""
    def __init__(self, **kwargs):
        """Creates a new HTMLEntry instance."""
        super().__init__(**kwargs)

    def _get_entry_title(self):
        """Determine title to use for the specified notebook entry"""
        from bs4 import BeautifulSoup

        with open(self.filepath) as fp:
            soup = BeautifulSoup(fp, 'html.parser')

            # If no title is found, use filename instead
            # TODO: print warning?
            if soup.title is None or soup.title.string is None:
                return self.filename
            else:
                return soup.title.string

class GenericEntry(Entry):
    """Generic lab notebook entry"""
    def __init__(self, **kwargs):
        """Creates a new GenericEntry instance."""
        super().__init__(**kwargs)

    def _get_entry_title(self):
        """Determine title to use for the specified notebook entry"""
        return self.filename 

class PythonEntry(Entry):
    """Python lab notebook entry"""
    def __init__(self, **kwargs):
        """Creates a new PythonEntry instance."""
        super().__init__(**kwargs)

    def _get_entry_title(self):
        """Attempts to extract the first line of a python file docstring to use
        as a notebook entry title"""
        import ast

        with open(self.filepath) as fp:
            # load python code
            try:
                mod = ast.parse(''.join(fp))
            except SyntaxError:
                # Non-standard Python code (e.g. Snakemake)
                return self.filename

        # grab docstring if it exists
        docstring = ast.get_docstring(mod)

        if docstring is not None:
            # extract first line from docstring
            return docstring.split('\n')[0]
        else:
            return self.filename

class JupyterEntry(Entry):
    """Jupyter/IPython notebook entry"""
    def __init__(self, **kwargs):
        """Creates a new JupyterEntry instance."""
        super().__init__(**kwargs)

    def _get_entry_title(self):
        """Determine title to use for the specified notebook entry"""
        import json

        with open(self.filepath) as fp:
            contents = json.load(fp)
            metadata = contents['metadata']

            # If no title is found, use filename
            if 'labnote' in metadata and 'title' in metadata['labnote']:
                return metadata['labnote']['title']
            else:
                return self.filename.replace('.ipynb', '')

class ExternalEntry(object):
    """External lab notebook entry
    
    NOTE: This class currently does not sub-class from the base Entry class.
    Eventually it may be helpful to create create a middle layer with
    "LocalEntry" and "ExternalEntry" or "RemoteEntry", from which each of
    the subclasses can inherit from.

    Another possibility would be to make the local or remote features
    decorators of each of the Entry subclasses.
    """
    def __init__(self, **kwargs):
        """Creates a new ExternalEntry instance."""
        from urllib import request
        from urllib.parse import urlsplit
        from urllib.request import HTTPError,URLError

        # Required variables - title & url
        self.title = kwargs['title']
        self.url   = kwargs['url']

        # Parse filename and directory from URL
        PATH_IDX = 2

        url_parts = urlsplit(self.url)
        url_path = url_parts[PATH_IDX]

        self.filename = os.path.basename(url_path)
        self.dir_name = os.path.basename(os.path.dirname(url_path))

        # Attempt to determine the date last modified
        try:
            conn = request.urlopen(self.url)

            if 'last-modified' in conn.headers:
                import email.utils as eut
                self.date = datetime(*eut.parsedate(conn.headers['last-modified'])[:6])
            else:
                # If date not specified, default to unix timestamp 0
                self.date = datetime.fromtimestamp(0)
        except (HTTPError, URLError, ConnectionRefusedError):
            # If URL is not accessible, default to unix timestamp 0
            self.date = datetime.fromtimestamp(0)

    def _get_entry_title(self):
        """Determine title to use for the specified notebook entry"""
        return self.title

    def __lt__(self, other):
        """Allow entries to be sorted by date"""
        return self.date < other.date

