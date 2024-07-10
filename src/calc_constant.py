from calc_element import CalcElement, Type


class CalcConstant(CalcElement):

    def __init__(self, constant):
        super().__init__(Type.CONSTANT)
        self.__constant = constant
        self.__sign = True

    def encode(self):
        return super().encode() | {
            'constant': self.__constant,
            'sign': self.__sign
        }

    def decode(self, constant='e', sign=True, **_):
        self.__constant = constant
        self.__sign = sign

    def negate(self):
        self.__sign = not self.__sign

    def __str__(self):
        sign = '' if self.__sign else '-'
        return sign + self.__constant
