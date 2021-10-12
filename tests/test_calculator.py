import unittest

from calculator.calculator import Calculator


class Test(unittest.TestCase):
    def test_calculator(self):
        test_map = (
            {
                'input_values': '2 1 + 3 *',
                'result_values': 9
            },

            {
                'input_values': '7 2 + 4 * 2 +',
                'result_values': 38
            },
        )
        for case in test_map:
            input_values, result_values = case.values()
            input_values = input_values.split(' ')
            with self.subTest(result_values):
                calculator = Calculator(input_values)
                result = calculator.get_result()
                self.assertEqual(result_values, result)
