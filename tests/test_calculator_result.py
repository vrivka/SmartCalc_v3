import unittest
import calc_model

from tests.test_utils import add_keys_to_calc_expression


class CalculatorResultTest(unittest.TestCase):
    def setUp(self):
        self.calc_model = calc_model.CalculatorModel()
        return super().setUp()

    def _check(self, expression, expected_expression, expected_result):
        add_keys_to_calc_expression(self.calc_model, *expression)
        self.assertEqual(self.calc_model.get_expression_string(), expected_expression)
        self.calc_model.result()
        self.assertEqual(self.calc_model.get_expression_string(), expected_result)

    def test_plus_operator(self):
        # Integer tests
        self._check(['4', '2', '+', '2', '1'], '42 + 21', '63')
        self._check([ '4', '2', 'negate', '+', '2', '1'], '-42 + 21', '-21')
        self._check(['4', '2', '+', '2', '1', 'negate'], '42 + -21', '21')
        self._check(['4', '2', 'negate', '+', '2', '1', 'negate'], '-42 + -21', '-63')

        # Float tests
        self._check(['4', '.', '2', '+', '2', '.', '1'], '4.2 + 2.1', '6.3')
        self._check(['4', '.', '2', 'negate', '+', '2', '.', '1'], '-4.2 + 2.1', '-2.1')
        self._check(['4', '.', '2', '+', '2', '.', '1', 'negate'], '4.2 + -2.1', '2.1')
        self._check(['4', '.', '2', 'negate', '+', '2', '.', '1', 'negate'], '-4.2 + -2.1', '-6.3')

        # Exponent tests
        self._check(['4', 'exp', '2', '2', '+', '2', 'exp', '1', '1'],
                    '4e22 + 2e11', '4.00000000002e22')
        self._check(['4', 'negate', 'exp', '2', '2', '+', '2', 'exp', '1', '1'],
                    '-4e22 + 2e11', '-3.99999999998e22')
        self._check(['4', 'exp', '2', '2', '+', '2', 'negate', 'exp', '1', '1'],
                    '4e22 + -2e11', '3.99999999998e22')
        self._check(['4', 'negate', 'exp', '2', '2', '+', '2', 'negate', 'exp', '1', '1'],
                    '-4e22 + -2e11', '-4.00000000002e22')
        self._check(['4', 'exp', '2', '2', 'negate', '+', '2', 'exp', '1', '1', 'negate'],
                    '4e-22 + 2e-11', '2.00000000004e-11')
        self._check(['4', 'negate', 'exp', '2', '2', 'negate', '+', '2', 'exp', '1', '1', 'negate'],
                    '-4e-22 + 2e-11', '1.99999999996e-11')
        self._check(['4', 'exp', '2', '2', 'negate', '+', '2', 'negate', 'exp', '1', '1', 'negate'],
                    '4e-22 + -2e-11', '-1.99999999996e-11')
        self._check(['4', 'negate', 'exp', '2', '2', 'negate', '+', '2', 'negate', 'exp', '1', '1', 'negate'],
                    '-4e-22 + -2e-11', '-2.00000000004e-11')

    def test_minus_operator(self):
        # Integer tests
        self._check(['4', '2', '-', '2', '1'], '42 - 21', '21')
        self._check([ '4', '2', 'negate', '-', '2', '1'], '-42 - 21', '-63')
        self._check(['4', '2', '-', '2', '1', 'negate'], '42 - -21', '63')
        self._check(['4', '2', 'negate', '-', '2', '1', 'negate'], '-42 - -21', '-21')

        # Float tests
        self._check(['4', '.', '2', '-', '2', '.', '1'], '4.2 - 2.1', '2.1')
        self._check(['4', '.', '2', 'negate', '-', '2', '.', '1'], '-4.2 - 2.1', '-6.3')
        self._check(['4', '.', '2', '-', '2', '.', '1', 'negate'], '4.2 - -2.1', '6.3')
        self._check(['4', '.', '2', 'negate', '-', '2', '.', '1', 'negate'], '-4.2 - -2.1', '-2.1')

        # Exponent tests
        self._check(['4', 'exp', '2', '2', '-', '2', 'exp', '1', '1'],
                    '4e22 - 2e11', '3.99999999998e22')
        self._check(['4', 'negate', 'exp', '2', '2', '-', '2', 'exp', '1', '1'],
                    '-4e22 - 2e11', '-4.00000000002e22')
        self._check(['4', 'exp', '2', '2', '-', '2', 'negate', 'exp', '1', '1'],
                    '4e22 - -2e11', '4.00000000002e22')
        self._check(['4', 'negate', 'exp', '2', '2', '-', '2', 'negate', 'exp', '1', '1'],
                    '-4e22 - -2e11', '-3.99999999998e22')
        self._check(['4', 'exp', '2', '2', 'negate', '-', '2', 'exp', '1', '1', 'negate'],
                    '4e-22 - 2e-11', '-1.99999999996e-11')
        self._check(['4', 'negate', 'exp', '2', '2', 'negate', '-', '2', 'exp', '1', '1', 'negate'],
                    '-4e-22 - 2e-11', '-2.00000000004e-11')
        self._check(['4', 'exp', '2', '2', 'negate', '-', '2', 'negate', 'exp', '1', '1', 'negate'],
                    '4e-22 - -2e-11', '2.00000000004e-11')
        self._check(['4', 'negate', 'exp', '2', '2', 'negate', '-', '2', 'negate', 'exp', '1', '1', 'negate'],
                    '-4e-22 - -2e-11', '1.99999999996e-11')

    def test_multiple_operator(self):
        # Integer tests
        self._check(['4', '2', '*', '2', '1'], '42 * 21', '882')
        self._check([ '4', '2', 'negate', '*', '2', '1'], '-42 * 21', '-882')
        self._check(['4', '2', '*', '2', '1', 'negate'], '42 * -21', '-882')
        self._check(['4', '2', 'negate', '*', '2', '1', 'negate'], '-42 * -21', '882')

        # Float tests
        self._check(['4', '.', '2', '*', '2', '.', '1'], '4.2 * 2.1', '8.82')
        self._check(['4', '.', '2', 'negate', '*', '2', '.', '1'], '-4.2 * 2.1', '-8.82')
        self._check(['4', '.', '2', '*', '2', '.', '1', 'negate'], '4.2 * -2.1', '-8.82')
        self._check(['4', '.', '2', 'negate', '*', '2', '.', '1', 'negate'], '-4.2 * -2.1', '8.82')

        # Exponent tests
        self._check(['4', 'exp', '2', '2', '*', '2', 'exp', '1', '1'],
                    '4e22 * 2e11', '8e33')
        self._check(['4', 'negate', 'exp', '2', '2', '*', '2', 'exp', '1', '1'],
                    '-4e22 * 2e11', '-8e33')
        self._check(['4', 'exp', '2', '2', '*', '2', 'negate', 'exp', '1', '1'],
                    '4e22 * -2e11', '-8e33')
        self._check(['4', 'negate', 'exp', '2', '2', '*', '2', 'negate', 'exp', '1', '1'],
                    '-4e22 * -2e11', '8e33')
        self._check(['4', 'exp', '2', '2', 'negate', '*', '2', 'exp', '1', '1', 'negate'],
                    '4e-22 * 2e-11', '8e-33')
        self._check(['4', 'negate', 'exp', '2', '2', 'negate', '*', '2', 'exp', '1', '1', 'negate'],
                    '-4e-22 * 2e-11', '-8e-33')
        self._check(['4', 'exp', '2', '2', 'negate', '*', '2', 'negate', 'exp', '1', '1', 'negate'],
                    '4e-22 * -2e-11', '-8e-33')
        self._check(['4', 'negate', 'exp', '2', '2', 'negate', '*', '2', 'negate', 'exp', '1', '1', 'negate'],
                    '-4e-22 * -2e-11', '8e-33')

    def test_division_operator(self):
        # Integer tests
        self._check(['4', '2', '/', '2', '1'], '42 / 21', '2')
        self._check([ '4', '2', 'negate', '/', '2', '1'], '-42 / 21', '-2')
        self._check(['4', '2', '/', '2', '1', 'negate'], '42 / -21', '-2')
        self._check(['4', '2', 'negate', '/', '2', '1', 'negate'], '-42 / -21', '2')

        # Float tests
        self._check(['4', '.', '2', '/', '2', '.', '1'], '4.2 / 2.1', '2')
        self._check(['4', '.', '2', 'negate', '/', '2', '.', '1'], '-4.2 / 2.1', '-2')
        self._check(['4', '.', '2', '/', '2', '.', '1', 'negate'], '4.2 / -2.1', '-2')
        self._check(['4', '.', '2', 'negate', '/', '2', '.', '1', 'negate'], '-4.2 / -2.1', '2')

        # Exponent tests
        self._check(['4', 'exp', '2', '2', '/', '2', 'exp', '1', '1'],
                    '4e22 / 2e11', '200000000000')
        self._check(['4', 'negate', 'exp', '2', '2', '/', '2', 'exp', '1', '1'],
                    '-4e22 / 2e11', '-200000000000')
        self._check(['4', 'exp', '2', '2', '/', '2', 'negate', 'exp', '1', '1'],
                    '4e22 / -2e11', '-200000000000')
        self._check(['4', 'negate', 'exp', '2', '2', '/', '2', 'negate', 'exp', '1', '1'],
                    '-4e22 / -2e11', '200000000000')
        self._check(['4', 'exp', '2', '2', 'negate', '/', '2', 'exp', '1', '1', 'negate'],
                    '4e-22 / 2e-11', '2.0000000000000002e-11')
        self._check(['4', 'negate', 'exp', '2', '2', 'negate', '/', '2', 'exp', '1', '1', 'negate'],
                    '-4e-22 / 2e-11', '-2.0000000000000002e-11')
        self._check(['4', 'exp', '2', '2', 'negate', '/', '2', 'negate', 'exp', '1', '1', 'negate'],
                    '4e-22 / -2e-11', '-2.0000000000000002e-11')
        self._check(['4', 'negate', 'exp', '2', '2', 'negate', '/', '2', 'negate', 'exp', '1', '1', 'negate'],
                    '-4e-22 / -2e-11', '2.0000000000000002e-11')

    def test_power_operator(self):
        # Integer tests
        self._check(['4', '^', '2'], '4 ^ 2', '16')
        self._check([ '4', 'negate', '^', '2'], '-4 ^ 2', '-16')
        self._check(['4', '^', '2', 'negate'], '4 ^ -2', '0.0625')
        self._check(['4', 'negate', '^', '2', 'negate'], '-4 ^ -2', '-0.0625')

        # Float tests
        self._check(['4', '.', '2', '^', '2', '.', '1'], '4.2 ^ 2.1', '20.3621443')
        self._check(['4', '.', '2', 'negate', '^', '2', '.', '1'], '-4.2 ^ 2.1', '-20.3621443')
        self._check(['4', '.', '2', '^', '2', '.', '1', 'negate'], '4.2 ^ -2.1', '0.0491107')
        self._check(['4', '.', '2', 'negate', '^', '2', '.', '1', 'negate'], '-4.2 ^ -2.1', '-0.0491107')

    def test_modulo_operator(self):
        # Integer tests
        self._check(['4', '2', 'mod', '3', '3'], '42 mod 33', '9')
        self._check(['4', '2', 'negate', 'mod', '3', '3'], '-42 mod 33', '24')
        self._check(['4', '2', 'mod', '3', '3', 'negate'], '42 mod -33', '-24')
        self._check(['4', '2', 'negate', 'mod', '3', '3', 'negate'], '-42 mod -33', '-9')

        # Float tests
        self._check(['4', '.', '2', 'mod', '3', '.', '3'], '4.2 mod 3.3', '0.9')
        self._check(['4', '.', '2', 'negate', 'mod', '3', '.', '3'], '-4.2 mod 3.3', '2.4')
        self._check(['4', '.', '2', 'mod', '3', '.', '3', 'negate'], '4.2 mod -3.3', '-2.4')
        self._check(['4', '.', '2', 'negate', 'mod', '3', '.', '3', 'negate'], '-4.2 mod -3.3', '-0.9')
        self._check(['4', '.', '2', '3', '5', '6', 'mod', '1'], '4.2356 mod 1', '0.2356')

    def test_paretheses(self):
        self._check(['(', '2', '+', '3', ')', '/', '(', '6', '+', '4', ')'], '(2 + 3) / (6 + 4)', '0.5')

    def test_sqrt_function(self):
        self._check(['sqrt', '4', ')'], 'sqrt(4)', '2')
        self._check(['sqrt', '0', '.','0', '4', ')'], '2 * sqrt(0.04)', '0.4')
        self._check(['sqrt', '4', 'exp','5', '2', ')'], '0.4 * sqrt(4e52)', '8e25')

    def test_sin_function(self):
        self._check(['sin', 'pi', '/', '2', ')'], 'sin(pi / 2)', '1')
        self._check(['sin', '3', '*', 'pi', '/', '2', ')'], '1 * sin(3 * pi / 2)', '-1')

    def test_asin_function(self):
        self._check(['asin', '1', ')'], 'asin(1)', '1.5707963')
        self._check(['asin', '1', 'negate', ')'], '1.5707963 * asin(-1)', '-2.4674011')

    def test_cos_function(self):
        self._check(['cos', 'pi', ')'], 'cos(pi)', '-1')
        self._check(['cos', '0', ')'], '-1 * cos(0)', '-1')

    def test_acos_function(self):
        self._check(['acos', '1', 'negate', ')'], 'acos(-1)', '3.1415927')
        self._check(['acos', '1', ')'], '3.1415927 * acos(1)', '0')

    def test_tan_function(self):
        self._check(['tan', '4', '2', ')'], 'tan(42)', '2.291388')

    def test_atan_function(self):
        self._check(['atan', '4', '2', ')'], 'atan(42)', '1.5469913')

    def test_ln_function(self):
        self._check(['ln', 'e', ')'], 'ln(e)', '1')

    def test_log_function(self):
        self._check(['log', '1', '0', '0', '0', ')'], 'log(1000)', '3')

    def test_errors(self):
        add_keys_to_calc_expression(self.calc_model, '1', '/', '0')
        self.assertEqual(self.calc_model.get_expression_string(), '1 / 0')
        self.assertRaises(ZeroDivisionError, self.calc_model.result)



if __name__ == '__main__':
    unittest.main()
