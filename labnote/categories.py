"""
CategoryManager class definition
"""
import fnmatch
from collections import OrderedDict
from datetime import datetime

class CategoryManager(OrderedDict):
    def __init__(self, categories):
        # If passed a list of tuples, covert to OrderedList first
        # This occurs after the object has been sorted.
        if isinstance(categories, list):
            categories = OrderedDict(categories)

        # If no categories were specifed in config, add "Other"
        if len(categories) == 0:
            categories['Other'] = Category('Other', [])
        else: 
            # If this is the first time CategoryManager is being created, we
            # need to initialize the Category instances from the relevant
            # settings; otherwise (e.g. after sorting), we can simply call the
            # parent constructor right away.
            key = list(categories.keys())[0]

            if not isinstance(categories[key], Category):

                # Extend category metadata with defaults
                for name,settings in categories.items():
                    # Dict of category metadata
                    if isinstance(settings, dict):
                        patterns = settings['patterns']
                        kwargs = settings
                        del kwargs['patterns']
                    else:
                        patterns = settings
                        kwargs = {}

                    # check to make sure patterns isn't a single string
                    if isinstance(patterns, str):
                        patterns = [patterns]

                    categories[name] = Category(name, patterns, **kwargs)

                # Add blank "Other" category
                if 'Other' not in categories.keys():
                    categories['Other'] = Category('Other', [])

        super().__init__(categories)

    def _get_category(self, entry, default='Other'):
        """Determines category for a given analysis"""
        for name,category in self.items():
            if any(fnmatch.fnmatch(entry.url, ("*%s*" % p)) for p in
                    category.patterns):
                return(name)
        return(default) 

    def add_entry(self, entry, category=None):
        """Adds a single entry to the CategoryManager"""
        if category is None:
            # if no category is specified, check to see if entry matches
            # any of the known category search patterns
            category = self._get_category(entry)
        elif category not in self:
            # for external entries, category may not yet exist
            self[category] = Category(category, [])

        self[category].append(entry)

    def get_entries(self):
        """Returns a flattened list of all entries"""
        entries = []
        for category in self.values():
            entries = entries + category
        return(entries)

    def sort_entries(self, by_date):
        """Sorts entries within each category"""
        # Sort by title or date
        for category in self:
            if by_date:
                self[category].sort(reverse=True)
            else:
                self[category].sort(key=lambda x: str(getattr(x, 'title')).lower())

        #for category in self:
        #    self[category] = Category(category, sorted(
        #        self[category],
        #        key=lambda x: str(getattr(x, sort_key)).lower(),
        #        reverse=by_date
        #    ))

class Category(list):
    """Notebook Category class definition"""
    def __init__(self, name, patterns, description='', image=''): 
        """Creates a new Category instance"""
        self.name = name
        self.patterns = patterns
        self.description = description
        self.image = image
        self.last_modified = datetime.fromtimestamp(0)
        super().__init__()

    def __repr__(self):
        return "Category([%s])" % (", ".join(x.title for x in self))

    def __lt__(self, other):
        """Allow sorting of categories by last modified date"""
        return self.last_modified < other.self_modified

    def append(self, entry):
        super().append(entry)

        if self.last_modified < entry.date:
            self.last_modified = entry.date


