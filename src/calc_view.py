import eel

from calc_presenter import CalcPresenter


class CalcView:
    def __init__(self):
        self.presenter = CalcPresenter(self)
        eel.expose(self.keyboard_handler)
        eel.expose(self.graph_data)
        eel.expose(self.get_history)
        eel.expose(self.clear_history)
        eel.expose(self.load_from_history)

    def showError(self, message):
        eel.showErrorMessage(message)

    def set_entry(self, value):
        eel.setEntry(value)

    def keyboard_handler(self, key):
        self.presenter.key_handler(key)

    def graph_data(self, func, cnv_data):
        return self.presenter.get_graph_result(func, cnv_data)

    def get_history(self):
        return self.presenter.get_all_history()

    def clear_history(self):
        self.presenter.clear_history()

    def load_from_history(self, hist):
        self.presenter.load_from_history(hist)
