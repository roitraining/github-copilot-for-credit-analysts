import unittest

from average import average


class AverageTests(unittest.TestCase):
    def test_average_with_normal_list(self):
        self.assertEqual(average([10, 20, 30, 40]), 25)

    def test_average_with_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            average([])


if __name__ == "__main__":
    unittest.main()
