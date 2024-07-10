import simpleeval

from calc_model import CalculatorModel

_key_bindings = {
    'e': 'e',
    '^': '^',
    '(': '(',
    ')': ')',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '0': '0',
    '.': '.',
    '+': '+',
    '-': '-',
    '*': '*',
    '/': '/',
    'Backspace': 'bckspc',
    'bckspc': 'bckspc',
    'n': 'negate',
    'negate': 'negate',
    'E': 'exp',
    'exp': 'exp',
    'P': 'pi',
    'pi': 'pi',
    'q': 'sqrt',
    'sqrt': 'sqrt',
    'm': 'mod',
    'mod': 'mod',
    '%': 'mod',
    's': 'sin',
    'sin': 'sin',
    'S': 'asin',
    'asin': 'asin',
    'c': 'cos',
    'cos': 'cos',
    'C': 'acos',
    'acos': 'acos',
    't': 'tan',
    'tan': 'tan',
    'T': 'atan',
    'atan': 'atan',
    'l': 'ln',
    'ln': 'ln',
    'L': 'log',
    'log': 'log',
    'Delete': 'clr',
    'clr': 'clr'
}


class CalcPresenter:

    def __init__(self, view):
        self._calc_model = CalculatorModel()
        self._calc_veiw = view

    def get_graph_result(self, func, cnv_data):
        try:
            neg_x = cnv_data['neg_x']
            pos_x = cnv_data['pos_x']
            scale = cnv_data['globalScaleX']

            return self._calc_model.graph_result(func, neg_x, pos_x, scale)
        except (SyntaxError, simpleeval.FeatureNotAvailable):
            self._calc_veiw.showError('Error: invalid syntax')
        except simpleeval.FunctionNotDefined:
            self._calc_veiw.showError('Error: function not defined')
        except simpleeval.NameNotDefined:
            self._calc_veiw.showError('Error: only x is defined as a variable')
        return []

    def key_handler(self, key):
        try:
            if key in _key_bindings:
                self._calc_model.add_key(_key_bindings[key])
            elif key in ('Enter', '='):
                self._calc_model.result()
        except SyntaxError:
            self._calc_veiw.showError('Error: syntax error')
        except ValueError:
            self._calc_veiw.showError('Error: value error')
        except ZeroDivisionError:
            self._calc_veiw.showError('Error: division by zero')

        self._calc_veiw.set_entry(self._calc_model.get_expression_string())

    def load_from_history(self, hist):
        hist_type, hist_id = hist.split('-')
        self._calc_model.load_from_history(int(hist_id), hist_type)

        self._calc_veiw.set_entry(self._calc_model.get_expression_string())

    def get_all_history(self):
        return self._calc_model.get_all_history()

    def clear_history(self):
        self._calc_model.clear_history()

    def save_history(self):
        self._calc_model.save_history()
