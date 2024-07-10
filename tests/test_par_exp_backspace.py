import unittest
import calc_parexp

from tests.test_utils import add_keys_to_calc_expression

class BackspaceTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()

    def test_add_key_backspace_empty(self):
        self.par_exp.add_key('bckspc')
        self.assertEqual(str(self.par_exp), '')

    def test_add_key_backspace_integer(self):
        case = '123'
        add_keys_to_calc_expression(self.par_exp, *list(case))
        expected = [case[:i] for i in range(len(case) - 1, -1, -1)]
        for e in expected:
            self.par_exp.add_key('bckspc')
            self.assertEqual(str(self.par_exp), e)

    def test_add_key_backspace_float(self):
        case = '123.0321'
        add_keys_to_calc_expression(self.par_exp, *list('123.0321'))
        expected = [case[:i] for i in range(len(case) - 1, -1, -1)]
        for e in expected:
            self.par_exp.add_key('bckspc')
            self.assertEqual(str(self.par_exp), e)

    def test_add_key_backspace_exponent(self):
        add_keys_to_calc_expression(self.par_exp, '1', '2', 'exp', '2', 'negate')
        expected = ['12e-', '12e', '12', '1', '']
        for e in expected:
            self.par_exp.add_key('bckspc')
            self.assertEqual(str(self.par_exp), e)

    def test_add_key_backspace_constant(self):
        self.par_exp.add_key('pi')
        self.assertEqual(str(self.par_exp), 'pi')
        self.par_exp.add_key('bckspc')
        self.assertEqual(str(self.par_exp), '')

    def test_add_key_backspace_operator(self):
        add_keys_to_calc_expression(self.par_exp, '1', '+')
        self.assertEqual(str(self.par_exp), '1 + ')
        self.par_exp.add_key('bckspc')
        self.assertEqual(str(self.par_exp), '1')

    def test_add_key_backspace_paretheses_open(self):
        add_keys_to_calc_expression(self.par_exp,'(', '1', )
        self.assertEqual(str(self.par_exp), '(1')
        self.par_exp.add_key('bckspc')
        self.assertEqual(str(self.par_exp), '(')
        self.par_exp.add_key('bckspc')
        self.assertEqual(str(self.par_exp), '')

    def test_add_key_backspace_paretheses_close(self):
        add_keys_to_calc_expression(self.par_exp,'(', '1', '2', ')')
        self.assertEqual(str(self.par_exp), '(12)')
        self.par_exp.add_key('bckspc')
        self.assertEqual(str(self.par_exp), '(12')

    def test_add_key_backspace_function(self):
        self.par_exp.add_key('sqrt')
        self.assertEqual(str(self.par_exp), 'sqrt(')
        self.par_exp.add_key('bckspc')
        self.assertEqual(str(self.par_exp), '')


if __name__ == '__main__':
    unittest.main()
