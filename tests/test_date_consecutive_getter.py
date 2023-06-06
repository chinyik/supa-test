import unittest
from datetime import datetime
from date_consecutive_getter import get_consecutive_date_table
from prettytable import PrettyTable

class TestDateConsecutiveGetter(unittest.TestCase):

    def test_get_consecutive_getter_with_multiple_consecutive_dates(self):
        items = [
            datetime(2023, 3, 1),
            datetime(2023, 3, 2),
            datetime(2023, 3, 3),
            datetime(2023, 3, 6),
            datetime(2023, 3, 9),
            datetime(2023, 3, 10),
            datetime(2023, 3, 12),
        ]

        expected = PrettyTable(["START", "END", "LENGTH"])
        expected.add_row([datetime(2023, 3, 1), datetime(2023, 3, 3), 3])
        expected.add_row([datetime(2023, 3, 9), datetime(2023, 3, 10), 2])
        expected.add_row([datetime(2023, 3, 12), datetime(2023, 3, 12), 1])
        expected.add_row([datetime(2023, 3, 6), datetime(2023, 3, 6), 1])

        actual = get_consecutive_date_table(items)

        self.assertEqual(actual, expected.get_string())

    def test_get_consecutive_getter_with_no_consecutive_dates(self):
        items = [
            datetime(2023, 3, 1),
            datetime(2023, 3, 3),
            datetime(2023, 3, 6),
            datetime(2023, 3, 10),
            datetime(2023, 3, 15),
            datetime(2023, 3, 21),
            datetime(2023, 3, 27),
        ]

        expected = PrettyTable(["START", "END", "LENGTH"])
        expected.add_row([datetime(2023, 3, 27), datetime(2023, 3, 27), 1])
        expected.add_row([datetime(2023, 3, 21), datetime(2023, 3, 21), 1])
        expected.add_row([datetime(2023, 3, 15), datetime(2023, 3, 15), 1])
        expected.add_row([datetime(2023, 3, 10), datetime(2023, 3, 10), 1])
        expected.add_row([datetime(2023, 3, 6), datetime(2023, 3, 6), 1])
        expected.add_row([datetime(2023, 3, 3), datetime(2023, 3, 3), 1])
        expected.add_row([datetime(2023, 3, 1), datetime(2023, 3, 1), 1])

        actual = get_consecutive_date_table(items)

        self.assertEqual(actual, expected.get_string())

    def test_get_consecutive_getter_with_only_one_date(self):
        items = [
            datetime(2023, 3, 1),
        ]

        expected = PrettyTable(["START", "END", "LENGTH"])
        expected.add_row([datetime(2023, 3, 1), datetime(2023, 3, 1), 1])

        actual = get_consecutive_date_table(items)

        self.assertEqual(actual, expected.get_string())

if __name__ == '__main__':
    unittest.main()