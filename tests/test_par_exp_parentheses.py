import unittest
import calc_parexp

from tests.test_utils import add_keys_to_calc_expression

class ParenthesesTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()
    
    def test_add_key_parentheses_single_open(self):
        self.par_exp.add_key('(')
        self.assertEqual(str(self.par_exp), '(')

    def test_add_key_parentheses_single_close(self):
        self.par_exp.add_key(')')
        self.assertEqual(str(self.par_exp), '')

    def test_add_key_parentheses_multiple_open(self):
        add_keys_to_calc_expression(self.par_exp, '(', '(', '(')
        self.assertEqual(str(self.par_exp), '(((')
    
    def test_add_key_parentheses_add_number(self):
        add_keys_to_calc_expression(self.par_exp, '(', '1', '2')
        self.assertEqual(str(self.par_exp), '(12')
    
    def test_add_key_parentheses_add_operator_after_close(self):
        add_keys_to_calc_expression(self.par_exp, '(', '1', '2', ')', '+')
        self.assertEqual(str(self.par_exp), '(12) + ')

    def test_add_key_parentheses_add_number_after_close(self):
        add_keys_to_calc_expression(self.par_exp, '(', '1', '2', ')', '1')
        self.assertEqual(str(self.par_exp), '(12) * 1')
        
    def test_add_key_parentheses_add_constant_after_close(self):
        add_keys_to_calc_expression(self.par_exp, '(', '1', '2', ')', 'pi')
        self.assertEqual(str(self.par_exp), '(12) * pi')

    def test_add_key_parentheses_add_parentheses_after_close(self):
        add_keys_to_calc_expression(self.par_exp, '(', '1', '2', ')', '(')
        self.assertEqual(str(self.par_exp), '(12) * (')

if __name__ == '__main__':
    unittest.main()
