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
                 output_file, theme='default'):
        self.author = author
        self.title = title
        self.email = email
        self.date = date
        self.entries = entries
        self.output_file = output_file
        self.theme = '%s.html' % theme

        # Load Jinja2 template
        env = Environment(loader=PackageLoader('labnote', 'templates'))
        self.template = env.get_template(self.theme)

    def render(self):
        """Abstract method for rendering the notebook"""
        pass

class HTMLRenderer(Renderer):
    """HTML notebook renderer"""
    def __init__(self, author, title, email, date, entries, output_file, template):
        super().__init__(author, title, email, date, entries, output_file,
                         template)

    def render(self):
        """Renders notebook"""
        html = self.template.render(author=self.author, title=self.title,
                                    email=self.email, date=self.date, 
                                    entries=self.entries)

        print("- Generating notebook HTML")

        # Output notebook
        with open(self.output_file, 'w') as fp:
            fp.write(html)

        print("- Saving notebook to %s" % self.output_file)

        # Path to resources/ directory
        resources = resource_filename(Requirement.parse('labnote'),
                                      os.path.join('labnote', 'resources'))

        # Copy CSS and image resources to output directory 
        output_dir = os.path.dirname(self.output_file)
        resource_dir = os.path.join(output_dir, 'resources')

        if os.path.isdir(resource_dir):
            shutil.rmtree(resource_dir)

        shutil.copytree(resources, resource_dir,
                        ignore=shutil.ignore_patterns("__init__.py", 
                                                        "__pycache__"))
