import unittest
import calc_parexp

from tests.test_utils import add_keys_to_calc_expression

class ExponentTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()

    def test_add_key_exponent(self):
        add_keys_to_calc_expression(self.par_exp, '1', '2', '3', '4', 'exp')
        self.assertEqual(str(self.par_exp), '1234e')
        add_keys_to_calc_expression(self.par_exp, '1', '2', '3', '4')
        self.assertEqual(str(self.par_exp), '1234e1234')
        self.par_exp.add_key('.')
        self.assertEqual(str(self.par_exp), '1234e1234')
    
    def test_add_key_exponent_empty_started(self):
        add_keys_to_calc_expression(self.par_exp, 'exp')
        self.assertEqual(str(self.par_exp), '0e')


if __name__ == '__main__':
    unittest.main()
