def find_valid_files(root_dir, search_paths, include_files):
    """Search specified locations for files that corresponding to lab notebook
       entries"""
    import fnmatch
    import glob
    import os

    filepaths = []

    for search_path in search_paths:
        # Iterate over sub-directories in each search path
        parent_dir = os.path.join(root_dir, search_path)

        print("- Scanning for notebook entries in %s" % parent_dir)

        for sub_dir in glob.glob(parent_dir):
            if not os.path.isdir(sub_dir):
                continue
            for filename in os.listdir(sub_dir):
                filepath = os.path.join(sub_dir, filename)
                if not os.path.isfile(filepath):
                    continue
                # For each file in the top-level of a matching dir, check to
                # see if it is a valid notebook entry file
                if any(fnmatch.fnmatch(filename, pattern) for 
                        pattern in include_files):
                    filepaths.append(filepath)

    return filepaths

def get_category(dir_name, categories, default='Other'):
    """Determines category for a given analysis"""
    import fnmatch

    for category,patterns in categories.items():
        if any(fnmatch.fnmatch(dir_name, ("*%s*" % p)) for p in patterns):
            return(category)
    return(default) 

def get_date_modified(filepath):
    """Determines the date that the file was last modified"""
    import datetime
    import os

    mtime = os.path.getmtime(filepath)
    return datetime.datetime.fromtimestamp(mtime).strftime('%Y/%m/%d')

def get_entry_title(filepath):
    """Determine title to use for the specified notebook entry"""
    import os
    from bs4 import BeautifulSoup

    # file extension
    ext = os.path.splitext(filepath)[-1].lower()

    # TODO: extend to support ipynb parsing; 
    # split into separate functions

    print(" * Adding %s" % filepath)

    # HTML
    if ext == '.html':
        with open(filepath) as fp:
            title = BeautifulSoup(fp, 'html.parser').title.string
        if title is not None:
            return title
    elif ext == '.py':
        return parse_python_title(filepath)

    # Default (filename)
    return os.path.basename(filepath)

def parse_python_title(filepath):
    """Attempts to extract the first line of a python file docstring to use as
    a notebook entry title"""
    import ast
    import os

    with open(filepath) as fp:
        # load python code
        try:
            mod = ast.parse(''.join(fp))
        except SyntaxError:
            # Non-standard Python code (e.g. Snakemake)
            return os.path.basename(filepath)

        # grab docstring if it exists
        docstring = ast.get_docstring(mod)

        if docstring is not None:
            # extract first line from docstring
            return docstring.split('\n')[0]
        else:
            return os.path.basename(filepath)

def create_entry(filepath, root_dir, url_prefix):
    """Creates a lab notebook entry dictionary.
   
    Parses the relevant file corresponding to the notebook entry and attempts
    to determine an appropriate title to use for the entry, the date the
    analysis was last modified, etc. and stores all of the relevant information
    as a dict instance.
    
    Args:
        filepath: Path to the file for which the lab notebook entry is being
            created.
        root_dir: The root directory from which the file was found. This is
            removed from the final path in order to generate a relative URL.
        url_prefix: An optional URL prefix to be preprended to the entry.

    Returns:
        A dict containing the relative metadata and filepaths corresponding to
        a single lab notebook entry.
    """
    import os

    return {
        'title': get_entry_title(filepath),
        'date': get_date_modified(filepath),
        'url': os.path.join(url_prefix, filepath.replace(root_dir, ''))
    }
