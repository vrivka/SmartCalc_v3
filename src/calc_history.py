import pickle
import utils


class CalcHistory:

    def __init__(self, path):
        self.path = utils.get_resource(path)
        try:
            with open(self.path, 'rb') as hist:
                hist = hist.read()
                self.history = pickle.loads(hist)
        except (FileNotFoundError):
            self.history = []

    def add(self, en_expr, str_expr, en_result, str_result):
        for i, hist in enumerate(self.history):
            if hist['expression_string'] == str_expr:
                self.history.pop(i)
        self.history.insert(0, {
            'expression_string': str_expr,
            'result_string': str_result,
            'expression': en_expr,
            'result': en_result
        })

    def on_close(self):
        with open(self.path, 'wb') as hist:
            pickle.dump(self.history, hist)

    def get_all(self):
        str_hitory = []

        for i, hist in enumerate(self.history):
            str_hitory.append({
                'id': i,
                'expr': hist['expression_string'],
                'res': hist['result_string']
            })
        return str_hitory

    def get_expr(self, expr_id):
        return self.history[expr_id]['expression']

    def get_res(self, res_id):
        return self.history[res_id]['result']

    def clear(self):
        self.history = []
