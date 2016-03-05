"""
Notebook test code
"""
class TestNotebook():
    def test_load_config(self, notebook):
        assert notebook.author == 'C. Darwin'
        assert notebook.email == 'cdarwin@geolsoc.org.uk'
        assert notebook.title == 'Lab Notebook'

    def test_categories(self, notebook):
        e = notebook.entries

        # Expected
        expected = {
            'categories': ['Barnacles', 'Finches', 'Other'],
            'descriptions': ['Finch research from the second voyage of HMS Beagle', 
                             '', ''],
            'images': ['images/a1417007h.jpg',
                       'images/1854_Balanidae_F339.2_figlbp12.jpg',
                       ''],
            'patterns': [['finch', 'natural-selection'], 
                         ['cirripede'], 
                         []]
        }
            
        # categories
        assert sorted(list(e.keys())) == expected['categories'] 

        # category descriptions
        descriptions = [e[cat]['description'] for cat in e]
        assert descriptions == expected['descriptions']

        # category images
        images = [e[cat]['image'] for cat in e]
        assert images == expected['images']

        # category patterns
        patterns = [e[cat]['patterns'] for cat in e]
        assert patterns == expected['patterns']

    def test_entries(self, notebook):
        e = notebook.entries

        # get a flattened list of entries
        entries = e.get_entries()

        # dict of category names and number of entries in each
        cats = {k:len(v['entries']) for k,v in notebook.entries.items()}
        assert cats == {'Barnacles': 2, 'Finches': 3, 'Other': 1}

        # check entry titles
        entry_titles = [entry.title for entry in entries]
        assert sorted(entry_titles) == [
            'Cirripede systematics analysis',
            'Comparison of cirripede morphology',
            'Finch Beak Size Analysis',
            'Molothrus parasitism',
            'Natural Selection',
            'foraging-strategies.py'
        ]
