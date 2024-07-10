import unittest
import calc_parexp

from tests.test_utils import add_keys_to_calc_expression


class OperatorTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()

    def test_add_key_operators_empty(self):
        self.par_exp.add_key('+')
        self.assertEqual(str(self.par_exp), '')
        self.par_exp.add_key('-')
        self.assertEqual(str(self.par_exp), '')
        self.par_exp.add_key('*')
        self.assertEqual(str(self.par_exp), '')
        self.par_exp.add_key('/')
        self.assertEqual(str(self.par_exp), '')
        self.par_exp.add_key('^')
        self.assertEqual(str(self.par_exp), '')
        self.par_exp.add_key('mod')
        self.assertEqual(str(self.par_exp), '')

    def test_add_key_operators_swap(self):
        add_keys_to_calc_expression(self.par_exp, '1', '2', '3', '+')
        self.assertEqual(str(self.par_exp), '123 + ')
        self.par_exp.add_key('-')
        self.assertEqual(str(self.par_exp), '123 - ')
        self.par_exp.add_key('*')
        self.assertEqual(str(self.par_exp), '123 * ')
        self.par_exp.add_key('/')
        self.assertEqual(str(self.par_exp), '123 / ')
        self.par_exp.add_key('^')
        self.assertEqual(str(self.par_exp), '123 ^ ')
        self.par_exp.add_key('mod')
        self.assertEqual(str(self.par_exp), '123 mod ')

if __name__ == '__main__':
    unittest.main()
