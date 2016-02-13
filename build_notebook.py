#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lab-notebook

Keith Hughitt <khughitt@umd.edu>
"""
import fnmatch
import glob
import os
import yaml
from jinja2 import Environment, FileSystemLoader

def get_category(dir_name, categories, default='Other'):
    """Determines category for a given analysis"""
    for category,patterns in categories.items():
        if any(fnmatch.fnmatch(dir_name, p) for p in patterns):
            return(category)
    return(default) 

fp = open('config.yaml')

# Load config
conf = yaml.load(fp)

# Find matching lab notebook entries
categories = {}

# Iterate over search paths
for search_path in conf['search_paths']:
    # Iterate over sub-directories in each search path
    parent_dir = os.path.join(conf['root_dir'], search_path)

    for sub_dir in glob.glob(parent_dir):
        if not os.path.isdir(sub_dir):
            continue
        for filename in os.listdir(sub_dir):
            filepath = os.path.join(sub_dir, filename)
            if not os.path.isfile(filepath):
                continue
            # For each file in the top-level of a matching dir, check to
            # see if it is a valid notebook entry file
            if any(fnmatch.fnmatch(filename, p) for p in conf['include_files']):
                # determine category to use
                category = get_category(sub_dir, conf['categories'])

                # create dict representation of notebook entry
                entry = {
                    'title': filename,
                    'date': '2016/02/13',
                    'url': filepath.replace(conf['root_dir'], '')
                }
                
                # add entry to master dictionary
                if category not in categories:
                    categories[category] = []
                categories[category].append(entry)

fp.close()

## Capture our current directory
pwd = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(pwd, 'templates')
env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)

template = env.get_template('index.html')
html = template.render(author=conf['author'], title=conf['title'],
                       email=conf['email'], categories=categories)

with open('index.html', 'w') as outfile:
    outfile.write(html)


