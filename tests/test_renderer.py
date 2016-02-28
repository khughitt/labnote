"""
NotebookRenderer test code
"""
import os

class TestNotebook():
    def test_notebook_render(self, notebook):
        # Render notebook to HTML and check for output file
        notebook.render()
        assert os.path.exists(notebook.output_file)

