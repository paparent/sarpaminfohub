from sarpaminfohub.infohub.tests.sarpam_test_case import SarpamTestCase
from itertools import islice

class TableTestCase(SarpamTestCase):
    def get_nth_value(self, iterable, n, default=None):
        return next(islice(iterable, n, None), default)
    
    def contains(self, string_to_search, sub_string):
        return string_to_search.find(sub_string) > -1

