import unittest
import calc_parexp

from tests.test_utils import add_keys_to_calc_expression

class ClearEntryTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()
    
    def test_add_key_clear_empty(self):
        self.par_exp.add_key('clr')
        self.assertEqual(str(self.par_exp), '')

    def test_add_key_clear_nonempty(self):
        add_keys_to_calc_expression(self.par_exp, '1', '2', '+', '2', '1')
        self.assertEqual(str(self.par_exp), '12 + 21')
        self.par_exp.add_key('clr')
        self.assertEqual(str(self.par_exp), '')

if __name__ == '__main__':
    unittest.main()
