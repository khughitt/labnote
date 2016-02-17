"""
Configuration handling logic for labnote.
"""
import yaml
from collections import OrderedDict

def load_config(args):
    """Loads labnote configuration"""
    import os
    import sys

    # Default configuration options
    config = _defaults()

    # If user specified a configuration filepath in the command, use that path
    if 'config' in args:
        if not os.path.isfile(args['config']):
            print("Invalid configuration path specified: %s" % args['config'])
            sys.exit()

        print("- Using configuration: %s" % args['config'])

        # Load config specified from run arguments
        with open(args['config']) as fp:
            config.update(ordered_load(fp))
    else:
        # Otherwise, load user config file if it exists
        config_dir = os.path.expanduser("~/.config/labnote/")

        # Check for config.yaml or config.yml
        config_file = os.path.join(config_dir, 'config.yml')
        if not os.path.isfile(config_file):
            config_file = os.path.join(config_dir, 'config.yaml')

        # If user config exists, use it to overwrite defaults
        if os.path.isfile(config_file):
            print("- Using configuration: %s" % config_file)
            with open(config_file) as fp:
                config.update(ordered_load(fp))

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
    from collections import OrderedDict

    return {
        'author': '',
        'categories': OrderedDict(),
        'email':  '',
        'include_files':  ['*.html', '*.py', '*.ipynb'],
        'input_dirs': None,
        'output_dir': None,
        'sort_categories_by_date': True,
        'title': 'Lab Notebook',
        'url_prefix': ''
    }

def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    """
    Order-preserving YAML parser

    Creates a python representation of a YAML file in the usual manner, except
    that dictionaries are stored as OrderedDict instances, preserving the order
    in which they appear in the YAML file.

    Source: http://stackoverflow.com/a/21912744/554531

    Args:
        stream: The YAML source stream
        Loader: Base YAML loader class (default: yaml.Loader)
        object_pairs_hook: Class to use for storing dicts. (default:
        OrderedDict)
    Returns:
        An OrderedDict or similar instance representation of the input YAML.
    """

    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

