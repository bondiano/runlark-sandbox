import unittest

from stats import variance


class VarianceTest(unittest.TestCase):
    def test_population_variance(self):
        self.assertEqual(variance([1, 2, 3, 4]), 1.25)

    def test_empty_is_refused(self):
        with self.assertRaises(ValueError):
            variance([])
