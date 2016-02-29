"""
CategoryManager class definition
"""
from collections import OrderedDict

class CategoryManager(OrderedDict):
    def __init__(self, categories):
        # Extend category metadata with defaults
        defaults = self._get_defaults()

        for k,v in categories.items():
            category = defaults.copy()
            # Dict of category metadata
            if isinstance(v, dict):
                category.update(v)
            elif isinstance(v, list):
                # List of category patterns
                category['patterns'] = v

            categories[k] = category

        super().__init__(categories)

    def _get_defaults(self):
        """Gets default category metadata"""
        return {
            'patterns': [],
            'description': "",
            'image': ""
        }
