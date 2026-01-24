import unittest
from EditDistanceCalculator import EditDistanceCalculator


class EditDistanceCalculatorTests(unittest.TestCase):
    def test_get_distance(self):
        text1 = "intention"
        text2 = "execution"
        calculator = EditDistanceCalculator(text1, text2)

        actual = calculator.get_distance()

        expected = 5
        self.assertEquals(
            actual,
            expected,
            "The edit distance is expected to be 5.")


if __name__ == '__main__':
    unittest.main()
