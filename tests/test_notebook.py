"""
Notebook test code
"""
class TestNotebook():
    def test_categories(self, nb1):
        e = nb1.entries

        # Expected
        expected = {
            'categories': ['First', 'Second', 'Other'],
            'descriptions': ['', '', ''],
            'images': ['', '', ''],
            'patterns': [['foo'], ['bar'], []]
        }
            
        # categories
        assert list(e.keys()) == expected['categories']

        # category descriptions
        descriptions = [e[cat]['description'] for cat in e]
        assert descriptions == expected['descriptions']

        # category images
        images = [e[cat]['image'] for cat in e]
        assert images == expected['images']

        # category patterns
        patterns = [e[cat]['patterns'] for cat in e]
        assert patterns == expected['patterns']

    def test_entries(self, nb1):
        e = nb1.entries

        # Sorted alphanumerically
        expected_titles = {
            'First': ['1', '2', '3', 'a', 'b', 'c'],
            'Second': ['one', 'three', 'two'],
            'Other': ['misc'],
        }

        # check order of entries in each category
        for category in e:
            titles = [item.title for item in e[category]['entries']]
            assert titles == expected_titles[category]

