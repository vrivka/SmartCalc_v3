from enum import Flag, auto


class Type(Flag):
    EMPTY = 0
    NUMBER = auto()
    CONSTANT = auto()
    OPERATOR = auto()
    PAR_EXP = auto()


class CalcElement:

    def __init__(self, _type=Type.EMPTY):
        self.type = _type

    def encode(self):
        return {'type': self.type.name}

    def backspace(self):
        self.type = Type.EMPTY
