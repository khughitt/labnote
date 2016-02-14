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
    config_file = os.path.expanduser("~/.config/labnote/config.yml")

    if os.path.isfile(config_file):
        with open(config_file) as fp:
            config.update(yaml.load(fp))

    return config

def get_args():
    """Parses input and returns arguments"""
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Generate HTML lab notebook.')

    parser.add_argument('-c', '--config',
                        help=('Input configuration filepath. (Default: ' 
                              '$HOME/.config/labnote/config.yml if it exists.)'))
    parser.add_argument('-d', '--input-dir', dest='input_dir',
                        help=('Input directory containing notebook entries. '
                              '(Default: /var/www/research)'))
    parser.add_argument('-o', '--output-dir', dest='output_dir',
                        help=('Location to output notebook HTML to. '
                              '(Default: /var/www/research)'))

    return parser

# Default options
def _defaults():
    """Gets a dictionary of default options"""
    return {
        'author': '',
        'email':  '',
        'title': 'Lab Notebook',
        'input_dir': '/var/www/research',
        'output_dir': '/var/www/research',
        'include_files':  ['*.html', '*.py', '*.ipynb'],
        'search_paths': ['*'],
        'categories': {}
    }
