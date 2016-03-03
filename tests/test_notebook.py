"""
Notebook test code
"""
class TestNotebook():
    def test_load_config(self, notebook):
        assert notebook.author == 'C. Darwin'
        assert notebook.email == 'cdarwin@geolsoc.org.uk'
        assert notebook.title == 'Lab Notebook'

        # check categories
        assert dict(notebook.categories) == {
            'Barnacles': {
                'patterns': ['cirripede'],
                'description': '',
                'image': ''
            },
            'Finches': {
                'patterns': ['finch', 'natural-selection'],
                'description': "Finch research from the second voyage of HMS Beagle",
                'image': ''
            }
        }

    def test_entries(self, notebook):
        # get a flattened list of entries
        entries = [i[x] for i in notebook.entries.values() for x in range(len(i))]

        entry_categories = [e.category for e in entries]
        assert sorted(entry_categories) == ['Barnacles', 'Barnacles', 
                                            'Finches', 'Finches', 'Finches',
                                            'Other']

        entry_titles = [e.title for e in entries]
        assert sorted(entry_titles) == [
            'Cirripede systematics analysis',
            'Comparison of cirripede morphology',
            'Finch Beak Size Analysis',
            'Molothrus parasitism',
            'Natural Selection',
            'foraging-strategies.py'
        ]
