import unittest
import calc_parexp

from tests.test_utils import add_keys_to_calc_expression

class ConstantTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()

    def test_add_key_constant_pi(self):
        self.par_exp.add_key('pi')
        self.assertEqual(str(self.par_exp), 'pi')

    def test_add_key_constant_e(self):
        self.par_exp.add_key('e')
        self.assertEqual(str(self.par_exp), 'e')

    def test_add_key_constant_after_number(self):
        add_keys_to_calc_expression(self.par_exp, '1', '2', '3', '-', 'e')
        self.assertEqual(str(self.par_exp), '123 - e')

    def test_add_key_constant_after_operator(self):
        add_keys_to_calc_expression(self.par_exp, '1', '2', '3', 'e')
        self.assertEqual(str(self.par_exp), '123 * e')

    def test_add_key_constant_after_constant(self):
        add_keys_to_calc_expression(self.par_exp, 'pi', 'e')
        self.assertEqual(str(self.par_exp), 'pi * e')


if __name__ == '__main__':
    unittest.main()
