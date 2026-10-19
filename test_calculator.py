"""calculator.divide 在正常输入下的单元测试。"""

import unittest

from calculator import divide


class DivideTest(unittest.TestCase):
    """覆盖常见的正常输入场景。"""

    def test_divisible_integers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_non_divisible_result(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_negative_numbers(self):
        self.assertEqual(divide(-9, 3), -3)

    def test_zero_dividend(self):
        self.assertEqual(divide(0, 5), 0)

    def test_float_operands(self):
        self.assertAlmostEqual(divide(1.5, 0.5), 3.0)

    def test_zero_divisor_raises(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_zero_divided_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(0, 0)


if __name__ == "__main__":
    unittest.main()
