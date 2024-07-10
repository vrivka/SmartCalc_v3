from enum import Flag, auto

from calc_element import CalcElement, Type


class NumStatus(Flag):
    ZERO = auto()
    INT = auto()
    FLOAT = auto()
    EXP = auto()


def _define_status(status):
    match status:
        case 'ZERO':
            return NumStatus.ZERO
        case 'INT':
            return NumStatus.INT
        case 'FLOAT':
            return NumStatus.FLOAT
        case 'EXP':
            return NumStatus.EXP
        case _:
            raise ValueError(f'ERROR: cannot define status from value: {status}')


class CalcNumber(CalcElement):

    def __init__(self):
        super().__init__(Type.NUMBER)
        self.__number = '0'
        self.__exp_number = ''
        self.__status = NumStatus.ZERO
        self.__sign = True
        self.__exp_sign = True

    def encode(self):
        return super().encode() | {
            'number': self.__number,
            'exp_number': self.__exp_number,
            'status': self.__status.name,
            'sign': self.__sign,
            'exp_sign': self.__exp_sign
        }

    def decode(self, number='0', exp_number='', status=NumStatus.ZERO.name, sign=True, exp_sign=True, **_):
        self.__number = number
        self.__exp_number = exp_number
        self.__status = _define_status(status)
        self.__sign = sign
        self.__exp_sign = exp_sign

    def parse_number(self, nbr):
        str_nbr = str(nbr)

        if str_nbr == 'inf':
            raise ValueError
        if isinstance(nbr, float) and 'e' not in str_nbr:
            str_nbr = str(round(nbr, 7)).rstrip('0')
        for c in str_nbr:
            if c == 'e':
                self.add_key('exp')
            elif c == '+':
                continue
            else:
                self.add_key(c)
        self.optimize()

    def __zero_status_handler(self, value):
        if value == '.':
            self.__status = NumStatus.FLOAT
        elif value == 'exp':
            self.__status = NumStatus.EXP
            value = 'e'
        elif value == '0':
            return
        else:
            self.__number = ''
            self.__status = NumStatus.INT
        self.__number += value

    def __int_status_handler(self, value):
        if value == '.':
            self.__status = NumStatus.FLOAT
        elif value == 'exp':
            self.__status = NumStatus.EXP
            value = 'e'
        self.__number += value

    def __float_status_handler(self, value):
        if value == '.':
            return
        elif value == 'exp':
            self.__status = NumStatus.EXP
            value = 'e'
        self.__number += value

    def __exp_status_handler(self, value):
        if value in ('.', 'exp'):
            return
        self.__exp_number += value

    def backspace(self):
        if self.__status in NumStatus.EXP:
            if self.__exp_number != '':
                self.__exp_number = self.__exp_number[:-1]
                return
            if not self.__exp_sign:
                self.negate()
                return
        if self.__status in NumStatus.INT and self.__number == '' and not self.__sign:
            self.negate()
            super().backspace()
            return
        self.__number = self.__number[:-1]
        self.__status = NumStatus.FLOAT if '.' in self.__number else NumStatus.INT
        self.__status = NumStatus.ZERO if self.__number == '0' else self.__status
        if self.__number == '' and self.__sign:
            super().backspace()

    def negate(self):
        if self.__status in NumStatus.EXP:
            self.__exp_sign = not self.__exp_sign
        else:
            self.__sign = not self.__sign

    def optimize(self):
        if self.__status in NumStatus.EXP and self.__exp_number == '':
            if not self.__exp_sign:
                self.negate()
            self.__number = self.__number[:-1]
            if '.' in self.__number:
                self.__status = NumStatus.FLOAT
            else:
                self.__status = NumStatus.INT
        if self.__status in NumStatus.FLOAT and self.__number[-1] == '.':
            self.__number = self.__number[:-1]
            self.__status = NumStatus.INT
        if self.__status in NumStatus.INT and self.__number == '':
            self.__number = '0'
            self.__sign = True

    def add_key(self, value: str):
        if self.__status == NumStatus.ZERO:
            self.__zero_status_handler(value)
        elif self.__status == NumStatus.INT:
            self.__int_status_handler(value)
        elif self.__status == NumStatus.FLOAT:
            self.__float_status_handler(value)
        elif self.__status == NumStatus.EXP:
            self.__exp_status_handler(value)

    def __str__(self):
        sign = '' if self.__sign else '-'
        exp_sign = '' if self.__exp_sign else '-'
        return sign + self.__number + exp_sign + self.__exp_number
