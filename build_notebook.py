#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lab-notebook

Keith Hughitt <khughitt@umd.edu>
"""
import fnmatch
import jinja2
import glob
import os
import yaml

with open('config.yaml') as fp:
    # Load config
    conf = yaml.load(fp)

    # Find matching lab notebook entries
    matches = []

    # Iterate over search paths
    for search_path in conf['search_paths']:
        # Iterate over sub-directories in each search path
        for root_dir in glob.glob(search_path):
            if not os.path.isdir(root_dir):
                continue
            for filename in os.listdir(root_dir):
                filepath = os.path.join(root_dir, filename)
                if not os.path.isfile(filepath):
                    continue
                # For each file in the top-level of a matching dir, check to
                # see if it is a valid notebook entry file
                if any(fnmatch.fnmatch(filename, p) for p in conf['include_files']):
                    matches.append(filepath)
    


