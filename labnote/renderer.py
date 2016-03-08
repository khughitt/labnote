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
                 output_file, user_css, user_js, theme='default'):
        self.author = author
        self.title = title
        self.email = email
        self.date = date
        self.entries = entries
        self.output_file = output_file
        self.user_css = user_css
        self.user_js = user_js
        self.theme = '%s.html' % theme

        # Load Jinja2 template
        env = Environment(loader=PackageLoader('labnote', 'templates'))
        self.template = env.get_template(self.theme)

    def render(self):
        """Abstract method for rendering the notebook"""
        pass

class HTMLRenderer(Renderer):
    """HTML notebook renderer"""
    def __init__(self, author, title, email, date, entries, output_file,
                 user_css, user_js, template):
        super().__init__(author, title, email, date, entries, output_file,
                         user_css, user_js, template)

    def render(self):
        """Renders notebook"""
        html = self.template.render(author=self.author, title=self.title,
                                    email=self.email, date=self.date, 
                                    user_css=self.user_css,
                                    user_js=self.user_js,
                                    entries=self.entries)

        print("- Generating notebook HTML")

        # Output notebook
        with open(self.output_file, 'w') as fp:
            fp.write(html)

        print("- Saving notebook to %s" % self.output_file)

        # Path to resources/ directory
        resources = resource_filename(Requirement.parse('labnote'),
                                      os.path.join('labnote', 'resources'))

        img_resources = os.path.join(resources, 'img')
        css_resources = os.path.join(resources, 'css')

        # Copy CSS and image resources to output directory 
        output_base = os.path.join(os.path.dirname(self.output_file),
                                   'resources')
        output_img = os.path.join(output_base, 'img')
        output_css = os.path.join(output_base, 'css')

        # Remove existing img/ and css/ directories
        for x in [output_img, output_css]:
            if os.path.isdir(x):
                shutil.rmtree(x)

        ignore_pattern = shutil.ignore_patterns("__init__.py", "__pycache__")

        shutil.copytree(img_resources, output_img, ignore=ignore_pattern)
        shutil.copytree(css_resources, output_css, ignore=ignore_pattern)

