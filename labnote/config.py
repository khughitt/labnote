"""
Configuration handling logic for labnote.
"""
def load_config():
    """Loads labnote configuration"""
    import os
    import yaml

    # Default configuration options
    config = _defaults()

    # Load user config file if it exists
    config_file = os.path.expanduser("~/.labnote/config.yaml")

    if os.path.isfile(config_file):
        with open(config_file) as fp:
            config.update(yaml.load(fp))

    return config

def get_args():
    """Parses input and returns arguments"""
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Generate HTML lab notebook.')

    parser.add_argument('-c', '--config',
                        help=('Input configuration filepath.'))

    return parser

# Default options
def _defaults():
    """Gets a dictionary of default options"""
    return {
        'author': '',
        'email':  '',
        'title': 'Lab Notebook',
        'root_dir': '/var/www/research',
        'include_files':  ['*.html', '*.py', '*.ipynb'],
        'search_paths': ['*'],
        'categories': {}
    }
