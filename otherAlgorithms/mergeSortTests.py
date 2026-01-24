import unittest
from mergeSort import merge_sort


class MergeSortTests(unittest.TestCase):
    def test_merge_sort(self):
        input = [7, 2, 5, 4, 1, 6, 0, 3, 9]
        actual = merge_sort(input)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 9]
        self.assertEquals(
            actual,
            expected,
            "List of numbers should be sorted."
        )


if __name__ == '__main__':
    unittest.main()
