import unittest

from tests.test_utils import add_keys_to_calc_expression

import calc_parexp
import calc_element
import calc_number


class SerializationTest(unittest.TestCase):
    def setUp(self):
        self.par_exp_empty = calc_parexp.CalcParExp()

        self.par_exp_simple_with_operators = calc_parexp.CalcParExp()
        add_keys_to_calc_expression(
            self.par_exp_simple_with_operators,
            '1', 'negate', '+', '2', '.', '3', '-', '1', '.', '2', 'exp', 'negate', '1', '5',
            '*', '2', 'exp', '1', '5', '/', '0', '.', '3', '4', '5', '^', '2', 'mod', '3')

        self.par_exp_parentheses = calc_parexp.CalcParExp()
        add_keys_to_calc_expression(
            self.par_exp_parentheses,
            '(', '2', '+', '3', ')', 'negate', '/', '(', '(', '4', '^', '2', ')', ')')

        self.par_exp_complex = calc_parexp.CalcParExp()
        add_keys_to_calc_expression(
            self.par_exp_complex,
            'sqrt', '2', '+', '3', ')', '/', 'sin', 'cos', 'pi', '^', '2', ')', ')')

        return super().setUp()

    def test_empty(self):
        empty_encode_expected = {
            'type': calc_element.Type.PAR_EXP.name,
            'name': '',
            'status': calc_parexp.Status.MAIN.name,
            'stack': [],
            'sign': True
        }
        encoded = self.par_exp_empty.encode()
        self.assertEqual(encoded, empty_encode_expected)

        self.par_exp_empty.decode(**encoded)
        self.assertEqual(str(self.par_exp_empty), '')

    def test_simple_with_operators(self):
        simple_encode_expected = {
            "type": calc_element.Type.PAR_EXP.name,
            "name": "",
            "status": calc_parexp.Status.MAIN.name,
            'sign': True,
            "stack": [
                {
                    "type": calc_element.Type.NUMBER.name,
                    "number": "1",
                    "exp_number": "",
                    "status": calc_number.NumStatus.INT.name,
                    "sign": False,
                    "exp_sign": True
                },
                {
                    "type": calc_element.Type.OPERATOR.name,
                    "operator": "+"
                },
                {
                    "type": calc_element.Type.NUMBER.name,
                    "number": "2.3",
                    "exp_number": "",
                    "status": calc_number.NumStatus.FLOAT.name,
                    "sign": True,
                    "exp_sign": True
                },
                {
                    "type": calc_element.Type.OPERATOR.name,
                    "operator": "-"
                },
                {
                    "type": calc_element.Type.NUMBER.name,
                    "number": "1.2e",
                    "exp_number": "15",
                    "status": calc_number.NumStatus.EXP.name,
                    "sign": True,
                    "exp_sign": False
                },
                {
                    "type": calc_element.Type.OPERATOR.name,
                    "operator": "*"
                },
                {
                    "type": calc_element.Type.NUMBER.name,
                    "number": "2e",
                    "exp_number": "15",
                    "status": calc_number.NumStatus.EXP.name,
                    "sign": True,
                    "exp_sign": True
                },
                {
                    "type": calc_element.Type.OPERATOR.name,
                    "operator": "/"
                },
                {
                    "type": calc_element.Type.NUMBER.name,
                    "number": "0.345",
                    "exp_number": "",
                    "status": calc_number.NumStatus.FLOAT.name,
                    "sign": True,
                    "exp_sign": True
                },
                {
                    "type": calc_element.Type.OPERATOR.name,
                    "operator": "^"
                },
                {
                    "type": calc_element.Type.NUMBER.name,
                    "number": "2",
                    "exp_number": "",
                    "status": calc_number.NumStatus.INT.name,
                    "sign": True,
                    "exp_sign": True
                },
                {
                    "type": calc_element.Type.OPERATOR.name,
                    "operator": "mod"
                },
                {
                    "type": calc_element.Type.NUMBER.name,
                    "number": "3",
                    "exp_number": "",
                    "status": calc_number.NumStatus.INT.name,
                    "sign": True,
                    "exp_sign": True
                }
            ]
        }
        encoded = self.par_exp_simple_with_operators.encode()
        self.assertEqual(encoded, simple_encode_expected)

        self.par_exp_simple_with_operators.decode(**encoded)
        self.assertEqual(str(self.par_exp_simple_with_operators), '-1 + 2.3 - 1.2e-15 * 2e15 / 0.345 ^ 2 mod 3')

    def test_parentheses(self):
        parentheses_encode_expected = {
            "type": calc_element.Type.PAR_EXP.name,
            "name": "",
            "status": calc_parexp.Status.MAIN.name,
            "stack": [
                {
                    "type": calc_element.Type.PAR_EXP.name,
                    "name": "",
                    "status": calc_parexp.Status.CLOSE.name,
                    "stack": [
                        {
                            "type": calc_element.Type.NUMBER.name,
                            "number": "2",
                            "exp_number": "",
                            "status": calc_number.NumStatus.INT.name,
                            "sign": True,
                            "exp_sign": True
                        },
                        {
                            "type": calc_element.Type.OPERATOR.name,
                            "operator": "+"
                        },
                        {
                            "type": calc_element.Type.NUMBER.name,
                            "number": "3",
                            "exp_number": "",
                            "status": calc_number.NumStatus.INT.name,
                            "sign": True,
                            "exp_sign": True
                        }
                    ],
                    "sign": False
                },
                {
                    "type": calc_element.Type.OPERATOR.name,
                    "operator": "/"
                },
                {
                    "type": calc_element.Type.PAR_EXP.name,
                    "name": "",
                    "status": calc_parexp.Status.CLOSE.name,
                    "stack": [
                        {
                            "type": calc_element.Type.PAR_EXP.name,
                            "name": "",
                            "status": calc_parexp.Status.CLOSE.name,
                            "stack": [
                                {
                                    "type": calc_element.Type.NUMBER.name,
                                    "number": "4",
                                    "exp_number": "",
                                    "status": calc_number.NumStatus.INT.name,
                                    "sign": True,
                                    "exp_sign": True
                                },
                                {
                                    "type": calc_element.Type.OPERATOR.name,
                                    "operator": "^"
                                },
                                {
                                    "type": calc_element.Type.NUMBER.name,
                                    "number": "2",
                                    "exp_number": "",
                                    "status": calc_number.NumStatus.INT.name,
                                    "sign": True,
                                    "exp_sign": True
                                }
                            ],
                            "sign": True
                        }
                    ],
                    "sign": True
                }
            ],
            "sign": True
        }
        encoded = self.par_exp_parentheses.encode()
        self.assertEqual(encoded, parentheses_encode_expected)

        self.par_exp_parentheses.decode(**encoded)
        self.assertEqual(str(self.par_exp_parentheses), '-(2 + 3) / ((4 ^ 2))')

    def test_complex(self):
        complex_encode_expected = {
            "type": calc_element.Type.PAR_EXP.name,
            "name": "",
            "status": calc_parexp.Status.MAIN.name,
            "stack": [
                {
                    "type": calc_element.Type.PAR_EXP.name,
                    "name": "sqrt",
                    "status": calc_parexp.Status.CLOSE.name,
                    "stack": [
                        {
                            "type": calc_element.Type.NUMBER.name,
                            "number": "2",
                            "exp_number": "",
                            "status": calc_number.NumStatus.INT.name,
                            "sign": True,
                            "exp_sign": True
                        },
                        {
                            "type": calc_element.Type.OPERATOR.name,
                            "operator": "+"
                        },
                        {
                            "type": calc_element.Type.NUMBER.name,
                            "number": "3",
                            "exp_number": "",
                            "status": calc_number.NumStatus.INT.name,
                            "sign": True,
                            "exp_sign": True
                        }
                    ],
                    "sign": True
                },
                {
                    "type": calc_element.Type.OPERATOR.name,
                    "operator": "/"
                },
                {
                    "type": calc_element.Type.PAR_EXP.name,
                    "name": "sin",
                    "status": calc_parexp.Status.CLOSE.name,
                    "stack": [
                        {
                            "type": calc_element.Type.PAR_EXP.name,
                            "name": "cos",
                            "status": calc_parexp.Status.CLOSE.name,
                            "stack": [
                                {
                                    "type": calc_element.Type.CONSTANT.name,
                                    "constant": "pi",
                                    "sign": True
                                },
                                {
                                    "type": calc_element.Type.OPERATOR.name,
                                    "operator": "^"
                                },
                                {
                                    "type": calc_element.Type.NUMBER.name,
                                    "number": "2",
                                    "exp_number": "",
                                    "status": calc_number.NumStatus.INT.name,
                                    "sign": True,
                                    "exp_sign": True
                                }
                            ],
                            "sign": True
                        }
                    ],
                    "sign": True
                }
            ],
            "sign": True
        }
        encoded = self.par_exp_complex.encode()
        self.assertEqual(encoded, complex_encode_expected)

        self.par_exp_complex.decode(**encoded)
        self.assertEqual(str(self.par_exp_complex), 'sqrt(2 + 3) / sin(cos(pi ^ 2))')


if __name__ == '__main__':
    unittest.main()
