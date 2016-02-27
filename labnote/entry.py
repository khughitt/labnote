"""
Labnote base Entry class.
"""
import datetime
import fnmatch
import os

class Entry(object):
    """Base notebook Entry class"""
    def __init__(self, filepath, output_dir, categories, url_prefix):
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
            categories: Dictionary mapping from notebook category names to a
                list of search expressions corresponding to category
                membership.
            url_prefix: An optional URL prefix to be preprended to the entry.
        """
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.dir_name = os.path.basename(os.path.dirname(filepath))
        self.title = self._get_entry_title()
        self.date = self._get_date_modified()
        self.url = os.path.join(url_prefix, filepath.replace(output_dir, ''))

        # determine category to use
        self.category = self._get_category(categories)

    @staticmethod
    def factory(filepath, output_dir, categories, url_prefix):
        """Static method used to create specific entry instances"""
        print(" * Adding %s" % filepath)

        # Determine file extension
        ext = os.path.splitext(filepath)[-1].lower()

        # HTML files
        if ext == '.html':
            return HTMLEntry(filepath, output_dir, categories, url_prefix)
        elif ext == '.py':
            # Python scripts
            return PythonEntry(filepath, output_dir, categories, url_prefix)
        else:
            # Everything else
            return GenericEntry(filepath, output_dir, categories, url_prefix)

    def _get_category(self, categories, default='Other'):
        """Determines category for a given analysis"""
        for category,patterns in categories.items():
            if any(fnmatch.fnmatch(self.dir_name, ("*%s*" % p)) for p in patterns):
                return(category)
        return(default) 

    def _get_date_modified(self):
        """Determines the date that the file was last modified"""
        mtime = os.path.getmtime(self.filepath)
        return datetime.datetime.fromtimestamp(mtime).strftime('%Y/%m/%d')

class HTMLEntry(Entry):
    """HTML lab notebook entry"""
    def __init__(self, filepath, output_dir, categories, url_prefix):
        """Creates a new HTMLEntry instance."""
        super().__init__(filepath, output_dir, categories, url_prefix)

    def _get_entry_title(self):
        """Determine title to use for the specified notebook entry"""
        from bs4 import BeautifulSoup

        with open(self.filepath) as fp:
            title = BeautifulSoup(fp, 'html.parser').title.string
            return title if title is not None else self.filename

class GenericEntry(Entry):
    """Generic lab notebook entry"""
    def __init__(self, filepath, output_dir, categories, url_prefix):
        """Creates a new GenericEntry instance."""
        super().__init__(filepath, output_dir, categories, url_prefix)

    def _get_entry_title(self):
        """Determine title to use for the specified notebook entry"""
        return self.filename 

class PythonEntry(Entry):
    """Python lab notebook entry"""
    def __init__(self, filepath, output_dir, categories, url_prefix):
        """Creates a new PythonEntry instance."""
        super().__init__(filepath, output_dir, categories, url_prefix)

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


