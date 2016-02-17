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
    config_dir = os.path.expanduser("~/.config/labnote/")

    # Check for config.yaml or config.yml
    config_file = os.path.join(config_dir, 'config.yml')
    if not os.path.isfile(config_file):
        config_file = os.path.join(config_dir, 'config.yaml')

    # If user config exists, use it to overwrite defaults
    if os.path.isfile(config_file):
        with open(config_file) as fp:
            config.update(yaml.load(fp))

    return config

def get_args():
    """Parses input and returns arguments"""
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Generate HTML lab notebook.')

    parser.add_argument('-c', '--config',
                        help=('Configuration filepath. (Will use configuration' 
                              'in $HOME/.config/labnote/config.yml, if it exists.)'))
    parser.add_argument('-i', '--input-dirs', dest='input_dirs', nargs='+',
                        help=('Input directory(s) containing notebook entries.'))
    parser.add_argument('-o', '--output-dir', dest='output_dir',
                        help=('Location to output notebook HTML to.'))
    parser.add_argument('-u', '--url-prefix', dest='url_prefix',
                        help=('Prefix to add to each entry URL. (Default: "")'))

    return parser

# Default options
def _defaults():
    """Gets a dictionary of default options"""
    return {
        'author': '',
        'email':  '',
        'title': 'Lab Notebook',
        'input_dirs': None,
        'output_dir': None,
        'include_files':  ['*.html', '*.py', '*.ipynb'],
        'categories': {},
        'url_prefix': ''
    }
