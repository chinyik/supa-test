import unittest
from datetime import date
from date_getter import get_sorted_dates

class TestDateGetter(unittest.TestCase):

    def test_get_sorted_dates_should_contains_only_dates(self):
        result = get_sorted_dates()

        for item in result:
            self.assertIsInstance(item, date)

if __name__ == '__main__':
    unittest.main()