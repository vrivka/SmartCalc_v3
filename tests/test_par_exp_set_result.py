import unittest
import calc_parexp

class SetResultTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()
    
    def test_set_result_integer(self):
        self.par_exp.set_result(123)
        self.assertEqual(str(self.par_exp), '123')
        self.par_exp.set_result(15_345)
        self.assertEqual(str(self.par_exp), '15345')
        self.par_exp.set_result(-15)
        self.assertEqual(str(self.par_exp), '-15')
    
    def test_set_result_float(self):
        self.par_exp.set_result(15.5)
        self.assertEqual(str(self.par_exp), '15.5')
        self.par_exp.set_result(15.5000000000000000000001)
        self.assertEqual(str(self.par_exp), '15.5')
        self.par_exp.set_result(0.543)
        self.assertEqual(str(self.par_exp), '0.543')
        self.par_exp.set_result(-648.33)
        self.assertEqual(str(self.par_exp), '-648.33')
        self.par_exp.set_result(648.123456789)
        self.assertEqual(str(self.par_exp), '648.1234568')
    
    def test_set_result_exponent(self):
        self.par_exp.set_result(123e20)
        self.assertEqual(str(self.par_exp), '1.23e22')
        self.par_exp.set_result(123456e-2)
        self.assertEqual(str(self.par_exp), '1234.56')
        self.par_exp.set_result(1.5e6)
        self.assertEqual(str(self.par_exp), '1500000')
        self.par_exp.set_result(0.000000000000000000000000000000000000000000000000000000012)
        self.assertEqual(str(self.par_exp), '1.2e-56')
        self.par_exp.set_result(120000000000000000000000000000000000000000000000000000000.0)
        self.assertEqual(str(self.par_exp), '1.2e56')
        self.par_exp.set_result(0.11e-22)
        self.assertEqual(str(self.par_exp), '1.1e-23')
        self.par_exp.set_result(0.11e-22)
        self.assertEqual(str(self.par_exp), '1.1e-23')
        self.par_exp.set_result(1.7e308)
        self.assertEqual(str(self.par_exp), '1.7e308')
        self.par_exp.set_result(1.7e-500)
        self.assertEqual(str(self.par_exp), '0')
        self.assertRaises(ValueError, self.par_exp.set_result, 1.82e308)

if __name__ == '__main__':
    unittest.main()
