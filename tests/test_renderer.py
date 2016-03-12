"""
NotebookRenderer test code
"""
import os

class TestNotebook():
    def test_notebook_render(self, nb1):
        # Render notebook to HTML and check for output file
        nb1.render()
        assert os.path.exists(nb1.output_file)

