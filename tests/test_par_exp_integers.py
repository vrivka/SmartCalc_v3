import unittest
import calc_parexp

class IntegersTest(unittest.TestCase):
    def setUp(self):
        self.par_exp = calc_parexp.CalcParExp()
        return super().setUp()

    def test_add_key_integer(self):
        keys = '1234567890'
        expected = [keys[:i] for i in range(len(keys) + 1)]
        for k, e in zip(keys, expected):
            self.assertEqual(str(self.par_exp), e)
            self.par_exp.add_key(k)



if __name__ == '__main__':
    unittest.main()
