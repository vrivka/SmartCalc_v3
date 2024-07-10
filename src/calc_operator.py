from calc_element import CalcElement, Type


class CalcOperator(CalcElement):

    def __init__(self, operator):
        super().__init__(Type.OPERATOR)
        self.__operator = operator

    def encode(self):
        return super().encode() | {
            'operator': self.__operator
        }

    def decode(self, operator='+', **_):
        self.__operator = operator

    def set_operator(self, operator):
        self.__operator = operator

    def __str__(self):
        return f' {self.__operator} '
