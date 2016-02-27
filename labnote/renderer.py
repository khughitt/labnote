"""
Notebook rendering classes

Currently, only an HTMLRenderer class is available. Eventually this could be
extended to include something like a MarkdownRenderer class for hosting on
Github, etc.
"""
import os
import shutil
from jinja2 import Environment, PackageLoader
from pkg_resources import resource_filename, Requirement

class Renderer(object):
    """Base notebook Renderer class"""
    def __init__(self, author, title, email, date, entries,
                 output_dir, theme='default'):
        self.author = author
        self.title = title
        self.email = email
        self.date = date
        self.entries = entries
        self.output_dir = output_dir
        self.theme = '%s.html' % theme

        # Load Jinja2 template
        env = Environment(loader=PackageLoader('labnote', 'templates'))
        self.template = env.get_template(self.theme)

    def render(self):
        """Abstract method for rendering the notebook"""
        pass

class HTMLRenderer(Renderer):
    """HTML notebook renderer"""
    def __init__(self, author, title, email, date, entries, output_dir, template):
        super().__init__(author, title, email, date, entries, output_dir,
                         template)

    def render(self):
        """Renders notebook"""
        html = self.template.render(author=self.author, title=self.title,
                                    email=self.email, date=self.date, 
                                    entries=self.entries)

        print("- Generating notebook HTML")

        # Output notebook
        outfile = os.path.join(self.output_dir, 'index.html')
        with open(outfile, 'w') as fp:
            fp.write(html)

        print("- Saving notebook to %s" % self.output_dir)

        # Path to resources/ directory
        resources = resource_filename(Requirement.parse('labnote'),
                                      os.path.join('labnote', 'resources'))

        # Copy CSS and image resources to output directory if it does not already
        # exist.
        resource_dir = os.path.join(self.output_dir, 'resources')

        if not os.path.isdir(resource_dir):
            shutil.copytree(resources, resource_dir,
                            ignore=shutil.ignore_patterns("__init__.py", 
                                                          "__pycache__"))
