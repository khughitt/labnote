"""
Notebook test code
"""
class TestNotebook():
    def test_load_config(self, notebook):
        assert notebook.author == 'C. Darwin'
