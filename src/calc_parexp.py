from enum import Flag, auto

from calc_constant import CalcConstant
from calc_element import CalcElement, Type
from calc_number import CalcNumber
from calc_operator import CalcOperator


class Status(Flag):
    MAIN = auto()
    OPEN = auto()
    CLOSE = auto()
    COMPLETE = auto()


def _define_status(status):
    match status:
        case 'MAIN':
            return Status.MAIN
        case 'OPEN':
            return Status.CLOSE
        case 'CLOSE':
            return Status.CLOSE
        case 'COMPLETE':
            return Status.COMPLETE
        case _:
            raise ValueError(f'ERROR: cannot define status from value: {status}')


class CalcParExp(CalcElement):
    __NUMBERS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', 'exp',)
    __CONSTANTS = ('e', 'pi')
    __NEGATE = ('negate',)
    __OPERATORS = ('+', '-', '*', '/', 'mod', '^',)
    __FUNCTIONS = ('sqrt', 'sin', 'asin', 'cos', 'acos', 'tan', 'atan', 'ln', 'log',)
    __CONTROL_STATEMENTS = ('(', ')', 'bckspc', 'clr', '=',)

    def __init__(self, status=Status.MAIN, name=''):
        super().__init__(Type.PAR_EXP)
        self._stack = []
        self.status = status
        self._name = name
        self.sign = True

    def encode(self):
        stack = []

        for elem in self._stack:
            stack.append(elem.encode())
        return super().encode() | {
            'name': self._name,
            'status': self.status.name,
            'stack': stack,
            'sign': self.sign
        }

    def decode(self, name='', status=Status.MAIN.name, stack=None, sign=True, **_):
        self._name = name
        self.status = _define_status(status)
        self._stack = []
        self.sign = sign

        if stack:
            for elem in stack:
                match elem['type']:
                    case 'PAR_EXP':
                        element = CalcParExp()
                    case 'NUMBER':
                        element = CalcNumber()
                    case 'CONSTANT':
                        element = CalcConstant('e')
                    case 'OPERATOR':
                        element = CalcOperator('+')
                    case _: continue
                element.decode(**elem)
                self._stack.append(element)

    @property
    def _last_element(self):
        try:
            return self._stack[-1]
        except IndexError:
            return None

    def set_result(self, nbr):
        self.add_key('clr')
        res = CalcNumber()
        res.parse_number(nbr)

        self._stack.append(res)
        self.add_key('=')

    def _add_number(self, value: str):
        if self._last_element is None or self._last_element.type in Type.OPERATOR:
            new_number = CalcNumber()
            new_number.add_key(value)
            self._stack.append(new_number)
        elif self._last_element.type in Type.NUMBER:
            self._last_element.add_key(value)
        elif self._last_element.type in Type.CONSTANT:
            self._add_operator('*')
            self._add_number(value)
        elif self._last_element.type in Type.PAR_EXP:
            if self._last_element.status in Status.OPEN:
                self._last_element.add_key(value)
            elif self._last_element.status in Status.CLOSE:
                self._add_operator('*')
                self._add_number(value)

    def _add_constant(self, value: str):
        if self._last_element is None or self._last_element.type in Type.OPERATOR:
            self._stack.append(CalcConstant(value))

        elif self._last_element.type in Type.NUMBER | Type.CONSTANT:
            self._add_operator('*')
            self._add_constant(value)
        elif self._last_element.type in Type.PAR_EXP:
            if self._last_element.status in Status.OPEN:
                self._last_element.add_key(value)
            elif self._last_element.status in Status.CLOSE:
                self._add_operator('*')
                self._add_constant(value)

    def _negate(self):
        if self._last_element is None:
            return
        if self._last_element.type in Type.NUMBER | Type.CONSTANT:
            self._last_element.negate()
        elif self._last_element.type in Type.PAR_EXP:
            if self._last_element.status in Status.OPEN:
                self._last_element.add_key('negate')
            elif self._last_element.status in Status.CLOSE:
                self._last_element.sign = not self._last_element.sign

    def _add_operator(self, value: str):
        if self._last_element is None:
            return
        if self._last_element.type in Type.NUMBER | Type.CONSTANT:
            if self._last_element.type in Type.NUMBER:
                self._last_element.optimize()
            self._stack.append(CalcOperator(value))

        elif self._last_element.type in Type.OPERATOR:
            self._last_element.set_operator(value)
        elif self._last_element.type in Type.PAR_EXP:
            if self._last_element.status in Status.OPEN:
                self._last_element.add_key(value)
            elif self._last_element.status in Status.CLOSE:
                self._stack.append(CalcOperator(value))

    def _add_function(self, value: str):
        if self._last_element is None or self._last_element.type in Type.OPERATOR:
            self._stack.append(CalcParExp(Status.OPEN, value))

        elif self._last_element.type in Type.NUMBER | Type.CONSTANT:
            self._add_operator('*')
            self._add_function(value)
        elif self._last_element.type in Type.PAR_EXP:
            if self._last_element.status in Status.OPEN:
                self._last_element.add_key(value)
            elif self._last_element.status in Status.CLOSE:
                self._add_operator('*')
                self._add_function(value)

    def _add_open_bracket_handler(self, value):
        if self._last_element is None or self._last_element.type in Type.OPERATOR:
            self._stack.append(CalcParExp(Status.OPEN))
        elif self._last_element.type in Type.NUMBER | Type.CONSTANT:
            self._add_operator('*')
            self._add_open_bracket_handler(value)
        elif self._last_element.type in Type.PAR_EXP:
            if self._last_element.status in Status.OPEN:
                self._last_element.add_key(value)
            elif self._last_element.status in Status.CLOSE:
                self._add_operator('*')
                self._add_open_bracket_handler(value)

    def _add_close_bracket_handler(self, value):
        if self._last_element is None or self._last_element.type in Type.OPERATOR:
            return
        if self._last_element.type in Type.NUMBER | Type.CONSTANT:
            if self.status in Status.OPEN:
                if self._last_element.type in Type.NUMBER:
                    self._last_element.optimize()
                self.status = Status.CLOSE
        elif self._last_element.type in Type.PAR_EXP:
            if self._last_element.status in Status.OPEN:
                self._last_element.add_key(value)
            elif self._last_element.status in Status.CLOSE:
                if self.status in Status.OPEN:
                    self.status = Status.CLOSE

    def backspace(self):
        if self._last_element is None:
            super().backspace()
            return
        if self.status in Status.CLOSE:
            self.status = Status.OPEN
            return
        self._backspace_last_element()

    def _backspace_last_element(self):
        if self._last_element is not None:
            self._last_element.backspace()

            if self._last_element.type in Type.EMPTY:
                self._stack.pop()

    def _add_control_statement(self, value):
        if value == '(':
            self._add_open_bracket_handler(value)
        elif value == ')':
            self._add_close_bracket_handler(value)
        elif value == 'bckspc':
            self._backspace_last_element()
        elif value == 'clr':
            self._stack = []
            self.status = Status.MAIN
            self._name = ''
        elif value == '=':
            self.status = Status.COMPLETE

    def add_key(self, value: str):
        if self.status in Status.COMPLETE:
            self.status = Status.MAIN
            if value in self.__NUMBERS:
                self.add_key('clr')
        if value in self.__NUMBERS:
            self._add_number(value)
        elif value in self.__CONSTANTS:
            self._add_constant(value)
        elif value in self.__NEGATE:
            self._negate()
        elif value in self.__OPERATORS:
            self._add_operator(value)
        elif value in self.__FUNCTIONS:
            self._add_function(value)
        elif value in self.__CONTROL_STATEMENTS:
            self._add_control_statement(value)

    def __str__(self):
        open_br = '(' if self.status in Status.OPEN | Status.CLOSE else ''
        close_br = ')' if self.status in Status.CLOSE else ''
        sign = '' if self.sign and self.status else '-'
        return sign + self._name + open_br + ''.join(map(str, self._stack)) + close_br
