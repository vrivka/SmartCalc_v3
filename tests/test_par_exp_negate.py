import unittest
import calc_parexp

from tests.test_utils import add_keys_to_calc_expression

class NegateTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()

    def test_add_key_integer_negate(self):
        add_keys_to_calc_expression(self.par_exp, '1', '2', '3', 'negate')
        self.assertEqual(str(self.par_exp), '-123')
        self.par_exp.add_key('negate')
        self.assertEqual(str(self.par_exp), '123')

    def test_add_key_float_negate(self):
        add_keys_to_calc_expression(self.par_exp, '1', '2', '.', '3', 'negate')
        self.assertEqual(str(self.par_exp), '-12.3')
        self.par_exp.add_key('negate')
        self.assertEqual(str(self.par_exp), '12.3')

    def test_add_key_exponent_negate(self):
        add_keys_to_calc_expression(self.par_exp, '1', '2', 'exp', '3', 'negate')
        self.assertEqual(str(self.par_exp), '12e-3')
        self.par_exp.add_key('negate')
        self.assertEqual(str(self.par_exp), '12e3')
    
    def test_add_key_constant_negate(self):
        add_keys_to_calc_expression(self.par_exp, 'e', 'negate')
        self.assertEqual(str(self.par_exp), '-e')
        self.par_exp.add_key('negate')
        self.assertEqual(str(self.par_exp), 'e')

    def test_add_key_operator_negate(self):
        add_keys_to_calc_expression(self.par_exp, '1', '+', 'negate')
        self.assertEqual(str(self.par_exp), '1 + ')
        self.par_exp.add_key('negate')
        self.assertEqual(str(self.par_exp), '1 + ')
    
    def test_add_key_parentheses_close_negate(self):
        add_keys_to_calc_expression(self.par_exp, '(', '1', ')', 'negate')
        self.assertEqual(str(self.par_exp), '-(1)')
        self.par_exp.add_key('negate')
        self.assertEqual(str(self.par_exp), '(1)')
        
            
    def test_add_key_parentheses_open_negate(self):
        add_keys_to_calc_expression(self.par_exp, '(', '1', 'negate')
        self.assertEqual(str(self.par_exp), '(-1')
        self.par_exp.add_key('negate')
        self.assertEqual(str(self.par_exp), '(1')
        
    def test_add_key_function_negate(self):
        add_keys_to_calc_expression(self.par_exp, 'ln', '1', ')', 'negate')
        self.assertEqual(str(self.par_exp), '-ln(1)')
        self.par_exp.add_key('negate')
        self.assertEqual(str(self.par_exp), 'ln(1)')


if __name__ == '__main__':
    unittest.main()
