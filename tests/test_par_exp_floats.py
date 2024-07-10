import unittest
import calc_parexp

class FloatsTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()

    def test_add_key_float_empty_started(self):
        keys = '.0123'
        expected = ('0.', '0.0', '0.01', '0.012', '0.0123')
        for k, e in zip(keys, expected):
            self.par_exp.add_key(k)
            self.assertEqual(str(self.par_exp), e)

    def test_add_key_float_zero_started(self):
        keys = '0.0123'
        expected = ('0', '0.', '0.0', '0.01', '0.012', '0.0123')
        for k, e in zip(keys, expected):
            self.par_exp.add_key(k)
            self.assertEqual(str(self.par_exp), e)

    def test_add_key_float_integers_started(self):
        keys = '123.0123'
        expected = ('1', '12', '123', '123.', '123.0', '123.01', '123.012', '123.0123')
        for k, e in zip(keys, expected):
            self.par_exp.add_key(k)
            self.assertEqual(str(self.par_exp), e)

    def test_add_key_float_multiple_zero_started(self):
        keys = '000.0123'
        expected = ('0', '0', '0', '0.', '0.0', '0.01', '0.012', '0.0123')
        for k, e in zip(keys, expected):
            self.par_exp.add_key(k)
            self.assertEqual(str(self.par_exp), e)

    def test_add_key_float_only_zero(self):
        keys = '000.0000'
        expected = ('0', '0', '0', '0.', '0.0', '0.00', '0.000', '0.0000')
        for k, e in zip(keys, expected):
            self.par_exp.add_key(k)
            self.assertEqual(str(self.par_exp), e)

    def test_add_key_float_multiple_dots(self):
        keys = '10.00.00.00.'
        expected = ('1', '10', '10.', '10.0', '10.00', '10.00', '10.000', '10.0000', '10.0000', '10.00000', '10.000000', '10.000000')
        for k, e in zip(keys, expected):
            self.par_exp.add_key(k)
            self.assertEqual(str(self.par_exp), e)


if __name__ == '__main__':
    unittest.main()
