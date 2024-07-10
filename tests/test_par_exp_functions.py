import unittest
import calc_parexp

class FunctionTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()
    
    def test_add_key_function_sqrt(self):
        self.par_exp.add_key('sqrt')
        self.assertEqual(str(self.par_exp), 'sqrt(')

    def test_add_key_function_sin(self):
        self.par_exp.add_key('sin')
        self.assertEqual(str(self.par_exp), 'sin(')

    def test_add_key_function_asin(self):
        self.par_exp.add_key('asin')
        self.assertEqual(str(self.par_exp), 'asin(')

    def test_add_key_function_cos(self):
        self.par_exp.add_key('cos')
        self.assertEqual(str(self.par_exp), 'cos(')

    def test_add_key_function_acos(self):
        self.par_exp.add_key('acos')
        self.assertEqual(str(self.par_exp), 'acos(')

    def test_add_key_function_tan(self):
        self.par_exp.add_key('tan')
        self.assertEqual(str(self.par_exp), 'tan(')

    def test_add_key_function_atan(self):
        self.par_exp.add_key('atan')
        self.assertEqual(str(self.par_exp), 'atan(')

    def test_add_key_function_ln(self):
        self.par_exp.add_key('ln')
        self.assertEqual(str(self.par_exp), 'ln(')

    def test_add_key_function_log(self):
        self.par_exp.add_key('log')
        self.assertEqual(str(self.par_exp), 'log(')

    def test_add_key_function_undefined(self):
        self.par_exp.add_key('max')
        self.assertEqual(str(self.par_exp), '')

if __name__ == '__main__':
    unittest.main()
