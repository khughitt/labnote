"""
Notebook test code
"""
class TestNotebook():
    def test_category_date_sorting(self, nb1):
        e = nb1.entries

        # Expected
        expected = {
            'categories': ['Second', 'First', 'Other'],
            'descriptions': ['', '', ''],
            'images': ['', '', ''],
            'patterns': [['bar'], ['foo'], []]
        }
            
        # categories
        assert list(e.keys()) == expected['categories']

        # category descriptions
        descriptions = [e[cat].description for cat in e]
        assert descriptions == expected['descriptions']

        # category images
        images = [e[cat].image for cat in e]
        assert images == expected['images']

        # category patterns
        patterns = [e[cat].patterns for cat in e]
        assert patterns == expected['patterns']

    def test_entry_date_sorting(self, nb1):
        """Tests labnote date-sorting (default for nb1)"""
        # files were touched in alphanumeric order, so they should appear in
        # reverse-alphanumeric order
        expected_titles = {
            'First': ['c', 'b', 'a', '3', '2', '1'],
            'Other': ['misc'],
            'Second': ['two', 'three', 'one']
        }

        e = nb1.entries

        # check order of entries in each category
        for category in e:
            titles = [item.title for item in e[category]]
            assert titles == expected_titles[category]

    def test_entry_alphanum_sorting(self, nb1_alphanum):
        """Tests labnote alphanumeric sorting"""
        e = nb1_alphanum.entries

        # Sorted alphanumerically
        expected_titles = {
            'First': ['1', '2', '3', 'a', 'b', 'c'],
            'Second': ['one', 'three', 'two'],
            'Other': ['misc'],
        }

        # check order of entries in each category
        for category in e:
            titles = [item.title for item in e[category]]
            assert titles == expected_titles[category]

    def test_entry(self, nb1):
        """Checks the values for a single entry"""
        import os

        e =  nb1.entries['Second'][0]

        assert e.dir_name == 'bar'
        assert e.filename == 'two'
        assert os.path.normpath(e.filepath) == os.path.normpath('tests/notebooks/nb1/bar/two')
        assert e.title == 'two'
        assert e.url == 'tests/notebooks/nb1/bar/two'

