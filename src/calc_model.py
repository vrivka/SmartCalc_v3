import functools
from math import sqrt, sin, asin, cos, acos, tan, atan, log, log10, e, pi
import numpy as np
import simpleeval

from calc_history import CalcHistory
from calc_parexp import CalcParExp

_functions = {
    "sin": sin,
    "asin": asin,
    "cos": cos,
    "acos": acos,
    "tan": tan,
    "atan": atan,
    "ln": log,
    "log": log10,
    "sqrt": sqrt
}

_constants = {
    'e': e,
    'pi': pi
}


class CalculatorModel:

    def __init__(self):
        self._par_exp = CalcParExp()
        self._history = CalcHistory('history.bin')

    def add_key(self, value):
        self._par_exp.add_key(value)
        return self

    def get_expression_string(self):
        return str(self._par_exp)

    @staticmethod
    @functools.cache
    def __calculate(expression):
        return simpleeval.simple_eval(expression, functions=_functions, names=_constants)

    def graph_result(self, function, neg_x, pos_x, scale):
        function = function.replace('^', '**').replace('mod', '%')
        result = []

        if function != '':
            for int_x in range(neg_x - scale, pos_x + scale, 1):
                for x in np.arange(int_x, int_x + 1, scale / 100):
                    func = function.replace('x', f'({str(x)})')
                    try:
                        y = self.__calculate(func)
                        if isinstance(y, complex):
                            continue
                    except (ZeroDivisionError, ValueError, TypeError):
                        continue
                    result.append([x, y])
            i = 3
            while i < len(result):
                y0 = result[i - 3][1]
                y1 = result[i - 2][1]
                y2 = result[i - 1][1]
                y3 = result[i][1]

                del_y10 = y1 - y0
                del_y32 = y3 - y2
                del_y21 = y2 - y1

                if (del_y10 > 0 and del_y32 > 0 and del_y21 < 0) or (del_y10 < 0 and del_y32 < 0 and del_y21 > 0):
                    result.insert(i - 1, '+' if del_y21 < 0 else '-')
                    i += 2
                i += 1
        return result

    def evaluate(self, expression):
        expression = expression.replace('^', '**').replace('mod', '%')
        return self.__calculate(expression)

    def result(self):
        expression = self.get_expression_string()

        if not expression:
            return
        try:
            res = self.evaluate(expression)
        except simpleeval.NumberTooHigh as exc:
            raise ValueError from exc

        en_expr = self._par_exp.encode()
        str_expr = expression

        self._par_exp.set_result(res)

        en_res = self._par_exp.encode()
        str_res = self.get_expression_string()

        self._history.add(en_expr, str_expr, en_res, str_res)

    def get_all_history(self):
        return self._history.get_all()

    def clear_history(self):
        return self._history.clear()

    def load_from_history(self, hist_id, hist_type):
        if hist_type == 'expr':
            self._par_exp.decode(**self._history.get_expr(hist_id))
        elif hist_type == 'res':
            self._par_exp.decode(**self._history.get_res(hist_id))

    def save_history(self):
        self._history.on_close()
