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

        print(" * Scanning for notebook entries in %s" % parent_dir)

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
        if any(fnmatch.fnmatch(dir_name, p) for p in patterns):
            return(category)
    return(default) 

def create_entry(title, filepath, root_dir):
    """Create a lab notebook entry dict"""
    return {
        'title': title,
        'date': '2016/02/13',
        'url': filepath.replace(root_dir, '')
    }
