"""
Labnote base Entry class.
"""
import datetime
import os
import fnmatch

class BaseEntry(object):
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
        self.title = self._get_entry_title(),
        self.date = self._get_date_modified(),
        self.url = os.path.join(url_prefix, filepath.replace(output_dir, ''))

        # determine category to use
        self.category = self._get_category(categories)

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

    def _get_entry_title(self):
        """Determine title to use for the specified notebook entry"""
        from bs4 import BeautifulSoup

        # file extension
        ext = os.path.splitext(self.filepath)[-1].lower()

        # TODO: extend to support ipynb parsing; 
        # split into separate functions

        print(" * Adding %s" % self.filepath)

        # HTML
        if ext == '.html':
            with open(self.filepath) as fp:
                title = BeautifulSoup(fp, 'html.parser').title.string
            if title is not None:
                return title
        elif ext == '.py':
            return self._parse_python_title()

        # Default (filename)
        return self.filename 

    def _parse_python_title(self):
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

