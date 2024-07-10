import unittest
import calc_parexp

from tests.test_utils import add_keys_to_calc_expression

class StatusTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()
    
    def test_add_key_main_status(self):
        self.assertEqual(self.par_exp.status, calc_parexp.Status.MAIN)
        
    def test_add_key_complete_status(self):
        add_keys_to_calc_expression(self.par_exp, '1', '+', '2')
        self.assertEqual(str(self.par_exp), '1 + 2')
        self.par_exp.add_key('=')
        self.assertEqual(self.par_exp.status, calc_parexp.Status.COMPLETE)

    def test_add_key_add_after_complete_status(self):
        add_keys_to_calc_expression(self.par_exp, '1', '+', '2')
        self.assertEqual(str(self.par_exp), '1 + 2')
        self.par_exp.add_key('=')
        add_keys_to_calc_expression(self.par_exp, '6', '*', '8')
        self.assertEqual(str(self.par_exp), '6 * 8')

if __name__ == '__main__':
    unittest.main()
